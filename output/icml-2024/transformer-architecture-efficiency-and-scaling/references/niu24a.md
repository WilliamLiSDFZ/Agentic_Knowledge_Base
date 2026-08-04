---
title: "Test-Time Model Adaptation with Only Forward Passes"
source: "https://proceedings.mlr.press/v235/niu24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/niu24a/niu24a.pdf"
categories: ['test-time-adaptation-methods-and-evaluation', 'transformer-architecture-efficiency-and-scaling']
tags: ['test-time-adaptation', 'forward-pass-only', 'distribution-shift']
venue: "ICML 2024"
tldr: "Proposes a test-time adaptation method that operates with only forward passes, enabling deployment on resource-limited non-modifiable hardware."
---

# Test-Time Model Adaptation with Only Forward Passes

**Source**: [https://proceedings.mlr.press/v235/niu24a.html](https://proceedings.mlr.press/v235/niu24a.html)

**TLDR**: Proposes a test-time adaptation method that operates with only forward passes, enabling deployment on resource-limited non-modifiable hardware.

## Abstract

Test-time adaptation has proven effective in adapting a given trained model to unseen test samples with potential distribution shifts. However, in real-world scenarios, models are usually deployed on resource-limited devices, e.g., FPGAs, and are often quantized and hard-coded with non-modifiable parameters for acceleration. In light of this, existing methods are often infeasible since they heavily depend on computation-intensive backpropagation for model updating that may be not supported. To address this, we propose a test-time Forward-Optimization Adaptation (FOA) method. In FOA, we seek to solely learn a newly added prompt (as model’s input) via a derivative-free covariance matrix adaptation evolution strategy. To make this strategy work stably under our online unsupervised setting, we devise a novel fitness function by measuring test-training statistic discrepancy and model prediction entropy. Moreover, we design an activation shifting scheme that directly tunes the model activations for shifted test samples, making them align with the source training domain, thereby further enhancing adaptation performance. Without using any backpropagation and altering model weights, FOA runs on quantized 8-bit ViT outperforms gradient-based TENT on full-precision 32-bit ViT, while achieving an up to 24-fold memory reduction on ImageNet-C. The source code is available at: https://github.com/mr-eggplant/FOA.