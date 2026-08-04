---
title: "Auditing Private Prediction"
source: "https://proceedings.mlr.press/v235/chadha24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/chadha24a/chadha24a.pdf"
categories: ['privacy-preserving-federated-and-distributed-learning', 'statistical-learning-robustness-uncertainty-quantification']
tags: ['differential-privacy', 'auditing', 'private-prediction', 'inference-privacy']
venue: "ICML 2024"
tldr: "Develops techniques for auditing differential privacy guarantees at inference time rather than only during training."
---

# Auditing Private Prediction

**Source**: [https://proceedings.mlr.press/v235/chadha24a.html](https://proceedings.mlr.press/v235/chadha24a.html)

**TLDR**: Develops techniques for auditing differential privacy guarantees at inference time rather than only during training.

## Abstract

Differential privacy (DP) offers a theoretical upper bound on the potential privacy leakage of an algorithm, while empirical auditing establishes a practical lower bound. Auditing techniques exist for DP training algorithms. However machine learning can also be made private at inference. We propose the first framework for auditing private prediction where we instantiate adversaries with varying poisoning and query capabilities. This enables us to study the privacy leakage of four private prediction algorithms: PATE (Papernot et al., 2016), CaPC (Choquette-Choo et al., 2020), PromptPATE (Duan et al., 2023), and Private-kNN (Zhu et al., 2020). To conduct our audit, we introduce novel techniques to empirically evaluate privacy leakage in terms of Renyi DP. Our experiments show that (i) the privacy analysis of private prediction can be improved, (ii) algorithms which are easier to poison lead to much higher privacy leakage, and (iii) the privacy leakage is significantly lower for adversaries without query control than those with full control.