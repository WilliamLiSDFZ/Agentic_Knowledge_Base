---
title: "AquaLoRA: Toward White-box Protection for Customized Stable Diffusion Models via Watermark LoRA"
source: "https://proceedings.mlr.press/v235/feng24k.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/feng24k/feng24k.pdf"
categories: ['generative-models-and-variational-inference']
tags: ['stable-diffusion', 'watermarking', 'LoRA']
venue: "ICML 2024"
tldr: "Proposes AquaLoRA, a white-box watermarking method for protecting customized Stable Diffusion models via watermark-embedded LoRA modules."
---

# AquaLoRA: Toward White-box Protection for Customized Stable Diffusion Models via Watermark LoRA

**Source**: [https://proceedings.mlr.press/v235/feng24k.html](https://proceedings.mlr.press/v235/feng24k.html)

**TLDR**: Proposes AquaLoRA, a white-box watermarking method for protecting customized Stable Diffusion models via watermark-embedded LoRA modules.

## Abstract

Diffusion models have achieved remarkable success in generating high-quality images. Recently, the open-source models represented by Stable Diffusion (SD) are thriving and are accessible for customization, giving rise to a vibrant community of creators and enthusiasts. However, the widespread availability of customized SD models has led to copyright concerns, like unauthorized model distribution and unconsented commercial use. To address it, recent works aim to let SD models output watermarked content for post-hoc forensics. Unfortunately, none of them can achieve the challenging white-box protection, wherein the malicious user can easily remove or replace the watermarking module to fail the subsequent verification. For this, we propose AquaLoRA as the first implementation under this scenario. Briefly, we merge watermark information into the U-Net of Stable Diffusion Models via a watermark LowRank Adaptation (LoRA) module in a two-stage manner. For watermark LoRA module, we devise a scaling matrix to achieve flexible message updates without retraining. To guarantee fidelity, we design Prior Preserving Fine-Tuning (PPFT) to ensure watermark learning with minimal impacts on model distribution, validated by proofs. Finally, we conduct extensive experiments and ablation studies to verify our design. Our code is available at github.com/Georgefwt/AquaLoRA.