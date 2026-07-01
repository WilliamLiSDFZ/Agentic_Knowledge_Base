---
title: "Infer Induced Sentiment of Comment Response to Video: A New Task, Dataset and Baseline"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/bbf090d264b94d29260f5303efea868c-Abstract-Datasets_and_Benchmarks_Track.html"
categories: ['audio-visual-speech-processing-and-benchmarks']
tags: ['sentiment-analysis', 'video-multimodal', 'viewer-induced-sentiment']
venue: "NeurIPS 2024"
tldr: "A new task, dataset, and baseline are introduced for inferring the sentiment induced in viewers by video content, going beyond in-video sentiment analysis."
---

# Infer Induced Sentiment of Comment Response to Video: A New Task, Dataset and Baseline

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/bbf090d264b94d29260f5303efea868c-Abstract-Datasets_and_Benchmarks_Track.html](https://papers.nips.cc/paper_files/paper/2024/hash/bbf090d264b94d29260f5303efea868c-Abstract-Datasets_and_Benchmarks_Track.html)

**TLDR**: A new task, dataset, and baseline are introduced for inferring the sentiment induced in viewers by video content, going beyond in-video sentiment analysis.

## Abstract

Existing video multi-modal sentiment analysis mainly focuses on the sentiment expression of people within the video, yet often neglects the induced sentiment of viewers while watching the videos. Induced sentiment of viewers is essential for inferring the public response to videos and has broad application in analyzing public societal sentiment, effectiveness of advertising and other areas. The micro videos and the related comments provide a rich application scenario for viewers’ induced sentiment analysis. In light of this, we introduces a novel research task, Multimodal Sentiment Analysis for Comment Response of Video Induced(MSA-CRVI), aims to infer opinions and emotions according to comments response to micro video. Meanwhile, we manually annotate a dataset named Comment Sentiment toward to Micro Video (CSMV) to support this research. It is the largest video multi-modal sentiment dataset in terms of scale and video duration to our knowledge, containing 107, 267 comments and 8, 210 micro videos with a video duration of 68.83 hours. To infer the induced sentiment of comment should leverage the video content, we propose the Video Content-aware Comment Sentiment Analysis (VC-CSA) method as a baseline to address the challenges inherent in this new task. Extensive experiments demonstrate that our method is showing significant improvements over other established baselines. We make the dataset and source code publicly available at https://github.com/IEIT-AGI/MSA-CRVI.