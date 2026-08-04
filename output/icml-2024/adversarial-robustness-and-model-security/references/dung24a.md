---
title: "Sharpness-Aware Data Generation for Zero-shot Quantization"
source: "https://proceedings.mlr.press/v235/dung24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/dung24a/dung24a.pdf"
categories: ['knowledge-distillation-methods-and-applications', 'adversarial-robustness-and-model-security']
tags: ['zero-shot-quantization', 'synthetic-data', 'sharpness-aware', 'model-compression']
venue: "ICML 2024"
tldr: "A sharpness-aware data generation approach for zero-shot quantization that produces synthetic training data yielding more robust quantized models."
---

# Sharpness-Aware Data Generation for Zero-shot Quantization

**Source**: [https://proceedings.mlr.press/v235/dung24a.html](https://proceedings.mlr.press/v235/dung24a.html)

**TLDR**: A sharpness-aware data generation approach for zero-shot quantization that produces synthetic training data yielding more robust quantized models.

## Abstract

Zero-shot quantization aims to learn a quantized model from a pre-trained full-precision model with no access to original real training data. The common idea in zero-shot quantization approaches is to generate synthetic data for quantizing the full-precision model. While it is well-known that deep neural networks with low sharpness have better generalization ability, none of the previous zero-shot quantization works considers the sharpness of the quantized model as a criterion for generating training data. This paper introduces a novel methodology that takes into account quantized model sharpness in synthetic data generation to enhance generalization. Specifically, we first demonstrate that sharpness minimization can be attained by maximizing gradient matching between the reconstruction loss gradients computed on synthetic and real validation data, under certain assumptions. We then circumvent the problem of the gradient matching without real validation set by approximating it with the gradient matching between each generated sample and its neighbors. Experimental evaluations on CIFAR-100 and ImageNet datasets demonstrate the superiority of the proposed method over the state-of-the-art techniques in low-bit quantization settings.