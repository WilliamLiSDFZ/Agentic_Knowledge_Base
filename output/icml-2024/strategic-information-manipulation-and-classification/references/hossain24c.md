---
title: "Multi-Sender Persuasion: A Computational Perspective"
source: "https://proceedings.mlr.press/v235/hossain24c.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/hossain24c/hossain24c.pdf"
categories: ['multi-agent-interaction-and-coordination-dynamics', 'strategic-information-manipulation-and-classification']
tags: ['multi-sender', 'bayesian-persuasion', 'computational-economics', 'signaling', 'game-theory']
venue: "ICML 2024"
tldr: "Analyzes multi-sender Bayesian persuasion from a computational perspective, extending the classical framework to settings with multiple strategic information senders."
---

# Multi-Sender Persuasion: A Computational Perspective

**Source**: [https://proceedings.mlr.press/v235/hossain24c.html](https://proceedings.mlr.press/v235/hossain24c.html)

**TLDR**: Analyzes multi-sender Bayesian persuasion from a computational perspective, extending the classical framework to settings with multiple strategic information senders.

## Abstract

We consider multiple senders with informational advantage signaling to convince a single self-interested actor to take certain actions. Generalizing the seminal Bayesian Persuasion framework, such settings are ubiquitous in computational economics, multi-agent learning, and machine learning with multiple objectives. The core solution concept here is the Nash equilibrium of senders’ signaling policies. Theoretically, we prove that finding an equilibrium in general is PPAD-Hard; in fact, even computing a sender’s best response is NP-Hard. Given these intrinsic difficulties, we turn to finding local Nash equilibria. We propose a novel differentiable neural network to approximate this game’s non-linear and discontinuous utilities. Complementing this with the extra-gradient algorithm, we discover local equilibria that Pareto dominates full-revelation equilibria and those found by existing neural networks. Broadly, our theoretical and empirical contributions are of interest to a large class of economic problems.