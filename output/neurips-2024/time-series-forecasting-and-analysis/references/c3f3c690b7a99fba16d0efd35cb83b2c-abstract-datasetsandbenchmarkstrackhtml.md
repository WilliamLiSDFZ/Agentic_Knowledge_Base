---
title: "The Elephant in the Room: Towards A Reliable Time-Series Anomaly Detection Benchmark"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/c3f3c690b7a99fba16d0efd35cb83b2c-Abstract-Datasets_and_Benchmarks_Track.html"
categories: ['time-series-forecasting-and-analysis']
tags: ['anomaly-detection', 'benchmark-evaluation', 'time-series']
venue: "NeurIPS 2024"
tldr: "Identifies and addresses critical flaws in time-series anomaly detection benchmarks including dataset issues and biased evaluation metrics."
---

# The Elephant in the Room: Towards A Reliable Time-Series Anomaly Detection Benchmark

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/c3f3c690b7a99fba16d0efd35cb83b2c-Abstract-Datasets_and_Benchmarks_Track.html](https://papers.nips.cc/paper_files/paper/2024/hash/c3f3c690b7a99fba16d0efd35cb83b2c-Abstract-Datasets_and_Benchmarks_Track.html)

**TLDR**: Identifies and addresses critical flaws in time-series anomaly detection benchmarks including dataset issues and biased evaluation metrics.

## Abstract

Time-series anomaly detection is a fundamental task across scientific fields and industries. However, the field has long faced the ``elephant in the room:'' critical issues including flawed datasets, biased evaluation measures, and inconsistent benchmarking practices that have remained largely ignored and unaddressed.  We introduce the TSB-AD to systematically tackle these issues in the following three aspects: (i) Dataset Integrity: with 1070 high-quality time series from a diverse collection of 40 datasets (doubling the size of the largest collection and four times the number of existing curated datasets), we provide the first large-scale, heterogeneous, meticulously curated dataset that combines the effort of human perception and model interpretation; (ii) Measure Reliability: by revealing issues and biases in evaluation measures, we identify the most reliable and accurate measure, namely, VUS-PR for anomaly detection in time series to address concerns from the community; and (iii) Comprehensive Benchmarking: with a broad spectrum of 40 detection algorithms, from statistical methods to the latest foundation models, we perform a comprehensive evaluation that includes a thorough hyperparameter tuning and a unified setup for a fair and reproducible comparison. Our findings challenge the conventional wisdom regarding the superiority of advanced neural network architectures, revealing that simpler architectures and statistical methods often yield better performance. The promising performance of neural networks on multivariate cases and foundation models on point anomalies highlights the need for further advancements in these methods. We open-source the benchmark at https://github.com/TheDatumOrg/TSB-AD to promote further research.