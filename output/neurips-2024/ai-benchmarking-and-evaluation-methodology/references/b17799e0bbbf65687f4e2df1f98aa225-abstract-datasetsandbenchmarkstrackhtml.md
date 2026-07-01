---
title: "Benchmarking the Attribution Quality of Vision Models"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/b17799e0bbbf65687f4e2df1f98aa225-Abstract-Datasets_and_Benchmarks_Track.html"
categories: ['ai-benchmarking-and-evaluation-methodology']
tags: ['attribution-maps', 'explainability', 'benchmarking']
venue: "NeurIPS 2024"
tldr: "A benchmark for evaluating the attribution quality of vision model explanation methods across multiple metrics."
---

# Benchmarking the Attribution Quality of Vision Models

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/b17799e0bbbf65687f4e2df1f98aa225-Abstract-Datasets_and_Benchmarks_Track.html](https://papers.nips.cc/paper_files/paper/2024/hash/b17799e0bbbf65687f4e2df1f98aa225-Abstract-Datasets_and_Benchmarks_Track.html)

**TLDR**: A benchmark for evaluating the attribution quality of vision model explanation methods across multiple metrics.

## Abstract

Attribution maps are one of the most established tools to explain the functioning of computer vision models. They assign importance scores to input features, indicating how relevant each feature is for the prediction of a deep neural network. While much research has gone into proposing new attribution methods, their proper evaluation remains a difficult challenge. In this work, we propose a novel evaluation protocol that overcomes two fundamental limitations of the widely used incremental-deletion protocol, i.e., the out-of-domain issue and lacking inter-model comparisons. This allows us to evaluate 23 attribution methods and how different design choices of popular vision backbones affect their attribution quality. We find that intrinsically explainable models outperform standard models and that raw attribution values exhibit a higher attribution quality than what is known from previous work. Further, we show consistent changes in the attribution quality when varying the network design, indicating that some standard design choices promote attribution quality.