---
title: "Provably Efficient Partially Observable Risk-sensitive Reinforcement Learning with Hindsight Observation"
source: "https://proceedings.mlr.press/v235/zhang24g.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/zhang24g/zhang24g.pdf"
categories: ['multi-agent-mdp-structure-and-dependencies', 'statistical-learning-robustness-uncertainty-quantification']
tags: ['risk-sensitive-RL', 'partial-observability', 'hindsight-observation']
venue: "ICML 2024"
tldr: "First provably efficient regret analysis of risk-sensitive reinforcement learning in partially observable settings with hindsight observations."
---

# Provably Efficient Partially Observable Risk-sensitive Reinforcement Learning with Hindsight Observation

**Source**: [https://proceedings.mlr.press/v235/zhang24g.html](https://proceedings.mlr.press/v235/zhang24g.html)

**TLDR**: First provably efficient regret analysis of risk-sensitive reinforcement learning in partially observable settings with hindsight observations.

## Abstract

This work pioneers regret analysis of risk-sensitive reinforcement learning in partially observable environments with hindsight observation, addressing a gap in theoretical exploration. We introduce a novel formulation that integrates hindsight observations into a Partially Observable Markov Decision Process (POMDP) framework, where the goal is to optimize accumulated reward under the entropic risk measure. We develop the first provably efficient RL algorithm tailored for this setting. We also prove by rigorous analysis that our algorithm achieves polynomial regret $\tilde{O}\left(\frac{e^{|{\gamma}|H}-1}{|{\gamma}|H}H^2\sqrt{KHS^2OA}\right)$, which outperforms or matches existing upper bounds when the model degenerates to risk-neutral or fully observable settings. We adopt the method of change-of-measure and develop a novel analytical tool of beta vectors to streamline mathematical derivations. These techniques are of particular interest to the theoretical study of reinforcement learning.