---
title: "Infusing Synthetic Data with Real-World Patterns for Zero-Shot Material State Segmentation"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/6ef4a4b387a5a547ea699f3df7fc1248-Abstract-Datasets_and_Benchmarks_Track.html"
categories: ['generative-models-for-visual-style-and-appearance', 'visual-language-multimodal-generation-reasoning']
tags: ['material-segmentation', 'synthetic-data', 'zero-shot-learning']
venue: "NeurIPS 2024"
tldr: "A method infusing synthetic data with real-world patterns enables zero-shot segmentation of material states like wetness, stains, and minerals."
---

# Infusing Synthetic Data with Real-World Patterns for Zero-Shot Material State Segmentation

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/6ef4a4b387a5a547ea699f3df7fc1248-Abstract-Datasets_and_Benchmarks_Track.html](https://papers.nips.cc/paper_files/paper/2024/hash/6ef4a4b387a5a547ea699f3df7fc1248-Abstract-Datasets_and_Benchmarks_Track.html)

**TLDR**: A method infusing synthetic data with real-world patterns enables zero-shot segmentation of material states like wetness, stains, and minerals.

## Abstract

Visual recognition of materials and their states is essential for understanding the physical world, from identifying wet regions on surfaces or stains on fabrics to detecting infected areas or minerals in rocks. Collecting data that captures this vast variability is complex due to the scattered and gradual nature of material states. Manually annotating real-world images is constrained by cost and precision, while synthetic data, although accurate and inexpensive, lacks real-world diversity. This work aims to bridge this gap by infusing patterns automatically extracted from real-world images into synthetic data. Hence, patterns collected from natural images are used to generate and map materials into synthetic scenes. This unsupervised approach captures the complexity of the real world while maintaining the precision and scalability of synthetic data. We also present the first comprehensive benchmark for zero-shot material state segmentation, utilizing real-world images across a diverse range of domains, including food, soils, construction, plants, liquids, and more, each appears in various states such as wet, dry, infected, cooked, burned, and many others. The annotation includes partial similarity between regions with similar but not identical materials and hard segmentation of only identical material states. This benchmark eluded top foundation models, exposing the limitations of existing data collection methods. Meanwhile, nets trained on the infused data performed significantly better on this and related tasks. The dataset, code, and trained model are publicly available. We also share 300,000 extracted textures and SVBRDF/PBR materials to facilitate future datasets generation.