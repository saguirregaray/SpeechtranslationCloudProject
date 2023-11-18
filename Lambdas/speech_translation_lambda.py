import boto3
from datetime import datetime
import time
import json


def lambda_handler(event, context):
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']

    print(f'Starting translation process for object s3://{bucket}/{key}')

    transcribe_client = boto3.client('transcribe')
    translate_client = boto3.client('translate')
    polly_client = boto3.client('polly')

    print(f'Services initialized!')

    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    job_name = f"{key.split('/')[-1].split('.')[0]}-{timestamp}"

    output_transcribe_file = f"transcription/{key.split('/')[-1].split('.')[0]}_{timestamp}.txt"
    output_translate_file = f"translation/{key.split('/')[-1].split('.')[0]}_translated_{timestamp}.txt"
    output_audio_file = f"audio/{key.split('/')[-1].split('.')[0]}_translated_{timestamp}.mp3"

    print(f'Transcribe job started!')
    transcribe_response = transcribe_client.start_transcription_job(
        TranscriptionJobName=job_name,
        LanguageCode='en-US',
        MediaFormat='mp3',
        Media={
            'MediaFileUri': f"s3://{bucket}/{key}"
        },
        OutputBucketName=bucket,
        OutputKey=output_transcribe_file
    )

    # Poll the status of the transcription job until it's completed
    while True:
        status = transcribe_client.get_transcription_job(
            TranscriptionJobName=job_name
        )['TranscriptionJob']['TranscriptionJobStatus']

        if status in ['COMPLETED', 'FAILED']:
            break

        time.sleep(5)  # Wait for 5 seconds before polling again

    if status == 'COMPLETED':
        # Get the URI of the transcription file
        transcription_file_uri = transcribe_client.get_transcription_job(
            TranscriptionJobName=job_name
        )['TranscriptionJob']['Transcript']['TranscriptFileUri']

        print(f'Transcription file URI: {transcription_file_uri}')

        # Retrieve the transcription file content from S3
        s3 = boto3.client('s3')
        response = s3.get_object(Bucket=bucket, Key=output_transcribe_file)
        transcription_text = json.loads(response['Body'].read().decode('utf-8'))['results']['transcripts'][0][
            'transcript']

        print(f'Transcribed text: {transcription_text}')

        # Translate the retrieved transcription text
        translation_response = translate_client.translate_text(
            Text=transcription_text,
            SourceLanguageCode='en',
            TargetLanguageCode='es'
        )

        translated_text = translation_response['TranslatedText']

        print(f'Translated text: {translated_text}')

        print(f'Synthesis job started!')

        polly_response = polly_client.synthesize_speech(
            Text=translated_text,
            OutputFormat='mp3',
            VoiceId='Joanna'
        )

        print(f'Synthesis job completed and stored in {output_audio_file}!')

        polly_audio_stream = polly_response['AudioStream'].read()
        s3 = boto3.resource('s3')
        s3.Bucket(bucket).put_object(
            Key=output_audio_file,
            Body=polly_audio_stream,
            ContentType='audio/mpeg'
        )

        print(f'Output saved as {output_audio_file}')

        return {
            'statusCode': 200,
            'body': 'Translation and audio synthesis completed!'
        }
    else:
        return {
            'statusCode': 500,
            'body': 'Transcription job failed!'
        }
