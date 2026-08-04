---
title: "Feature Reuse and Scaling: Understanding Transfer Learning with Protein Language Models"
source: "https://proceedings.mlr.press/v235/li24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/li24a/li24a.pdf"
categories: ['neural-network-learning-dynamics-theory', 'learning-with-imperfect-data-and-bias']
tags: ['protein-language-models', 'transfer-learning', 'feature-reuse', 'scaling', 'representation-learning']
venue: "ICML 2024"
tldr: "Investigates how feature reuse and model scaling govern transfer learning effectiveness of pretrained protein language models on downstream tasks."
---

# Feature Reuse and Scaling: Understanding Transfer Learning with Protein Language Models

**Source**: [https://proceedings.mlr.press/v235/li24a.html](https://proceedings.mlr.press/v235/li24a.html)

**TLDR**: Investigates how feature reuse and model scaling govern transfer learning effectiveness of pretrained protein language models on downstream tasks.

## Abstract

Large pretrained protein language models (PLMs) have improved protein property and structure prediction from sequences via transfer learning, in which weights and representations from PLMs are repurposed for downstream tasks. Although PLMs have shown great promise, currently there is little understanding of how the features learned by pretraining relate to and are useful for downstream tasks. We perform a systematic analysis of transfer learning using PLMs, conducting 370 experiments across a comprehensive suite of factors including different downstream tasks, architectures, model sizes, model depths, and pretraining time. We observe that while almost all downstream tasks do benefit from pretrained models compared to naive sequence representations, for the majority of tasks performance does not scale with pretraining, and instead relies on low-level features learned early in pretraining. Our results point to a mismatch between current PLM pretraining paradigms and most applications of these models, indicating a need for better pretraining methods.