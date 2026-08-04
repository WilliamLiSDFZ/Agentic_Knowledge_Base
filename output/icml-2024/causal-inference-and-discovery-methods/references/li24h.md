---
title: "Learning Causal Domain-Invariant Temporal Dynamics for Few-Shot Action Recognition"
source: "https://proceedings.mlr.press/v235/li24h.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/li24h/li24h.pdf"
categories: ['causal-inference-and-discovery-methods', 'causal-ml-for-clinical-decision-making']
tags: ['few-shot-action-recognition', 'causal-inference', 'domain-invariant', 'temporal-dynamics', 'distribution-shift']
venue: "ICML 2024"
tldr: "Proposes CDTD to learn causal domain-invariant temporal dynamics for improved few-shot action recognition under distribution shift."
---

# Learning Causal Domain-Invariant Temporal Dynamics for Few-Shot Action Recognition

**Source**: [https://proceedings.mlr.press/v235/li24h.html](https://proceedings.mlr.press/v235/li24h.html)

**TLDR**: Proposes CDTD to learn causal domain-invariant temporal dynamics for improved few-shot action recognition under distribution shift.

## Abstract

Few-shot action recognition aims at quickly adapting a pre-trained model to the novel data with a distribution shift using only a limited number of samples. Key challenges include how to identify and leverage the transferable knowledge learned by the pre-trained model. We therefore propose CDTD, or Causal Domain-Invariant Temporal Dynamics for knowledge transfer. To identify the temporally invariant and variant representations, we employ the causal representation learning methods for unsupervised pertaining, and then tune the classifier with supervisions in next stage. Specifically, we assume the domain information can be well estimated and the pre-trained temporal dynamic generation and transition models can be well transferred. During adaptation, we fix the transferable temporal dynamics and update the image encoder and domain estimator. The efficacy of our approach is revealed by the superior accuracy of CDTD over leading alternatives across standard few-shot action recognition datasets.