---
title: "EMGBench: Benchmarking Out-of-Distribution Generalization and Adaptation for Electromyography"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/59fe60482e2e5faf557c37d121994663-Abstract-Datasets_and_Benchmarks_Track.html"
categories: ['wearable-biosignal-gesture-activity-benchmarks']
tags: ['electromyography', 'out-of-distribution-generalization', 'benchmark']
venue: "NeurIPS 2024"
tldr: "EMGBench is the first benchmark evaluating out-of-distribution generalization and adaptation of EMG classification algorithms."
---

# EMGBench: Benchmarking Out-of-Distribution Generalization and Adaptation for Electromyography

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/59fe60482e2e5faf557c37d121994663-Abstract-Datasets_and_Benchmarks_Track.html](https://papers.nips.cc/paper_files/paper/2024/hash/59fe60482e2e5faf557c37d121994663-Abstract-Datasets_and_Benchmarks_Track.html)

**TLDR**: EMGBench is the first benchmark evaluating out-of-distribution generalization and adaptation of EMG classification algorithms.

## Abstract

This paper introduces the first generalization and adaptation benchmark using machine learning for evaluating out-of-distribution performance of electromyography (EMG) classification algorithms. The ability of an EMG classifier to handle inputs drawn from a different distribution than the training distribution is critical for real-world deployment as a control interface. By predicting the user’s intended gesture using EMG signals, we can create a wearable solution to control assistive technologies, such as computers, prosthetics, and mobile manipulator robots. This new out-of-distribution benchmark consists of two major tasks that have utility for building robust and adaptable control interfaces: 1) intersubject classification, and 2) adaptation using train-test splits for time-series. This benchmark spans nine datasets, the largest collection of EMG datasets in a benchmark. Among these, a new dataset is introduced, featuring a novel, easy-to-wear high-density EMG wearable for data collection. The lack of open-source benchmarks has made comparing accuracy results between papers challenging for the EMG research community. This new benchmark provides researchers with a valuable resource for analyzing practical measures of out-of-distribution performance for EMG datasets. Our code and data from our new dataset can be found at emgbench.github.io.