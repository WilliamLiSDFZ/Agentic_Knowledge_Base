---
title: "Weakly-Supervised Residual Evidential Learning for Multi-Instance Uncertainty Estimation"
source: "https://proceedings.mlr.press/v235/liu24ac.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/liu24ac/liu24ac.pdf"
categories: ['statistical-learning-robustness-uncertainty-quantification', 'learning-with-imperfect-data-and-bias']
tags: ['uncertainty-estimation', 'weakly-supervised', 'multi-instance-learning']
venue: "ICML 2024"
tldr: "A residual evidential learning framework for uncertainty estimation under weak supervision with incomplete label information in multi-instance settings."
---

# Weakly-Supervised Residual Evidential Learning for Multi-Instance Uncertainty Estimation

**Source**: [https://proceedings.mlr.press/v235/liu24ac.html](https://proceedings.mlr.press/v235/liu24ac.html)

**TLDR**: A residual evidential learning framework for uncertainty estimation under weak supervision with incomplete label information in multi-instance settings.

## Abstract

Uncertainty estimation (UE), as an effective means of quantifying predictive uncertainty, is crucial for safe and reliable decision-making, especially in high-risk scenarios. Existing UE schemes usually assume that there are completely-labeled samples to support fully-supervised learning. In practice, however, many UE tasks often have no sufficiently-labeled data to use, such as the Multiple Instance Learning (MIL) with only weak instance annotations. To bridge this gap, this paper, for the first time, addresses the weakly-supervised issue of Multi-Instance UE (MIUE) and proposes a new baseline scheme, Multi-Instance Residual Evidential Learning (MIREL). Particularly, at the fine-grained instance UE with only weak supervision, we derive a multi-instance residual operator through the Fundamental Theorem of Symmetric Functions. On this operator derivation, we further propose MIREL to jointly model the high-order predictive distribution at bag and instance levels for MIUE. Extensive experiments empirically demonstrate that our MIREL not only could often make existing MIL networks perform better in MIUE, but also could surpass representative UE methods by large margins, especially in instance-level UE tasks. Our source code is available at https://github.com/liupei101/MIREL.