---
title: "Randomized Confidence Bounds for Stochastic Partial Monitoring"
source: "https://proceedings.mlr.press/v235/heuillet24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/heuillet24a/heuillet24a.pdf"
categories: ['online-learning-and-sequential-decision-making', 'statistical-learning-robustness-uncertainty-quantification']
tags: ['partial-monitoring', 'sequential-learning', 'confidence-bounds', 'stochastic']
venue: "ICML 2024"
tldr: "Develops randomized confidence bounds for stochastic partial monitoring to improve sequential learning with incomplete feedback."
---

# Randomized Confidence Bounds for Stochastic Partial Monitoring

**Source**: [https://proceedings.mlr.press/v235/heuillet24a.html](https://proceedings.mlr.press/v235/heuillet24a.html)

**TLDR**: Develops randomized confidence bounds for stochastic partial monitoring to improve sequential learning with incomplete feedback.

## Abstract

The partial monitoring (PM) framework provides a theoretical formulation of sequential learning problems with incomplete feedback. At each round, a learning agent plays an action while the environment simultaneously chooses an outcome. The agent then observes a feedback signal that is only partially informative about the (unobserved) outcome. The agent leverages the received feedback signals to select actions that minimize the (unobserved) cumulative loss. In contextual PM, the outcomes depend on some side information that is observable by the agent before selecting the action. In this paper, we consider the contextual and non-contextual PM settings with stochastic outcomes. We introduce a new class of PM strategies based on the randomization of deterministic confidence bounds. We also extend regret guarantees to settings where existing stochastic strategies are not applicable. Our experiments show that the proposed RandCBP and RandCBPside* strategies have competitive performance against state-of-the-art baselines in multiple PM games. To illustrate how the PM framework can benefit real world applications, we design a use case on the real-world problem of monitoring the error rate of any deployed classification system.