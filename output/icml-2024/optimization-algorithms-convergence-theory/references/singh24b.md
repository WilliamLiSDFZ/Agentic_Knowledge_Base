---
title: "Finite Time Logarithmic Regret Bounds for Self-Tuning Regulation"
source: "https://proceedings.mlr.press/v235/singh24b.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/singh24b/singh24b.pdf"
categories: ['online-learning-and-sequential-decision-making', 'optimization-algorithms-convergence-theory']
tags: ['self-tuning-regulation', 'logarithmic-regret', 'online-control']
venue: "ICML 2024"
tldr: "Establishes the first finite-time logarithmic regret bounds for the self-tuning regulation problem using a modified certainty equivalence algorithm."
---

# Finite Time Logarithmic Regret Bounds for Self-Tuning Regulation

**Source**: [https://proceedings.mlr.press/v235/singh24b.html](https://proceedings.mlr.press/v235/singh24b.html)

**TLDR**: Establishes the first finite-time logarithmic regret bounds for the self-tuning regulation problem using a modified certainty equivalence algorithm.

## Abstract

We establish the first finite-time logarithmic regret bounds for the self-tuning regulation problem. We introduce a modified version of the certainty equivalence algorithm, which we call PIECE, that clips inputs in addition to utilizing probing inputs for exploration. We show that it has a $C \log T$ upper bound on the regret after $T$ time-steps for bounded noise, and $C\log^3 T$ in the case of sub-Gaussian noise, unlike the LQ problem where logarithmic regret is shown to be not possible. The PIECE algorithm is also designed to address the critical challenge of poor initial transient performance of reinforcement learning algorithms for linear systems. Comparative simulation results illustrate the improved performance of PIECE.