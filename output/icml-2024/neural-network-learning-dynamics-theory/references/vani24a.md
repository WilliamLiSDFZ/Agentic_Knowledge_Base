---
title: "Forget Sharpness: Perturbed Forgetting of Model Biases Within SAM Dynamics"
source: "https://proceedings.mlr.press/v235/vani24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/vani24a/vani24a.pdf"
categories: ['neural-network-learning-dynamics-theory', 'learning-with-imperfect-data-and-bias']
tags: ['sharpness-aware-minimization', 'model-bias', 'generalization']
venue: "ICML 2024"
tldr: "Reinterprets SAM's generalization benefit as arising from perturbed forgetting of model biases rather than sharpness minimization."
---

# Forget Sharpness: Perturbed Forgetting of Model Biases Within SAM Dynamics

**Source**: [https://proceedings.mlr.press/v235/vani24a.html](https://proceedings.mlr.press/v235/vani24a.html)

**TLDR**: Reinterprets SAM's generalization benefit as arising from perturbed forgetting of model biases rather than sharpness minimization.

## Abstract

Despite attaining high empirical generalization, the sharpness of models trained with sharpness-aware minimization (SAM) do not always correlate with generalization error. Instead of viewing SAM as minimizing sharpness to improve generalization, our paper considers a new perspective based on SAM’s training dynamics. We propose that perturbations in SAM perform perturbed forgetting, where they discard undesirable model biases to exhibit learning signals that generalize better. We relate our notion of forgetting to the information bottleneck principle, use it to explain observations like the better generalization of smaller perturbation batches, and show that perturbed forgetting can exhibit a stronger correlation with generalization than flatness. While standard SAM targets model biases exposed by the steepest ascent directions, we propose a new perturbation that targets biases exposed through the model’s outputs. Our output bias forgetting perturbations outperform standard SAM, GSAM, and ASAM on ImageNet, robustness benchmarks, and transfer to CIFAR-10,100, while sometimes converging to sharper regions. Our results suggest that the benefits of SAM can be explained by alternative mechanistic principles that do not require flatness of the loss surface.