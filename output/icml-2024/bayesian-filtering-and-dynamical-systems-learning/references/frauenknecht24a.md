---
title: "Trust the Model Where It Trusts Itself - Model-Based Actor-Critic with Uncertainty-Aware Rollout Adaption"
source: "https://proceedings.mlr.press/v235/frauenknecht24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/frauenknecht24a/frauenknecht24a.pdf"
categories: ['bayesian-filtering-and-dynamical-systems-learning', 'bayesian-optimization-and-surrogate-methods']
tags: ['model-based-RL', 'uncertainty-estimation', 'rollout-length']
venue: "ICML 2024"
tldr: "An uncertainty-aware rollout adaptation method determines when to trust model-based rollouts in Dyna-style reinforcement learning."
---

# Trust the Model Where It Trusts Itself - Model-Based Actor-Critic with Uncertainty-Aware Rollout Adaption

**Source**: [https://proceedings.mlr.press/v235/frauenknecht24a.html](https://proceedings.mlr.press/v235/frauenknecht24a.html)

**TLDR**: An uncertainty-aware rollout adaptation method determines when to trust model-based rollouts in Dyna-style reinforcement learning.

## Abstract

Dyna-style model-based reinforcement learning (MBRL) combines model-free agents with predictive transition models through model-based rollouts. This combination raises a critical question: “When to trust your model?”; i.e., which rollout length results in the model providing useful data? Janner et al. (2019) address this question by gradually increasing rollout lengths throughout the training. While theoretically tempting, uniform model accuracy is a fallacy that collapses at the latest when extrapolating. Instead, we propose asking the question “Where to trust your model?”. Using inherent model uncertainty to consider local accuracy, we obtain the Model-Based Actor-Critic with Uncertainty-Aware Rollout Adaption (MACURA) algorithm. We propose an easy-to-tune rollout mechanism and demonstrate substantial improvements in data efficiency and performance compared to state-of-the-art deep MBRL methods on the MuJoCo benchmark.