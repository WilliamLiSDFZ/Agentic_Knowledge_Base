---
title: "Decoding-time Realignment of Language Models"
source: "https://proceedings.mlr.press/v235/liu24r.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/liu24r/liu24r.pdf"
categories: ['large-language-model-alignment-and-capabilities']
tags: ['language-model-alignment', 'RLHF', 'decoding-time']
venue: "ICML 2024"
tldr: "A decoding-time realignment method for language models is introduced to adjust outputs to human preferences without retraining."
---

# Decoding-time Realignment of Language Models

**Source**: [https://proceedings.mlr.press/v235/liu24r.html](https://proceedings.mlr.press/v235/liu24r.html)

**TLDR**: A decoding-time realignment method for language models is introduced to adjust outputs to human preferences without retraining.

## Abstract

Aligning language models with human preferences is crucial for reducing errors and biases in these models. Alignment techniques, such as reinforcement learning from human feedback (RLHF), are typically cast as optimizing a tradeoff between human preference rewards and a proximity regularization term that encourages staying close to the unaligned model. Selecting an appropriate level of regularization is critical: insufficient regularization can lead to reduced model capabilities due to reward hacking, whereas excessive regularization hinders alignment. Traditional methods for finding the optimal regularization level require retraining multiple models with varying regularization strengths. This process, however, is resource-intensive, especially for large models. To address this challenge, we propose decoding-time realignment (DeRa), a simple method to explore and evaluate different regularization strengths in aligned models without retraining. DeRa enables control over the degree of alignment, allowing users to smoothly transition between unaligned and aligned models. It also enhances the efficiency of hyperparameter tuning by enabling the identification of effective regularization strengths using a validation dataset.