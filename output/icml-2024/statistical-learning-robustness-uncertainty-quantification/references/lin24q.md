---
title: "Smoothness Adaptive Hypothesis Transfer Learning"
source: "https://proceedings.mlr.press/v235/lin24q.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/lin24q/lin24q.pdf"
categories: ['learning-with-imperfect-data-and-bias', 'statistical-learning-robustness-uncertainty-quantification']
tags: ['transfer-learning', 'kernel-methods', 'smoothness-adaptation']
venue: "ICML 2024"
tldr: "A smoothness-adaptive hypothesis transfer learning algorithm that achieves optimality without requiring prior knowledge of function smoothness."
---

# Smoothness Adaptive Hypothesis Transfer Learning

**Source**: [https://proceedings.mlr.press/v235/lin24q.html](https://proceedings.mlr.press/v235/lin24q.html)

**TLDR**: A smoothness-adaptive hypothesis transfer learning algorithm that achieves optimality without requiring prior knowledge of function smoothness.

## Abstract

Many existing two-phase kernel-based hypothesis transfer learning algorithms employ the same kernel regularization across phases and rely on the known smoothness of functions to obtain optimality. Therefore, they fail to adapt to the varying and unknown smoothness between the target/source and their offset. This paper introduces Smoothness Adaptive Transfer Learning (SATL), a two-phase kernel ridge regression (KRR)-based algorithm to address these limitations. We first demonstrate that employing a misspecified fixed bandwidth Gaussian kernel in target-only KRR learning can achieve minimax optimality when the true function resides in Sobolev spaces. Leveraging this result, SATL enables the estimators to provably and universally adapt to the varying and unknown Sobolev smoothness of the source and offset functions. We derive the minimax lower bound of the learning problem in excess risk and show that SATL achieves a matching upper bound up to logarithmic factors. The optimal statistical rate reveals the factors influencing the transfer dynamics and efficacy, including the source sample size and the relative strength between domains. The theoretical findings and the effectiveness of SATL are confirmed by several experiments.