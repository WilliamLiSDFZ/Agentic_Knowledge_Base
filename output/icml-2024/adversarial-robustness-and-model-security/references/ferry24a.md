---
title: "Trained Random Forests Completely Reveal your Dataset"
source: "https://proceedings.mlr.press/v235/ferry24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/ferry24a/ferry24a.pdf"
categories: ['adversarial-robustness-and-model-security', 'privacy-preserving-federated-and-distributed-learning']
tags: ['reconstruction-attack', 'random-forest', 'privacy']
venue: "ICML 2024"
tldr: "An optimization-based attack can nearly completely reconstruct training datasets from trained random forest models using only information available in standard libraries."
---

# Trained Random Forests Completely Reveal your Dataset

**Source**: [https://proceedings.mlr.press/v235/ferry24a.html](https://proceedings.mlr.press/v235/ferry24a.html)

**TLDR**: An optimization-based attack can nearly completely reconstruct training datasets from trained random forest models using only information available in standard libraries.

## Abstract

We introduce an optimization-based reconstruction attack capable of completely or near-completely reconstructing a dataset utilized for training a random forest. Notably, our approach relies solely on information readily available in commonly used libraries such as scikit-learn. To achieve this, we formulate the reconstruction problem as a combinatorial problem under a maximum likelihood objective. We demonstrate that this problem is NP-hard, though solvable at scale using constraint programming - an approach rooted in constraint propagation and solution-domain reduction. Through an extensive computational investigation, we demonstrate that random forests trained without bootstrap aggregation but with feature randomization are susceptible to a complete reconstruction. This holds true even with a small number of trees. Even with bootstrap aggregation, the majority of the data can also be reconstructed. These findings underscore a critical vulnerability inherent in widely adopted ensemble methods, warranting attention and mitigation. Although the potential for such reconstruction attacks has been discussed in privacy research, our study provides clear empirical evidence of their practicability.