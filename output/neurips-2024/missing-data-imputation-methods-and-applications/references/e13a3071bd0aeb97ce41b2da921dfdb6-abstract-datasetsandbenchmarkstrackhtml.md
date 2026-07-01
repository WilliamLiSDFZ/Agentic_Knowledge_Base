---
title: "Pedestrian Trajectory Prediction with Missing Data: Datasets, Imputation, and Benchmarking"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/e13a3071bd0aeb97ce41b2da921dfdb6-Abstract-Datasets_and_Benchmarks_Track.html"
categories: ['missing-data-imputation-methods-and-applications', 'autonomous-driving-and-trajectory-prediction']
tags: ['trajectory-prediction', 'missing-data', 'imputation', 'pedestrian', 'benchmarking']
venue: "NeurIPS 2024"
tldr: "Presents datasets, imputation strategies, and benchmarks for pedestrian trajectory prediction under missing observation conditions."
---

# Pedestrian Trajectory Prediction with Missing Data: Datasets, Imputation, and Benchmarking

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/e13a3071bd0aeb97ce41b2da921dfdb6-Abstract-Datasets_and_Benchmarks_Track.html](https://papers.nips.cc/paper_files/paper/2024/hash/e13a3071bd0aeb97ce41b2da921dfdb6-Abstract-Datasets_and_Benchmarks_Track.html)

**TLDR**: Presents datasets, imputation strategies, and benchmarks for pedestrian trajectory prediction under missing observation conditions.

## Abstract

Pedestrian trajectory prediction is crucial for several applications such as robotics and self-driving vehicles. Significant progress has been made in the past decade thanks to the availability of pedestrian trajectory datasets, which enable trajectory prediction methods to learn from pedestrians' past movements and predict future trajectories. However, these datasets and methods typically assume that the observed trajectory sequence is complete, ignoring real-world issues such as sensor failure, occlusion, and limited fields of view that can result in missing values in observed trajectories. To address this challenge, we present TrajImpute, a pedestrian trajectory prediction dataset that simulates missing coordinates in the observed trajectory, enhancing real-world applicability. TrajImpute maintains a uniform distribution of missing data within the observed trajectories. In this work, we comprehensively examine several imputation methods to reconstruct the missing coordinates and benchmark them for imputing pedestrian trajectories. Furthermore, we provide a thorough analysis of recent trajectory prediction methods and evaluate the performance of these models on the imputed trajectories. Our experimental evaluation of the imputation and trajectory prediction methods offers several valuable insights. Our dataset provides a foundational resource for future research on imputation-aware pedestrian trajectory prediction, potentially accelerating the deployment of these methods in real-world applications. Publicly accessible links to the datasets and code files are available at https://github.com/Pranav-chib/TrajImpute.