---
title: "Deciphering RNA Secondary Structure Prediction: A Probabilistic K-Rook Matching Perspective"
source: "https://proceedings.mlr.press/v235/tan24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/tan24a/tan24a.pdf"
categories: ['probabilistic-generating-circuits-research']
tags: ['RNA-structure', 'probabilistic-matching', 'deep-learning']
venue: "ICML 2024"
tldr: "RNA secondary structure prediction is reframed as a probabilistic K-Rook matching problem, improving generalization and reducing complexity."
---

# Deciphering RNA Secondary Structure Prediction: A Probabilistic K-Rook Matching Perspective

**Source**: [https://proceedings.mlr.press/v235/tan24a.html](https://proceedings.mlr.press/v235/tan24a.html)

**TLDR**: RNA secondary structure prediction is reframed as a probabilistic K-Rook matching problem, improving generalization and reducing complexity.

## Abstract

The secondary structure of ribonucleic acid (RNA) is more stable and accessible in the cell than its tertiary structure, making it essential for functional prediction. Although deep learning has shown promising results in this field, current methods suffer from poor generalization and high complexity. In this work, we reformulate the RNA secondary structure prediction as a K-Rook problem, thereby simplifying the prediction process into probabilistic matching within a finite solution space. Building on this innovative perspective, we introduce RFold, a simple yet effective method that learns to predict the most matching K-Rook solution from the given sequence. RFold employs a bi-dimensional optimization strategy that decomposes the probabilistic matching problem into row-wise and column-wise components to reduce the matching complexity, simplifying the solving process while guaranteeing the validity of the output. Extensive experiments demonstrate that RFold achieves competitive performance and about eight times faster inference efficiency than the state-of-the-art approaches. The code is available at https://github.com/A4Bio/RFold.