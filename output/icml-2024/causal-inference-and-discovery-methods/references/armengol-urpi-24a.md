---
title: "Causal Action Influence Aware Counterfactual Data Augmentation"
source: "https://proceedings.mlr.press/v235/armengol-urpi-24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/armengol-urpi-24a/armengol-urpi-24a.pdf"
categories: ['causal-inference-and-discovery-methods', 'learning-with-imperfect-data-and-bias']
tags: ['counterfactual-data-augmentation', 'causal-inference', 'offline-RL', 'robot-learning', 'imitation-learning']
venue: "ICML 2024"
tldr: "Uses causal action influence to perform counterfactual data augmentation for improving offline robot learning beyond training distributions."
---

# Causal Action Influence Aware Counterfactual Data Augmentation

**Source**: [https://proceedings.mlr.press/v235/armengol-urpi-24a.html](https://proceedings.mlr.press/v235/armengol-urpi-24a.html)

**TLDR**: Uses causal action influence to perform counterfactual data augmentation for improving offline robot learning beyond training distributions.

## Abstract

Offline data are both valuable and practical resources for teaching robots complex behaviors. Ideally, learning agents should not be constrained by the scarcity of available demonstrations, but rather generalize beyond the training distribution. However, the complexity of real-world scenarios typically requires huge amounts of data to prevent neural network policies from picking up on spurious correlations and learning non-causal relationships. We propose CAIAC, a data augmentation method that can create feasible synthetic transitions from a fixed dataset without having access to online environment interactions. By utilizing principled methods for quantifying causal influence, we are able to perform counterfactual reasoning by swapping $\textit{action}$-unaffected parts of the state-space between independent trajectories in the dataset. We empirically show that this leads to a substantial increase in robustness of offline learning algorithms against distributional shift.