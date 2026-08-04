---
title: "Predictive Linear Online Tracking for Unknown Targets"
source: "https://proceedings.mlr.press/v235/tsiamis24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/tsiamis24a/tsiamis24a.pdf"
categories: ['online-learning-and-sequential-decision-making', 'neuromorphic-computing-and-neural-dynamics-modeling']
tags: ['online-tracking', 'linear-control', 'non-stochastic-control']
venue: "ICML 2024"
tldr: "Studies online tracking of unknown non-stationary targets in linear control systems using online non-stochastic control framework."
---

# Predictive Linear Online Tracking for Unknown Targets

**Source**: [https://proceedings.mlr.press/v235/tsiamis24a.html](https://proceedings.mlr.press/v235/tsiamis24a.html)

**TLDR**: Studies online tracking of unknown non-stationary targets in linear control systems using online non-stochastic control framework.

## Abstract

In this paper, we study the problem of online tracking in linear control systems, where the objective is to follow a moving target. Unlike classical tracking control, the target is unknown, non-stationary, and its state is revealed sequentially, thus, fitting the framework of online non-stochastic control. We consider the case of quadratic costs and propose a new algorithm, called predictive linear online tracking (PLOT). The algorithm uses recursive least squares with exponential forgetting to learn a time-varying dynamic model of the target. The learned model is used in the optimal policy under the framework of receding horizon control. We show the dynamic regret of PLOT scales with $\mathcal{O}(\sqrt{TV_T})$, where $V_T$ is the total variation of the target dynamics and $T$ is the time horizon. Unlike prior work, our theoretical results hold for non-stationary targets. We implement our online control algorithm on a real quadrotor, thus, showcasing one of the first successful applications of online control methods on real hardware.