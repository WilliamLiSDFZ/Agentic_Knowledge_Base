---
title: "Adaptive Advantage-Guided Policy Regularization for Offline Reinforcement Learning"
source: "https://proceedings.mlr.press/v235/liu24ai.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/liu24ai/liu24ai.pdf"
categories: ['online-learning-and-sequential-decision-making', 'optimization-algorithms-convergence-theory']
tags: ['offline-reinforcement-learning', 'policy-regularization', 'out-of-distribution']
venue: "ICML 2024"
tldr: "An advantage-guided policy regularization method for offline RL that reduces unnecessary conservativeness by selectively constraining actions based on estimated advantage."
---

# Adaptive Advantage-Guided Policy Regularization for Offline Reinforcement Learning

**Source**: [https://proceedings.mlr.press/v235/liu24ai.html](https://proceedings.mlr.press/v235/liu24ai.html)

**TLDR**: An advantage-guided policy regularization method for offline RL that reduces unnecessary conservativeness by selectively constraining actions based on estimated advantage.

## Abstract

In offline reinforcement learning, the challenge of out-of-distribution (OOD) is pronounced. To address this, existing methods often constrain the learned policy through policy regularization. However, these methods often suffer from the issue of unnecessary conservativeness, hampering policy improvement. This occurs due to the indiscriminate use of all actions from the behavior policy that generates the offline dataset as constraints. The problem becomes particularly noticeable when the quality of the dataset is suboptimal. Thus, we propose Adaptive Advantage-guided Policy Regularization (A2PR), obtaining high-advantage actions from an augmented behavior policy combined with VAE to guide the learned policy. A2PR can select high-advantage actions that differ from those present in the dataset, while still effectively maintaining conservatism from OOD actions. This is achieved by harnessing the VAE capacity to generate samples matching the distribution of the data points. We theoretically prove that the improvement of the behavior policy is guaranteed. Besides, it effectively mitigates value overestimation with a bounded performance gap. Empirically, we conduct a series of experiments on the D4RL benchmark, where A2PR demonstrates state-of-the-art performance. Furthermore, experimental results on additional suboptimal mixed datasets reveal that A2PR exhibits superior performance. Code is available at https://github.com/ltlhuuu/A2PR.