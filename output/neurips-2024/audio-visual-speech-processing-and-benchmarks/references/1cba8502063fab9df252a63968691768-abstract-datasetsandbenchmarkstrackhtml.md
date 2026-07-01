---
title: "EEVR: A Dataset of Paired Physiological Signals and Textual Descriptions for Joint Emotion Representation Learning"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/1cba8502063fab9df252a63968691768-Abstract-Datasets_and_Benchmarks_Track.html"
categories: ['wearable-biosignal-gesture-activity-benchmarks', 'audio-visual-speech-processing-and-benchmarks']
tags: ['physiological-signals', 'emotion-recognition', 'multimodal-dataset']
venue: "NeurIPS 2024"
tldr: "EEVR is a new dataset pairing physiological signals with textual descriptions for language-supervised emotion recognition pre-training."
---

# EEVR: A Dataset of Paired Physiological Signals and Textual Descriptions for Joint Emotion Representation Learning

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/1cba8502063fab9df252a63968691768-Abstract-Datasets_and_Benchmarks_Track.html](https://papers.nips.cc/paper_files/paper/2024/hash/1cba8502063fab9df252a63968691768-Abstract-Datasets_and_Benchmarks_Track.html)

**TLDR**: EEVR is a new dataset pairing physiological signals with textual descriptions for language-supervised emotion recognition pre-training.

## Abstract

EEVR (Emotion Elicitation in Virtual Reality) is a novel dataset specifically designed for language supervision-based pre-training of emotion recognition tasks, such as valence and arousal classification. It features high-quality physiological signals, including electrodermal activity (EDA) and photoplethysmography (PPG), acquired through emotion elicitation via 360-degree virtual reality (VR) videos.Additionally, it includes subject-wise textual descriptions of emotions experienced during each stimulus gathered from qualitative interviews. The dataset consists of recordings from 37 participants and is the first dataset to pair raw text with physiological signals, providing additional contextual information that objective labels cannot offer. To leverage this dataset, we introduced the Contrastive Language Signal Pre-training (CLSP) method, which jointly learns representations using pairs of physiological signals and textual descriptions. Our results show that integrating self-reported textual descriptions with physiological signals significantly improves performance on emotion recognition tasks, such as arousal and valence classification. Moreover, our pre-trained CLSP model demonstrates strong zero-shot transferability to existing datasets, outperforming supervised baseline models, suggesting that the representations learned by our method are more contextualized and generalized. The dataset also includes baseline models for arousal, valence, and emotion classification, as well as code for data cleaning and feature extraction. Further details and access to the dataset are available at https://melangelabiiitd.github.io/EEVR/.