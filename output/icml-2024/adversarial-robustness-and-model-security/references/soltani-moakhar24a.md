---
title: "SPADE: Sparsity-Guided Debugging for Deep Neural Networks"
source: "https://proceedings.mlr.press/v235/soltani-moakhar24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/soltani-moakhar24a/soltani-moakhar24a.pdf"
categories: ['ai-explainability-uncertainty-human-decision-making', 'adversarial-robustness-and-model-security']
tags: ['sparsity', 'debugging', 'interpretability', 'deep-neural-networks']
venue: "ICML 2024"
tldr: "SPADE uses sparsity guidance to debug deep neural networks without requiring pre-training with sparsity constraints or altering general network behavior."
---

# SPADE: Sparsity-Guided Debugging for Deep Neural Networks

**Source**: [https://proceedings.mlr.press/v235/soltani-moakhar24a.html](https://proceedings.mlr.press/v235/soltani-moakhar24a.html)

**TLDR**: SPADE uses sparsity guidance to debug deep neural networks without requiring pre-training with sparsity constraints or altering general network behavior.

## Abstract

It is known that sparsity can improve interpretability for deep neural networks. However, existing methods in the area either require networks that are pre-trained with sparsity constraints, or impose sparsity after the fact, altering the network’s general behavior. In this paper, we demonstrate, for the first time, that sparsity can instead be incorporated into the interpretation process itself, as a sample-specific preprocessing step. Unlike previous work, this approach, which we call SPADE, does not place constraints on the trained model and does not affect its behavior during inference on the sample. Given a trained model and a target sample, SPADE uses sample-targeted pruning to provide a "trace" of the network’s execution on the sample, reducing the network to the most important connections prior to computing an interpretation. We demonstrate that preprocessing with SPADE significantly increases the accuracy of image saliency maps across several interpretability methods. Additionally, SPADE improves the usefulness of neuron visualizations, aiding humans in reasoning about network behavior. Our code is available at https://github.com/IST-DASLab/SPADE.