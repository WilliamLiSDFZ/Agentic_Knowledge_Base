---
title: "ERQ: Error Reduction for Post-Training Quantization of Vision Transformers"
source: "https://proceedings.mlr.press/v235/zhong24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/zhong24a/zhong24a.pdf"
categories: ['transformer-architecture-efficiency-and-scaling']
tags: ['post-training-quantization', 'vision-transformers', 'weight-activation-interdependence', 'error-reduction']
venue: "ICML 2024"
tldr: "ERQ addresses quantization error in vision transformers by explicitly modeling and reducing the interdependence between quantized weights and activations."
---

# ERQ: Error Reduction for Post-Training Quantization of Vision Transformers

**Source**: [https://proceedings.mlr.press/v235/zhong24a.html](https://proceedings.mlr.press/v235/zhong24a.html)

**TLDR**: ERQ addresses quantization error in vision transformers by explicitly modeling and reducing the interdependence between quantized weights and activations.

## Abstract

Post-training quantization (PTQ) for vision transformers (ViTs) has garnered significant attention due to its efficiency in compressing models. However, existing methods typically overlook the intricate interdependence between quantized weight and activation, leading to considerable quantization error. In this paper, we propose ERQ, a two-step PTQ approach meticulously crafted to sequentially reduce the quantization error arising from activation and weight quantization. ERQ first introduces Activation quantization error reduction (Aqer) that strategically formulates the minimization of activation quantization error as a Ridge Regression problem, tackling it by updating weights with full-precision. Subsequently, ERQ introduces Weight quantization error reduction (Wqer) that adopts an iterative approach to mitigate the quantization error induced by weight quantization. In each iteration, an empirically derived, efficient proxy is employed to refine the rounding directions of quantized weights, coupled with a Ridge Regression solver to curtail weight quantization error. Experimental results attest to the effectiveness of our approach. Notably, ERQ surpasses the state-of-the-art GPTQ by 22.36% in accuracy for W3A4 ViT-S.