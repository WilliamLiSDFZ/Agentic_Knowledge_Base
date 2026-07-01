---
title: "A Benchmark Suite for Evaluating Neural Mutual Information Estimators on Unstructured Datasets"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/525bd8aedafa375564f73bacdef411e5-Abstract-Datasets_and_Benchmarks_Track.html"
categories: ['ai-benchmarking-and-evaluation-methodology']
tags: ['mutual-information-estimation', 'benchmark', 'unstructured-data']
venue: "NeurIPS 2024"
tldr: "Introduces a benchmark suite for systematically evaluating neural mutual information estimators on unstructured datasets."
---

# A Benchmark Suite for Evaluating Neural Mutual Information Estimators on Unstructured Datasets

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/525bd8aedafa375564f73bacdef411e5-Abstract-Datasets_and_Benchmarks_Track.html](https://papers.nips.cc/paper_files/paper/2024/hash/525bd8aedafa375564f73bacdef411e5-Abstract-Datasets_and_Benchmarks_Track.html)

**TLDR**: Introduces a benchmark suite for systematically evaluating neural mutual information estimators on unstructured datasets.

## Abstract

Mutual Information (MI) is a fundamental metric for quantifying dependency between two random variables. When we can access only the samples, but not the underlying distribution functions, we can evaluate MI using sample-based estimators. Assessment of such MI estimators, however, has almost always relied on analytical datasets including Gaussian multivariates. Such datasets allow analytical calculations of the true MI values, but they are limited in that they do not reflect the complexities of real-world datasets. This study introduces a comprehensive benchmark suite for evaluating neural MI estimators on unstructured datasets, specifically focusing on images and texts. By leveraging same-class sampling for positive pairing and introducing a binary symmetric channel trick, we show that we can accurately manipulate true MI values of real-world datasets. Using the benchmark suite, we investigate seven challenging scenarios, shedding light on the reliability of neural MI estimators for unstructured datasets.