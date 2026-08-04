---
title: "Predictive Dynamic Fusion"
source: "https://proceedings.mlr.press/v235/cao24c.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/cao24c/cao24c.pdf"
categories: ['neuromorphic-computing-and-neural-dynamics-modeling', 'time-series-modeling-and-forecasting-methods']
tags: ['multimodal-fusion', 'dynamic-fusion', 'predictive-uncertainty', 'open-environment']
venue: "ICML 2024"
tldr: "Proposes a theoretically grounded predictive dynamic fusion framework for robust multimodal decision-making in open environments."
---

# Predictive Dynamic Fusion

**Source**: [https://proceedings.mlr.press/v235/cao24c.html](https://proceedings.mlr.press/v235/cao24c.html)

**TLDR**: Proposes a theoretically grounded predictive dynamic fusion framework for robust multimodal decision-making in open environments.

## Abstract

Multimodal fusion is crucial in joint decision-making systems for rendering holistic judgments. Since multimodal data changes in open environments, dynamic fusion has emerged and achieved remarkable progress in numerous applications. However, most existing dynamic multimodal fusion methods lack theoretical guarantees and easily fall into suboptimal problems, yielding unreliability and instability. To address this issue, we propose a Predictive Dynamic Fusion (PDF) framework for multimodal learning. We proceed to reveal the multimodal fusion from a generalization perspective and theoretically derive the predictable Collaborative Belief (Co-Belief) with Mono- and Holo-Confidence, which provably reduces the upper bound of generalization error. Accordingly, we further propose a relative calibration strategy to calibrate the predicted Co-Belief for potential uncertainty. Extensive experiments on multiple benchmarks confirm our superiority. Our code is available at https://github.com/Yinan-Xia/PDF.