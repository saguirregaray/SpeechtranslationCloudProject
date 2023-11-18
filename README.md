# Project Proposal: Real-Time Voice Translation and Input Voice Simulator

## Problem Statement

Language differences create significant challenges for online educational videos and podcasts. These barriers can limit the global reach of valuable content and hinder understanding for viewers and listeners. We aim to tackle this issue by creating a cloud-based system that provides real-time voice translation for educational content. What makes our proposed solution unique is that it maintains the original speaker's voice, ensuring a seamless, natural, and immersive learning experience.

## Motivation

Imagine a world where anyone can access educational content in their native language. This system will open up a world of knowledge for diverse audiences and promote inclusive learning.

Effective communication is vital in both personal and professional settings. Language differences often lead to misunderstandings, cultural insensitivity, and a lack of inclusivity. By providing real-time voice translation, we can empower people to communicate effortlessly across language boundaries.

## Existing Solutions/Literature Review

While there are no exact 1:1 solutions that have been built to address our specific goal, we have identified several libraries and products (some of which we have used in the past) that will aid us in building our product. These include the OpenAI Whisper API, Deepgram transcription API, and Vocode (an SDK for building LLM-augmented voice applications). We will also take some inspiration from this AWS case-study, specifically using the SUPERB dataset and leveraging a combination of AWS Sagemaker and Huggingface to experiment with various models for real-time inference and audio-generation. 

## Success Criteria/Targets

Our project's success will be measured based on the following criteria:
- **Accuracy:** Achieve an accuracy rate of at least 75% in voice recognition and translation.
- **Latency:** Ensure that the system can perform real-time translation with a latency of less than 3 seconds.
- **Scalability:** Develop a system architecture that can handle a minimum of 1,000 concurrent users.
- **User Satisfaction:** Conduct user surveys and aim for a satisfaction rating of 90% or higher.
- **Security:** Implement robust security measures to protect user data and ensure privacy.

If time permits, we aim to provide compatibility with popular communication platforms (e.g., Youtube, Spotify), and even extend our implementation to include multi-speaker contexts. 

## Target Audience

Our target audience would be students interested in Youtube educational content or Podcasts, or potential users using any educational materials delivered by human voice. In the future, we may extend the scope to various domains other than educational content such as movies, gaming, and etc.

## Data Handling

Our system will handle a vast amount of audio data for voice recognition and translation. Data sources will include:
- **Audio Input:** Users' spoken language input, captured through microphones.
- **Language Models:** Pre-trained language models and data sources for transcribing the audio, translating it and outputting it in the speaker’s voice.

We have identified several open voice datasets including Common Voice, Google Audioset, and VoxCeleb which we might possibly use.
To ensure data security and privacy, we will implement encryption and comply with data protection regulations.
