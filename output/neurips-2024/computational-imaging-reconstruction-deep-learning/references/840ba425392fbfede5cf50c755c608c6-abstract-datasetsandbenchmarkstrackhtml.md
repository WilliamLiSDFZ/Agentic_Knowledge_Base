---
title: "Arctique: An artificial histopathological dataset unifying realism and controllability for uncertainty quantification"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/840ba425392fbfede5cf50c755c608c6-Abstract-Datasets_and_Benchmarks_Track.html"
categories: ['ai-benchmarking-and-evaluation-methodology', 'computational-imaging-reconstruction-deep-learning']
tags: ['uncertainty-quantification', 'histopathology', 'synthetic-benchmarks']
venue: "NeurIPS 2024"
tldr: "Arctique is an artificial histopathological dataset designed to benchmark uncertainty quantification methods with controllable and realistic properties."
---

# Arctique: An artificial histopathological dataset unifying realism and controllability for uncertainty quantification

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/840ba425392fbfede5cf50c755c608c6-Abstract-Datasets_and_Benchmarks_Track.html](https://papers.nips.cc/paper_files/paper/2024/hash/840ba425392fbfede5cf50c755c608c6-Abstract-Datasets_and_Benchmarks_Track.html)

**TLDR**: Arctique is an artificial histopathological dataset designed to benchmark uncertainty quantification methods with controllable and realistic properties.

## Abstract

Uncertainty Quantification (UQ) is crucial for reliable image segmentation. Yet, while the field sees continual development of novel methods, a lack of agreed-upon benchmarks limits their systematic comparison and evaluation: Current UQ methods are typically tested either on overly simplistic toy datasets or on complex real-world datasets that do not allow to discern true uncertainty. To unify both controllability and complexity, we introduce Arctique, a procedurally generated dataset modeled after histopathological colon images. We chose histopathological images for two reasons: 1) their complexity in terms of intricate object structures and highly variable appearance, which yields challenging segmentation problems, and 2) their broad prevalence for medical diagnosis and respective relevance of high-quality UQ. To generate Arctique, we established a Blender-based framework for 3D scene creation with intrinsic noise manipulation. Arctique contains up to 50,000 rendered images with precise masks as well as noisy label simulations. We show that by independently controlling the uncertainty in both images and labels, we can effectively study the performance of several commonly used UQ methods. Hence, Arctique serves as a critical resource for benchmarking and advancing UQ techniques and other methodologies in complex, multi-object environments, bridging the gap between realism and controllability. All code is publicly available, allowing re-creation and controlled manipulations of our shipped images as well as creation and rendering of new scenes.