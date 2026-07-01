---
title: "RealMAN: A Real-Recorded and Annotated Microphone Array Dataset for Dynamic Speech Enhancement and Localization"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/bf8f6f5b017dc60d0c4e28a7a9a4ee7b-Abstract-Datasets_and_Benchmarks_Track.html"
categories: ['audio-visual-speech-processing-and-benchmarks', 'wearable-biosignal-gesture-activity-benchmarks']
tags: ['microphone-array', 'speech-enhancement', 'source-localization']
venue: "NeurIPS 2024"
tldr: "A large-scale real-recorded and annotated microphone array dataset for training and evaluating multichannel speech enhancement and localization systems."
---

# RealMAN: A Real-Recorded and Annotated Microphone Array Dataset for Dynamic Speech Enhancement and Localization

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/bf8f6f5b017dc60d0c4e28a7a9a4ee7b-Abstract-Datasets_and_Benchmarks_Track.html](https://papers.nips.cc/paper_files/paper/2024/hash/bf8f6f5b017dc60d0c4e28a7a9a4ee7b-Abstract-Datasets_and_Benchmarks_Track.html)

**TLDR**: A large-scale real-recorded and annotated microphone array dataset for training and evaluating multichannel speech enhancement and localization systems.

## Abstract

The training of deep learning-based multichannel speech enhancement and source localization systems relies heavily on the simulation of room impulse response and multichannel diffuse noise, due to the lack of large-scale real-recorded datasets. However, the acoustic mismatch between simulated and real-world data could degrade the model performance when applying in real-world scenarios. To bridge this simulation-to-real gap, this paper presents a new relatively large-scale Real-recorded and annotated Microphone Array speech&Noise (RealMAN) dataset. The proposed dataset is valuable in two aspects: 1) benchmarking speech enhancement and localization algorithms in real scenarios; 2) offering a substantial amount of real-world training data for potentially improving the performance of real-world applications. Specifically, a 32-channel array with high-fidelity microphones is used for recording. A loudspeaker is used for playing source speech signals (about 35 hours of Mandarin speech). A total of 83.7 hours of speech signals (about 48.3 hours for static speaker and 35.4 hours for moving speaker) are recorded in 32 different scenes, and 144.5 hours of background noise are recorded in 31 different scenes. Both speech and noise recording scenes cover various common indoor, outdoor, semi-outdoor and transportation environments, which enables the training of general-purpose speech enhancement and source localization networks. To obtain the task-specific annotations, speaker location is annotated with an omni-directional fisheye camera by automatically detecting the loudspeaker. The direct-path signal is set as the target clean speech for speech enhancement, which is obtained by filtering the source speech signal with an estimated direct-path propagation filter. Baseline experiments demonstrate that i) compared to using simulated data, the proposed dataset is indeed able to train better speech enhancement and source localization networks; ii) using various sub-arrays of the proposed 32-channel microphone array can successfully train variable-array networks that can be directly used to unseen arrays.