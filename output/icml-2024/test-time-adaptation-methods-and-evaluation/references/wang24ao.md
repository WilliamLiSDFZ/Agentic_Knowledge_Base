---
title: "Connecting the Dots: Collaborative Fine-tuning for Black-Box Vision-Language Models"
source: "https://proceedings.mlr.press/v235/wang24ao.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/wang24ao/wang24ao.pdf"
categories: ['knowledge-distillation-methods-and-applications', 'test-time-adaptation-methods-and-evaluation']
tags: ['vision-language-models', 'black-box-fine-tuning', 'collaborative-learning', 'adaptation']
venue: "ICML 2024"
tldr: "A collaborative fine-tuning framework is proposed for adapting black-box vision-language models without access to model parameters."
---

# Connecting the Dots: Collaborative Fine-tuning for Black-Box Vision-Language Models

**Source**: [https://proceedings.mlr.press/v235/wang24ao.html](https://proceedings.mlr.press/v235/wang24ao.html)

**TLDR**: A collaborative fine-tuning framework is proposed for adapting black-box vision-language models without access to model parameters.

## Abstract

With the emergence of pretrained vision-language models (VLMs), considerable efforts have been devoted to fine-tuning them for downstream tasks. Despite the progress made in designing efficient fine-tuning methods, such methods require access to the model’s parameters, which can be challenging as model owners often opt to provide their models as a black box to safeguard model ownership. This paper proposes a Collaborative Fine-Tuning (CraFT) approach for fine-tuning black-box VLMs to downstream tasks, where one only has access to the input prompts and the output predictions of the model. CraFT comprises two modules, a prompt generation module for learning text prompts and a prediction refinement module for enhancing output predictions in residual style. Additionally, we introduce an auxiliary prediction-consistent loss to promote consistent optimization across these modules. These modules are optimized by a novel collaborative training algorithm. Extensive experiments on few-shot classification over 15 datasets demonstrate the superiority of CraFT. The results show that CraFT achieves a decent gain of about 12% with 16-shot datasets and only 8,000 queries. Moreover, CraFT trains faster and uses only about 1/80 of the memory footprint for deployment, while sacrificing only 1.62% compared to the white-box method. Our code is publicly available at https://github.com/mrflogs/CraFT.