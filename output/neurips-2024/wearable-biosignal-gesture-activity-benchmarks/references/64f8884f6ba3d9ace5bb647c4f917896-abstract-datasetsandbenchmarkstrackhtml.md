---
title: "emg2pose: A Large and Diverse Benchmark for Surface Electromyographic Hand Pose Estimation"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/64f8884f6ba3d9ace5bb647c4f917896-Abstract-Datasets_and_Benchmarks_Track.html"
categories: ['wearable-biosignal-gesture-activity-benchmarks', 'audio-visual-speech-processing-and-benchmarks']
tags: ['electromyography', 'hand-pose-estimation', 'benchmark']
venue: "NeurIPS 2024"
tldr: "Presents a large diverse benchmark for surface EMG-based hand pose estimation enabling new human-computer interaction schemes."
---

# emg2pose: A Large and Diverse Benchmark for Surface Electromyographic Hand Pose Estimation

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/64f8884f6ba3d9ace5bb647c4f917896-Abstract-Datasets_and_Benchmarks_Track.html](https://papers.nips.cc/paper_files/paper/2024/hash/64f8884f6ba3d9ace5bb647c4f917896-Abstract-Datasets_and_Benchmarks_Track.html)

**TLDR**: Presents a large diverse benchmark for surface EMG-based hand pose estimation enabling new human-computer interaction schemes.

## Abstract

Hands are the primary means through which humans interact with the world. Reliable and always-available hand pose inference could yield new and intuitive control schemes for human-computer interactions, particularly in virtual and augmented reality. Computer vision is effective but requires one or multiple cameras and can struggle with occlusions, limited field of view, and poor lighting. Wearable wrist-based surface electromyography (sEMG) presents a promising alternative as an always-available modality sensing muscle activities that drive hand motion. However, sEMG signals are strongly dependent on user anatomy and sensor placement; existing sEMG models have thus required hundreds of users and device placements to effectively generalize for tasks other than pose inference. To facilitate progress on sEMG pose inference, we introduce the emg2pose benchmark, which is to our knowledge the first publicly available dataset of high-quality hand pose labels and wrist sEMG recordings. emg2pose contains 2kHz, 16 channel sEMG and pose labels from a 26-camera motion capture rig for 193 users, 370 hours, and 29 stages with diverse gestures - a scale comparable to vision-based hand pose datasets. We provide competitive baselines and challenging tasks evaluating real-world generalization scenarios: held-out users, sensor placements, and stages. This benchmark provides the machine learning community a platform for exploring complex generalization problems, holding potential to significantly enhance the development of sEMG-based human-computer interactions.