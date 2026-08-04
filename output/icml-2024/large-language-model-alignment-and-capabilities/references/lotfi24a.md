---
title: "Non-Vacuous Generalization Bounds for Large Language Models"
source: "https://proceedings.mlr.press/v235/lotfi24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/lotfi24a/lotfi24a.pdf"
categories: ['neural-network-learning-dynamics-theory', 'large-language-model-alignment-and-capabilities']
tags: ['generalization-bounds', 'large-language-models', 'PAC-Bayes', 'non-vacuous-bounds']
venue: "ICML 2024"
tldr: "Derives the first non-vacuous generalization bounds for pretrained large language models using compression-based techniques."
---

# Non-Vacuous Generalization Bounds for Large Language Models

**Source**: [https://proceedings.mlr.press/v235/lotfi24a.html](https://proceedings.mlr.press/v235/lotfi24a.html)

**TLDR**: Derives the first non-vacuous generalization bounds for pretrained large language models using compression-based techniques.

## Abstract

Modern language models can contain billions of parameters, raising the question of whether they can generalize beyond the training data or simply parrot their training corpora. We provide the first non-vacuous generalization bounds for pretrained large language models (LLMs), indicating that language models are capable of discovering regularities that generalize to unseen data. In particular, we derive a compression bound that is valid for the unbounded log-likelihood loss using prediction smoothing, and we extend the bound to handle subsampling, making bound computation 900 times faster on massive datasets. To achieve the extreme level of compression required for non-vacuous bounds, we devise SubLoRA, a simple low-dimensional nonlinear parameterization that leads to non-vacuous generalization bounds for very large models with up to 849 million parameters. Finally, we use our bounds to understand LLM generalization and find that larger models have better generalization bounds and are more compressible than smaller models.