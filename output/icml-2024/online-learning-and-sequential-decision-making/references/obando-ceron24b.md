---
title: "Mixtures of Experts Unlock Parameter Scaling for Deep RL"
source: "https://proceedings.mlr.press/v235/obando-ceron24b.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/obando-ceron24b/obando-ceron24b.pdf"
categories: ['online-learning-and-sequential-decision-making']
tags: ['mixture-of-experts', 'reinforcement-learning', 'scaling-laws', 'parameter-scaling']
venue: "ICML 2024"
tldr: "Mixture-of-Experts architectures unlock parameter scaling laws for deep reinforcement learning domains."
---

# Mixtures of Experts Unlock Parameter Scaling for Deep RL

**Source**: [https://proceedings.mlr.press/v235/obando-ceron24b.html](https://proceedings.mlr.press/v235/obando-ceron24b.html)

**TLDR**: Mixture-of-Experts architectures unlock parameter scaling laws for deep reinforcement learning domains.

## Abstract

The recent rapid progress in (self) supervised learning models is in large part predicted by empirical scaling laws: a model’s performance scales proportionally to its size. Analogous scaling laws remain elusive for reinforcement learning domains, however, where increasing the parameter count of a model often hurts its final performance. In this paper, we demonstrate that incorporating Mixture-of-Expert (MoE) modules, and in particular Soft MoEs (Puigcerver et al., 2023), into value-based networks results in more parameter-scalable models, evidenced by substantial performance increases across a variety of training regimes and model sizes. This work thus provides strong empirical evidence towards developing scaling laws for reinforcement learning.