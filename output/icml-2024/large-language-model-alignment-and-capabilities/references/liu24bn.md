---
title: "DoRA: Weight-Decomposed Low-Rank Adaptation"
source: "https://proceedings.mlr.press/v235/liu24bn.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/liu24bn/liu24bn.pdf"
categories: ['transformer-architecture-efficiency-and-scaling', 'large-language-model-alignment-and-capabilities']
tags: ['parameter-efficient-fine-tuning', 'LoRA', 'weight-decomposition', 'low-rank-adaptation', 'fine-tuning']
venue: "ICML 2024"
tldr: "DoRA decomposes pretrained weights into magnitude and direction for low-rank adaptation, closing the accuracy gap between LoRA-based methods and full fine-tuning."
---

# DoRA: Weight-Decomposed Low-Rank Adaptation

**Source**: [https://proceedings.mlr.press/v235/liu24bn.html](https://proceedings.mlr.press/v235/liu24bn.html)

**TLDR**: DoRA decomposes pretrained weights into magnitude and direction for low-rank adaptation, closing the accuracy gap between LoRA-based methods and full fine-tuning.

## Abstract

Among the widely used parameter-efficient fine-tuning (PEFT) methods, LoRA and its variants have gained considerable popularity because of avoiding additional inference costs. However, there still often exists an accuracy gap between these methods and full fine-tuning (FT). In this work, we first introduce a novel weight decomposition analysis to investigate the inherent differences between FT and LoRA. Aiming to resemble the learning capacity of FT from the findings, we propose Weight-Decomposed Low-Rank Adaptation (DoRA). DoRA decomposes the pre-trained weight into two components, magnitude and direction, for fine-tuning, specifically employing LoRA for directional updates to efficiently minimize the number of trainable parameters. By employing DoRA, we enhance both the learning capacity and training stability of LoRA while avoiding any additional inference overhead. DoRA consistently outperforms LoRA on fine-tuning LLaMA, LLaVA, and VL-BART on various downstream tasks, such as commonsense reasoning, visual instruction tuning, and image/video-text understanding. The code is available at https://github.com/NVlabs/DoRA.