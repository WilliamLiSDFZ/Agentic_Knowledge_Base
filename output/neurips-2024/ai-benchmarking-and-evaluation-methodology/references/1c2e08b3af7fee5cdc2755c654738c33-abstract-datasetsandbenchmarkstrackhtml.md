---
title: "FT-AED: Benchmark Dataset for Early Freeway Traffic Anomalous Event Detection"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/1c2e08b3af7fee5cdc2755c654738c33-Abstract-Datasets_and_Benchmarks_Track.html"
categories: ['ai-benchmarking-and-evaluation-methodology', 'autonomous-driving-and-trajectory-prediction']
tags: ['traffic-anomaly-detection', 'freeway-benchmark', 'event-detection', 'dataset']
venue: "NeurIPS 2024"
tldr: "FT-AED introduces a benchmark dataset specifically designed for early detection of anomalous traffic events on freeways using real-world sensor data."
---

# FT-AED: Benchmark Dataset for Early Freeway Traffic Anomalous Event Detection

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/1c2e08b3af7fee5cdc2755c654738c33-Abstract-Datasets_and_Benchmarks_Track.html](https://papers.nips.cc/paper_files/paper/2024/hash/1c2e08b3af7fee5cdc2755c654738c33-Abstract-Datasets_and_Benchmarks_Track.html)

**TLDR**: FT-AED introduces a benchmark dataset specifically designed for early detection of anomalous traffic events on freeways using real-world sensor data.

## Abstract

Early and accurate detection of anomalous events on the freeway, such as accidents, can improve emergency response and clearance. However, existing delays and mistakes from manual crash reporting records make it a difficult problem to solve. Current large-scale freeway traffic datasets are not designed for anomaly detection and ignore these challenges. In this paper, we introduce the first large-scale lane-level freeway traffic dataset for anomaly detection. Our dataset consists of a month of weekday radar detection sensor data collected in 4 lanes along an 18-mile stretch of Interstate 24 heading toward Nashville, TN, comprising over 3.7 million sensor measurements. We also collect official crash reports from the Tennessee Department of Transportation Traffic Management Center and manually label all other potential anomalies in the dataset. To show the potential for our dataset to be used in future machine learning and traffic research, we benchmark numerous deep learning anomaly detection models on our dataset. We find that unsupervised graph neural network autoencoders are a promising solution for this problem and that ignoring spatial relationships leads to decreased performance. We demonstrate that our methods can reduce reporting delays by over 10 minutes on average while detecting 75% of crashes. Our dataset and all preprocessing code needed to get started are publicly released at https://vu.edu/ft-aed/ to facilitate future research.