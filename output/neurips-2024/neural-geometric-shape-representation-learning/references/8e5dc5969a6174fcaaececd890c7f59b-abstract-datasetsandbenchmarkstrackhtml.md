---
title: "Point Cloud Matters: Rethinking the Impact of Different Observation Spaces on Robot Learning"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/8e5dc5969a6174fcaaececd890c7f59b-Abstract-Datasets_and_Benchmarks_Track.html"
categories: ['reinforcement-learning-optimization-and-decision-making', 'neural-geometric-shape-representation-learning']
tags: ['point-clouds', 'robot-learning', 'observation-spaces']
venue: "NeurIPS 2024"
tldr: "Systematically studies the impact of different observation modalities including point clouds on robot learning performance and policy design."
---

# Point Cloud Matters: Rethinking the Impact of Different Observation Spaces on Robot Learning

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/8e5dc5969a6174fcaaececd890c7f59b-Abstract-Datasets_and_Benchmarks_Track.html](https://papers.nips.cc/paper_files/paper/2024/hash/8e5dc5969a6174fcaaececd890c7f59b-Abstract-Datasets_and_Benchmarks_Track.html)

**TLDR**: Systematically studies the impact of different observation modalities including point clouds on robot learning performance and policy design.

## Abstract

In robot learning, the observation space is crucial due to the distinct characteristics of different modalities, which can potentially become a bottleneck alongside policy design. In this study, we explore the influence of various observation spaces on robot learning, focusing on three predominant modalities: RGB, RGB-D, and point cloud. We introduce OBSBench, a benchmark comprising two simulators and 125 tasks, along with standardized pipelines for various encoders and policy baselines. Extensive experiments on diverse contact-rich manipulation tasks reveal a notable trend: point cloud-based methods, even those with the simplest designs, frequently outperform their RGB and RGB-D counterparts. This trend persists in both scenarios: training from scratch and utilizing pre-training. Furthermore, our findings demonstrate that point cloud observations often yield better policy performance and significantly stronger generalization capabilities across various geometric and visual conditions. These outcomes suggest that the 3D point cloud is a valuable observation modality for intricate robotic tasks. We also suggest that incorporating both appearance and coordinate information can enhance the performance of point cloud methods. We hope our work provides valuable insights and guidance for designing more generalizable and robust robotic models.