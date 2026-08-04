---
title: "REST: Efficient and Accelerated EEG Seizure Analysis through Residual State Updates"
source: "https://proceedings.mlr.press/v235/afzal24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/afzal24a/afzal24a.pdf"
categories: ['neuromorphic-computing-and-neural-dynamics-modeling']
tags: ['eeg', 'seizure-detection', 'graph-neural-network', 'residual-state', 'real-time']
venue: "ICML 2024"
tldr: "REST proposes a graph-based residual state update mechanism for efficient real-time EEG seizure detection."
---

# REST: Efficient and Accelerated EEG Seizure Analysis through Residual State Updates

**Source**: [https://proceedings.mlr.press/v235/afzal24a.html](https://proceedings.mlr.press/v235/afzal24a.html)

**TLDR**: REST proposes a graph-based residual state update mechanism for efficient real-time EEG seizure detection.

## Abstract

EEG-based seizure detection models face challenges in terms of inference speed and memory efficiency, limiting their real-time implementation in clinical devices. This paper introduces a novel graph-based residual state update mechanism (REST) for real-time EEG signal analysis in applications such as epileptic seizure detection. By leveraging a combination of graph neural networks and recurrent structures, REST efficiently captures both non-Euclidean geometry and temporal dependencies within EEG data. Our model demonstrates high accuracy in both seizure detection and classification tasks. Notably, REST achieves a remarkable 9-fold acceleration in inference speed compared to state-of-the-art models, while simultaneously demanding substantially less memory than the smallest model employed for this task. These attributes position REST as a promising candidate for real-time implementation in clinical devices, such as Responsive Neurostimulation or seizure alert systems.