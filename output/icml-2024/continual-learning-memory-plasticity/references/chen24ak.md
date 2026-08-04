---
title: "Unleashing the Power of Meta-tuning for Few-shot Generalization Through Sparse Interpolated Experts"
source: "https://proceedings.mlr.press/v235/chen24ak.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/chen24ak/chen24ak.pdf"
categories: ['test-time-adaptation-methods-and-evaluation', 'continual-learning-memory-plasticity']
tags: ['meta-tuning', 'sparse-mixture-of-experts', 'few-shot-generalization', 'parameter-efficient-fine-tuning']
venue: "ICML 2024"
tldr: "Combines meta-learning with sparse interpolated experts for parameter-efficient fine-tuning to improve few-shot generalization of foundation models."
---

# Unleashing the Power of Meta-tuning for Few-shot Generalization Through Sparse Interpolated Experts

**Source**: [https://proceedings.mlr.press/v235/chen24ak.html](https://proceedings.mlr.press/v235/chen24ak.html)

**TLDR**: Combines meta-learning with sparse interpolated experts for parameter-efficient fine-tuning to improve few-shot generalization of foundation models.

## Abstract

Recent successes suggest that parameter-efficient fine-tuning of foundation models is becoming the state-of-the-art method for transfer learning in vision, gradually replacing the rich literature of alternatives such as meta-learning. In trying to harness the best of both worlds, meta-tuning introduces a subsequent optimization stage of foundation models but has so far only shown limited success and crucially tends to underperform on out-of-distribution (OOD) tasks. In this paper, we introduce Sparse MetA-Tuning (SMAT), a method inspired by sparse mixture-of-experts approaches and trained to isolate subsets of pre-trained parameters automatically for meta-tuning on each task. SMAT successfully overcomes OOD sensitivity and delivers on the promise of enhancing the transfer abilities of vision foundation models beyond parameter-efficient finetuning. We establish new state-of-the-art results on a challenging combination of Meta-Dataset augmented with additional OOD tasks in both zero-shot and gradient-based adaptation settings. In addition, we provide a thorough analysis of the superiority of learned over hand-designed sparsity patterns for sparse expert methods and the pivotal importance of the sparsity level in balancing between in-distribution and out-of-distribution generalization. Our code and models are publicly available.