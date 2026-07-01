---
title: "CableInspect-AD: An Expert-Annotated Anomaly Detection Dataset"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/76d9dd096d9469d6b7e732f0cddb51b3-Abstract-Datasets_and_Benchmarks_Track.html"
categories: ['ai-benchmarking-and-evaluation-methodology']
tags: ['anomaly-detection', 'benchmark-dataset', 'power-line-inspection', 'robotics', 'expert-annotation']
venue: "NeurIPS 2024"
tldr: "CableInspect-AD introduces an expert-annotated visual anomaly detection dataset for robotic power line cable inspection to study model transferability to critical applications."
---

# CableInspect-AD: An Expert-Annotated Anomaly Detection Dataset

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/76d9dd096d9469d6b7e732f0cddb51b3-Abstract-Datasets_and_Benchmarks_Track.html](https://papers.nips.cc/paper_files/paper/2024/hash/76d9dd096d9469d6b7e732f0cddb51b3-Abstract-Datasets_and_Benchmarks_Track.html)

**TLDR**: CableInspect-AD introduces an expert-annotated visual anomaly detection dataset for robotic power line cable inspection to study model transferability to critical applications.

## Abstract

Machine learning models are increasingly being deployed in real-world contexts. However, systematic studies on their transferability to specific and critical applications are underrepresented in the research literature. An important example is visual anomaly detection (VAD) for robotic power line inspection. While existing VAD methods perform well in controlled environments, real-world scenarios present diverse and unexpected anomalies that current datasets fail to capture. To address this gap, we introduce CableInspect-AD, a high-quality, publicly available dataset created and annotated by domain experts from Hydro-Québec, a Canadian public utility. This dataset includes high-resolution images with challenging real-world anomalies, covering defects with varying severity levels. To address the challenges of collecting diverse anomalous and nominal examples for setting a detection threshold, we propose an enhancement to the celebrated PatchCore algorithm. This enhancement enables its use in scenarios with limited labeled data. We also present a comprehensive evaluation protocol based on cross-validation to assess models' performances. We evaluate our Enhanced-PatchCore for few-shot and many-shot detection, and Vision-Language Models for zero-shot detection. While promising, these models struggle to detect all anomalies, highlighting the dataset's value as a challenging benchmark for the broader research community. Project page: https://mila-iqia.github.io/cableinspect-ad/.