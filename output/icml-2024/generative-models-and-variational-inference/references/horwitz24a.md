---
title: "Recovering the Pre-Fine-Tuning Weights of Generative Models"
source: "https://proceedings.mlr.press/v235/horwitz24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/horwitz24a/horwitz24a.pdf"
categories: ['adversarial-robustness-and-model-security', 'generative-models-and-variational-inference']
tags: ['model-security', 'fine-tuning', 'generative-models', 'weight-recovery', 'safety']
venue: "ICML 2024"
tldr: "Demonstrates that pre-fine-tuning weights of generative models can be recovered from aligned model weights, posing safety risks to alignment-by-fine-tuning paradigms."
---

# Recovering the Pre-Fine-Tuning Weights of Generative Models

**Source**: [https://proceedings.mlr.press/v235/horwitz24a.html](https://proceedings.mlr.press/v235/horwitz24a.html)

**TLDR**: Demonstrates that pre-fine-tuning weights of generative models can be recovered from aligned model weights, posing safety risks to alignment-by-fine-tuning paradigms.

## Abstract

The dominant paradigm in generative modeling consists of two steps: i) pre-training on a large-scale but unsafe dataset, ii) aligning the pre-trained model with human values via fine-tuning. This practice is considered safe, as no current method can recover the unsafe, pre-fine-tuning model weights. In this paper, we demonstrate that this assumption is often false. Concretely, we present Spectral DeTuning, a method that can recover the weights of the pre-fine-tuning model using a few low-rank (LoRA) fine-tuned models. In contrast to previous attacks that attempt to recover pre-fine-tuning capabilities, our method aims to recover the exact pre-fine-tuning weights. Our approach exploits this new vulnerability against large-scale models such as a personalized Stable Diffusion and an aligned Mistral. The code is available at https://vision.huji.ac.il/spectral_detuning/.