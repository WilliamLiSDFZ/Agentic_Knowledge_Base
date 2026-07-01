---
title: "A New Multi-Source Light Detection Benchmark and Semi-Supervised Focal Light Detection"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/8114d5aec06601f02446b9fc9a1d5ba4-Abstract-Datasets_and_Benchmarks_Track.html"
categories: ['autonomous-driving-and-trajectory-prediction', 'ai-benchmarking-and-evaluation-methodology']
tags: ['light-detection', 'autonomous-driving', 'semi-supervised', 'benchmark']
venue: "NeurIPS 2024"
tldr: "A new multi-source light detection benchmark for driving scenarios paired with a semi-supervised focal detection method."
---

# A New Multi-Source Light Detection Benchmark and Semi-Supervised Focal Light Detection

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/8114d5aec06601f02446b9fc9a1d5ba4-Abstract-Datasets_and_Benchmarks_Track.html](https://papers.nips.cc/paper_files/paper/2024/hash/8114d5aec06601f02446b9fc9a1d5ba4-Abstract-Datasets_and_Benchmarks_Track.html)

**TLDR**: A new multi-source light detection benchmark for driving scenarios paired with a semi-supervised focal detection method.

## Abstract

This paper addresses a multi-source light detection (LD) problem from vehicles, traffic signals, and streetlights under driving scenarios. Albeit it is crucial for autonomous driving and night vision, this problem has not been yet focused on as much as other object detection (OD). One of the main reasons is the absence of a public available LD benchmark dataset. Therefore, we construct a new large LD dataset consisting of different light sources via heavy annotation: YouTube Driving Light Detection dataset (YDLD). Compared to the existing LD datasets, our dataset has much more images and box annotations for multi-source lights. We also provide rigorous statistical analysis and transfer learning comparison of other well-known detection benchmark datasets to prove the generality of our YDLD.For the recent object detectors, we achieve the extensive comparison results on YDLD. However, they tend to yield the low mAP scores due to the intrinsic challenges of LD caused by very tiny size and similar appearance. To resolve those, we design a novel lightness focal loss which penalizes miss-classified samples more and a lightness spatial attention prior by reflecting a global scene context. In addition, we develop a semi-supervised focal light detection (SS-FLD) by embedding our lightness focal loss into the semi-supervised object detection (SSOD). We prove that our methods can consistently boost mAP to the variety of types of recent detectors on YDLD. We will open both YDLD and SS-FLD code at https://github.com/YDLD-dataset/YDLD.