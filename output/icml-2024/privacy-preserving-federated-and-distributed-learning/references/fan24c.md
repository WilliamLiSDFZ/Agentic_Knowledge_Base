---
title: "Locally Estimated Global Perturbations are Better than Local Perturbations for Federated Sharpness-aware Minimization"
source: "https://proceedings.mlr.press/v235/fan24c.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/fan24c/fan24c.pdf"
categories: ['privacy-preserving-federated-and-distributed-learning']
tags: ['federated-learning', 'sharpness-aware-minimization', 'data-heterogeneity']
venue: "ICML 2024"
tldr: "Proposes a federated SAM approach using locally estimated global perturbations to improve generalization under data heterogeneity."
---

# Locally Estimated Global Perturbations are Better than Local Perturbations for Federated Sharpness-aware Minimization

**Source**: [https://proceedings.mlr.press/v235/fan24c.html](https://proceedings.mlr.press/v235/fan24c.html)

**TLDR**: Proposes a federated SAM approach using locally estimated global perturbations to improve generalization under data heterogeneity.

## Abstract

In federated learning (FL), the multi-step update and data heterogeneity among clients often lead to a loss landscape with sharper minima, degenerating the performance of the resulted global model. Prevalent federated approaches incorporate sharpness-aware minimization (SAM) into local training to mitigate this problem. However, the local loss landscapes may not accurately reflect the flatness of global loss landscape in heterogeneous environments; as a result, minimizing local sharpness and calculating perturbations on client data might not align the efficacy of SAM in FL with centralized training. To overcome this challenge, we propose FedLESAM, a novel algorithm that locally estimates the direction of global perturbation on client side as the difference between global models received in the previous active and current rounds. Besides the improved quality, FedLESAM also speed up federated SAM-based approaches since it only performs once backpropagation in each iteration. Theoretically, we prove a slightly tighter bound than its original FedSAM by ensuring consistent perturbation. Empirically, we conduct comprehensive experiments on four federated benchmark datasets under three partition strategies to demonstrate the superior performance and efficiency of FedLESAM.