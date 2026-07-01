---
title: "Expecting The Unexpected: Towards Broad Out-Of-Distribution Detection"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/ec80d18205e39d42a27192d5f3ddd688-Abstract-Datasets_and_Benchmarks_Track.html"
categories: ['machine-learning-theory-and-evaluation-methods', 'statistical-testing-under-distribution-shift']
tags: ['out-of-distribution-detection', 'distribution-shift', 'anomaly-detection']
venue: "NeurIPS 2024"
tldr: "Proposes a broader framework for OOD detection that handles multiple types of distribution shifts beyond novel class detection."
---

# Expecting The Unexpected: Towards Broad Out-Of-Distribution Detection

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/ec80d18205e39d42a27192d5f3ddd688-Abstract-Datasets_and_Benchmarks_Track.html](https://papers.nips.cc/paper_files/paper/2024/hash/ec80d18205e39d42a27192d5f3ddd688-Abstract-Datasets_and_Benchmarks_Track.html)

**TLDR**: Proposes a broader framework for OOD detection that handles multiple types of distribution shifts beyond novel class detection.

## Abstract

Deployed machine learning systems require some mechanism to detect out-of-distribution (OOD) inputs. Existing research mainly focuses on one type of distribution shift: detecting samples from novel classes, absent from the training set. However, real-world systems encounter a broad variety of anomalous inputs, and the OOD literature neglects this diversity. This work categorizes five distinct types of distribution shifts and critically evaluates the performance of recent OOD detection methods on each of them. We publicly release our benchmark under the name BROAD (Benchmarking Resilience Over Anomaly Diversity). We find that while these methods excel in detecting novel classes, their performances are inconsistent across other types of distribution shifts. In other words, they can only reliably detect unexpected inputs that they have been specifically designed to expect. As a first step toward broad OOD detection, we learn a Gaussian mixture generative model for existing detection scores, enabling an ensemble detection approach that is more consistent and comprehensive for broad OOD detection, with improved performances over existing methods. We release code to build BROAD to facilitate a more comprehensive evaluation of novel OOD detectors.