---
title: "Understanding the Training Speedup from Sampling with Approximate Losses"
source: "https://proceedings.mlr.press/v235/das24b.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/das24b/das24b.pdf"
categories: ['data-selection-and-active-learning-methods', 'optimization-algorithms-convergence-theory']
tags: ['data-selection', 'importance-sampling', 'approximate-losses', 'training-efficiency', 'curriculum-learning']
venue: "ICML 2024"
tldr: "Studies how selecting samples by approximate losses speeds up training and provides theoretical analysis of the resulting training speedup."
---

# Understanding the Training Speedup from Sampling with Approximate Losses

**Source**: [https://proceedings.mlr.press/v235/das24b.html](https://proceedings.mlr.press/v235/das24b.html)

**TLDR**: Studies how selecting samples by approximate losses speeds up training and provides theoretical analysis of the resulting training speedup.

## Abstract

It is well known that selecting samples with large losses/gradients can significantly reduce the number of training steps. However, the selection overhead is often too high to yield any meaningful gains in terms of overall training time. In this work, we focus on the greedy approach of selecting samples with large approximate losses instead of exact losses in order to reduce the selection overhead. For smooth convex losses, we show that such a greedy strategy can converge to a constant factor of the minimum value of the average loss in fewer iterations than the standard approach of random selection. We also theoretically quantify the effect of the approximation level. We then develop SIFT which uses early exiting to obtain approximate losses with an intermediate layer’s representations for sample selection. We evaluate SIFT on the task of training a 110M parameter 12 layer BERT base model, and show significant gains (in terms of training hours and number of backpropagation steps) without any optimized implementation over vanilla training. For e.g., to reach 64% validation accuracy, SIFT with exit at the first layer takes $\sim$ 43 hours compared to $\sim$ 57 hours of vanilla training.