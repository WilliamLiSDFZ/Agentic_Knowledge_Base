---
title: "Asymmetry in Low-Rank Adapters of Foundation Models"
source: "https://proceedings.mlr.press/v235/zhu24c.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/zhu24c/zhu24c.pdf"
categories: ['neural-network-learning-dynamics-theory', 'optimization-algorithms-convergence-theory']
tags: ['lora', 'fine-tuning', 'asymmetry', 'low-rank-adaptation', 'foundation-models']
venue: "ICML 2024"
tldr: "This paper investigates the asymmetric roles of LoRA matrices during fine-tuning of foundation models and characterizes how this asymmetry affects optimization and performance."
---

# Asymmetry in Low-Rank Adapters of Foundation Models

**Source**: [https://proceedings.mlr.press/v235/zhu24c.html](https://proceedings.mlr.press/v235/zhu24c.html)

**TLDR**: This paper investigates the asymmetric roles of LoRA matrices during fine-tuning of foundation models and characterizes how this asymmetry affects optimization and performance.

## Abstract

Parameter-efficient fine-tuning optimizes large, pre-trained foundation models by updating a subset of parameters; in this class, Low-Rank Adaptation (LoRA) is particularly effective. Inspired by an effort to investigate the different roles of LoRA matrices during fine-tuning, this paper characterizes and leverages unexpected asymmetry in the importance of low-rank adapter matrices. Specifically, when updating the parameter matrices of a neural network by adding a product $BA$, we observe that the $B$ and $A$ matrices have distinct functions: $A$ extracts features from the input, while $B$ uses these features to create the desired output. Based on this observation, we demonstrate that fine-tuning $B$ is inherently more effective than fine-tuning $A$, and that a random untrained $A$ should perform nearly as well as a fine-tuned one. Using an information-theoretic lens, we also bound the generalization of low-rank adapters, showing that the parameter savings of exclusively training $B$ improves the bound. We support our conclusions with experiments on RoBERTa, BART-Large, LLaMA-2, and ViTs. The code and data is available at https://github.com/Jiacheng-Zhu-AIML/AsymmetryLoRA