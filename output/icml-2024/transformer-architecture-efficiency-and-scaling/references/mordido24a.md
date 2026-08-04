---
title: "Lookbehind-SAM: k steps back, 1 step forward"
source: "https://proceedings.mlr.press/v235/mordido24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/mordido24a/mordido24a.pdf"
categories: ['optimization-algorithms-convergence-theory', 'transformer-architecture-efficiency-and-scaling']
tags: ['sharpness-aware-minimization', 'SAM', 'optimizer-efficiency', 'loss-landscape']
venue: "ICML 2024"
tldr: "Lookbehind-SAM improves the efficiency of SAM by taking k backward steps to better estimate the sharpness landscape before a single optimizer step forward."
---

# Lookbehind-SAM: k steps back, 1 step forward

**Source**: [https://proceedings.mlr.press/v235/mordido24a.html](https://proceedings.mlr.press/v235/mordido24a.html)

**TLDR**: Lookbehind-SAM improves the efficiency of SAM by taking k backward steps to better estimate the sharpness landscape before a single optimizer step forward.

## Abstract

Sharpness-aware minimization (SAM) methods have gained increasing popularity by formulating the problem of minimizing both loss value and loss sharpness as a minimax objective. In this work, we increase the efficiency of the maximization and minimization parts of SAM’s objective to achieve a better loss-sharpness trade-off. By taking inspiration from the Lookahead optimizer, which uses multiple descent steps ahead, we propose Lookbehind, which performs multiple ascent steps behind to enhance the maximization step of SAM and find a worst-case perturbation with higher loss. Then, to mitigate the variance in the descent step arising from the gathered gradients across the multiple ascent steps, we employ linear interpolation to refine the minimization step. Lookbehind leads to a myriad of benefits across a variety of tasks. Particularly, we show increased generalization performance, greater robustness against noisy weights, as well as improved learning and less catastrophic forgetting in lifelong learning settings. Our code is available at https://github.com/chandar-lab/Lookbehind-SAM.