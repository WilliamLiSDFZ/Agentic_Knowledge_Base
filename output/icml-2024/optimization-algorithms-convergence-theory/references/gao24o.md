---
title: "Parameter-Efficient Fine-Tuning with Discrete Fourier Transform"
source: "https://proceedings.mlr.press/v235/gao24o.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/gao24o/gao24o.pdf"
categories: ['transformer-architecture-efficiency-and-scaling', 'optimization-algorithms-convergence-theory']
tags: ['parameter-efficient-fine-tuning', 'LoRA', 'Fourier-transform', 'foundation-models']
venue: "ICML 2024"
tldr: "FourierFT uses discrete Fourier transforms to achieve parameter-efficient fine-tuning of foundation models with fewer stored parameters than LoRA."
---

# Parameter-Efficient Fine-Tuning with Discrete Fourier Transform

**Source**: [https://proceedings.mlr.press/v235/gao24o.html](https://proceedings.mlr.press/v235/gao24o.html)

**TLDR**: FourierFT uses discrete Fourier transforms to achieve parameter-efficient fine-tuning of foundation models with fewer stored parameters than LoRA.

## Abstract

Low-rank adaptation (LoRA) has recently gained much interest in fine-tuning foundation models. It effectively reduces the number of trainable parameters by incorporating low-rank matrices $A$ and $B$ to represent the weight change, i.e., $\Delta W=BA$. Despite LoRA’s progress, it faces storage challenges when handling extensive customization adaptations or larger base models. In this work, we aim to further compress trainable parameters by enjoying the powerful expressiveness of the Fourier transform. Specifically, we introduce FourierFT, which treats $\Delta W$ as a matrix in the spatial domain and learns only a small fraction of its spectral coefficients. With the trained spectral coefficients, we implement the inverse discrete Fourier transform to recover $\Delta W$. Empirically, our FourierFT method shows comparable or better performance with fewer parameters than LoRA on various tasks, including natural language understanding, natural language generation, instruction tuning, and image classification. For example, when performing instruction tuning on the LLaMA2-7B model, FourierFT surpasses LoRA with only 0.064M trainable parameters, compared to LoRA’s 33.5M. Our code is released at this link.