---
title: "Self-cognitive Denoising in the Presence of Multiple Noisy Label Sources"
source: "https://proceedings.mlr.press/v235/sun24o.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/sun24o/sun24o.pdf"
categories: ['learning-with-imperfect-data-and-bias']
tags: ['noisy-labels', 'denoising', 'multiple-sources']
venue: "ICML 2024"
tldr: "A self-cognitive denoising framework is proposed for learning from multiple noisy label sources without requiring clean supervision."
---

# Self-cognitive Denoising in the Presence of Multiple Noisy Label Sources

**Source**: [https://proceedings.mlr.press/v235/sun24o.html](https://proceedings.mlr.press/v235/sun24o.html)

**TLDR**: A self-cognitive denoising framework is proposed for learning from multiple noisy label sources without requiring clean supervision.

## Abstract

The strong performance of neural networks typically hinges on the availability of extensive labeled data, yet acquiring ground-truth labels is often challenging. Instead, noisy supervisions from multiple sources, e.g., by multiple well-designed rules, are more convenient to collect. In this paper, we focus on the realistic problem of learning from multiple noisy label sources, and argue that prior studies have overlooked the crucial self-cognition ability of neural networks, i.e., the inherent capability of autonomously distinguishing noise during training. We theoretically analyze this ability of neural networks when meeting multiple noisy label sources, which reveals that neural networks possess the capability to recognize both instance-wise noise within each single noisy label source and annotator-wise quality among multiple noisy label sources. Inspired by the theoretical analyses, we introduce an approach named Self-cognitive Denoising for Multiple noisy label sources (SDM), which exploits the self-cognition ability of neural networks to denoise during training. Furthermore, we build a selective distillation module following the theoretical insights to optimize computational efficiency. The experiments on various datasets demonstrate the superiority of our method.