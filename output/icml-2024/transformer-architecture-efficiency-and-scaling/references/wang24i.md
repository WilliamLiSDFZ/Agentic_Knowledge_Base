---
title: "Revisiting the Power of Prompt for Visual Tuning"
source: "https://proceedings.mlr.press/v235/wang24i.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/wang24i/wang24i.pdf"
categories: ['test-time-adaptation-methods-and-evaluation', 'transformer-architecture-efficiency-and-scaling']
tags: ['visual-prompt-tuning', 'parameter-efficient', 'self-supervised', 'pre-trained-models', 'downstream-tasks']
venue: "ICML 2024"
tldr: "This paper revisits visual prompt tuning by addressing initialization and length challenges to improve adaptation of self-supervised pre-trained models."
---

# Revisiting the Power of Prompt for Visual Tuning

**Source**: [https://proceedings.mlr.press/v235/wang24i.html](https://proceedings.mlr.press/v235/wang24i.html)

**TLDR**: This paper revisits visual prompt tuning by addressing initialization and length challenges to improve adaptation of self-supervised pre-trained models.

## Abstract

Visual prompt tuning (VPT) is a promising solution incorporating learnable prompt tokens to customize pre-trained models for downstream tasks. However, VPT and its variants often encounter challenges like prompt initialization, prompt length, and subpar performance in self-supervised pretraining, hindering successful contextual adaptation. This study commences by exploring the correlation evolvement between prompts and patch tokens during proficient training. Inspired by the observation that the prompt tokens tend to share high mutual information with patch tokens, we propose initializing prompts with downstream token prototypes. The strategic initialization, a stand-in for the previous initialization, substantially improves performance. To refine further, we optimize token construction with a streamlined pipeline that maintains excellent performance with almost no increase in computational expenses compared to VPT. Exhaustive experiments show our proposed approach outperforms existing methods by a remarkable margin. For instance, after MAE pre-training, our method improves accuracy by up to 10%$\sim$30% compared to VPT, and outperforms Full fine-tuning 19 out of 24 cases while using less than 0.4% of learnable parameters. Besides, the experimental results demonstrate the proposed SPT is robust to prompt lengths and scales well with model capacity and training data size. We finally provide an insightful exploration into the amount of target data facilitating the adaptation of pre-trained models to downstream tasks. The code is available at https://github.com/WangYZ1608/Self-Prompt-Tuning.