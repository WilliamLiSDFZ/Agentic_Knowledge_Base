---
title: "IndicVoices-R: Unlocking a Massive Multilingual Multi-speaker Speech Corpus for Scaling Indian TTS"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/7dfcaf4512bbf2a807a783b90afb6c09-Abstract-Datasets_and_Benchmarks_Track.html"
categories: ['audio-visual-speech-processing-and-benchmarks']
tags: ['text-to-speech', 'Indian-languages', 'multilingual-corpus']
venue: "NeurIPS 2024"
tldr: "Presents IndicVoices-R, a large multilingual multi-speaker speech corpus to scale TTS for low-resource Indian languages."
---

# IndicVoices-R: Unlocking a Massive Multilingual Multi-speaker Speech Corpus for Scaling Indian TTS

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/7dfcaf4512bbf2a807a783b90afb6c09-Abstract-Datasets_and_Benchmarks_Track.html](https://papers.nips.cc/paper_files/paper/2024/hash/7dfcaf4512bbf2a807a783b90afb6c09-Abstract-Datasets_and_Benchmarks_Track.html)

**TLDR**: Presents IndicVoices-R, a large multilingual multi-speaker speech corpus to scale TTS for low-resource Indian languages.

## Abstract

Recent advancements in text-to-speech (TTS) synthesis show that large-scale models trained with extensive web data produce highly natural-sounding output. However, such data is scarce for Indian languages due to the lack of high-quality, manually subtitled data on platforms like LibriVox or YouTube. To address this gap, we enhance existing large-scale ASR datasets containing natural conversations collected in low-quality environments to generate high-quality TTS training data. Our pipeline leverages the cross-lingual generalization of denoising and speech enhancement models trained on English and applied to Indian languages. This results in IndicVoices-R (IV-R), the largest multilingual Indian TTS dataset derived from an ASR dataset, with 1,704 hours of high-quality speech from 10,496 speakers across 22 Indian languages. IV-R matches the quality of gold-standard TTS datasets like LJSpeech, LibriTTS, and IndicTTS. We also introduce the IV-R Benchmark, the first to assess zero-shot, few-shot, and many-shot speaker generalization capabilities of TTS models on Indian voices, ensuring diversity in age, gender, and style. We demonstrate that fine-tuning an English pre-trained model on a combined dataset of high-quality IndicTTS and our IV-R dataset results in better zero-shot speaker generalization compared to fine-tuning on the IndicTTS dataset alone. Further, our evaluation reveals limited zero-shot generalization for Indian voices in TTS models trained on prior datasets, which we improve by fine-tuning the model on our data containing diverse set of speakers across language families. We open-source code and data for all 22 official Indian languages.