---
title: "Experts Don’t Cheat: Learning What You Don’t Know By Predicting Pairs"
source: "https://proceedings.mlr.press/v235/johnson24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/johnson24a/johnson24a.pdf"
categories: ['statistical-learning-robustness-uncertainty-quantification', 'uncertainty-calibration-and-distribution-shift-adaptation']
tags: ['uncertainty-quantification', 'hallucination-detection', 'calibration']
venue: "ICML 2024"
tldr: "Proposes a paired-prediction framework to distinguish aleatoric from epistemic uncertainty in generative models without knowing the true data distribution."
---

# Experts Don’t Cheat: Learning What You Don’t Know By Predicting Pairs

**Source**: [https://proceedings.mlr.press/v235/johnson24a.html](https://proceedings.mlr.press/v235/johnson24a.html)

**TLDR**: Proposes a paired-prediction framework to distinguish aleatoric from epistemic uncertainty in generative models without knowing the true data distribution.

## Abstract

Identifying how much a model $\hat{p}_{Y|X}^{\theta}$ knows about the stochastic real-world process $p_{Y|X}$ it was trained on is important to ensure it avoids producing incorrect or "hallucinated" answers or taking unsafe actions. But this is difficult for generative models because probabilistic predictions do not distinguish between per-response noise (aleatoric uncertainty) and lack of knowledge about the process (epistemic uncertainty), and existing epistemic uncertainty quantification techniques tend to be overconfident when the model underfits. We propose a general strategy for teaching a model to both approximate $p_{Y|X}$ and also estimate the remaining gaps between $\hat{p}_{Y|X}^{\theta}$ and $p_{Y|X}$: train it to predict pairs of independent responses drawn from the true conditional distribution, allow it to "cheat" by observing one response while predicting the other, then measure how much it cheats. Remarkably, we prove that being good at cheating (i.e. cheating whenever it improves your prediction) is equivalent to being second-order calibrated, a principled extension of ordinary calibration that allows us to construct provably-correct frequentist confidence intervals for $p_{Y|X}$ and detect incorrect responses with high probability. We demonstrate empirically that our approach accurately estimates how much models don’t know across ambiguous image classification, (synthetic) language modeling, and partially-observable navigation tasks, outperforming existing techniques.