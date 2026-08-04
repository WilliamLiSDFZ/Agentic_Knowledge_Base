---
title: "Pragmatic Feature Preferences: Learning Reward-Relevant Preferences from Human Input"
source: "https://proceedings.mlr.press/v235/peng24d.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/peng24d/peng24d.pdf"
categories: ['large-language-model-alignment-and-capabilities', 'fairness-aware-algorithmic-decision-making']
tags: ['reward-learning', 'preference-learning', 'pragmatic-communication', 'human-feedback', 'RLHF']
venue: "ICML 2024"
tldr: "Proposes a pragmatic framework for extracting fine-grained reward-relevant feature preferences from human input to improve reward model inference."
---

# Pragmatic Feature Preferences: Learning Reward-Relevant Preferences from Human Input

**Source**: [https://proceedings.mlr.press/v235/peng24d.html](https://proceedings.mlr.press/v235/peng24d.html)

**TLDR**: Proposes a pragmatic framework for extracting fine-grained reward-relevant feature preferences from human input to improve reward model inference.

## Abstract

Humans use context to specify preferences over behaviors, i.e. their reward functions. Yet, algorithms for inferring reward models from preference data do not take this social learning view into account. Inspired by pragmatic human communication, we study how to extract fine-grained data regarding why an example is preferred that is useful for learning an accurate reward model. We propose to enrich preference queries to ask both (1) which features of a given example are preferable in addition to (2) comparisons between objects. We derive an approach for learning from these feature-level preferences, both for cases where users specify which features are reward-relevant, and when users do not. We evaluate our approach on linear bandit settings in both visual and language-based domains. Results support the efficiency of our approach in quickly converging to accurate rewards with less comparisons vs. example-only labels. Finally, we validate the real-world applicability with a behavioral experiment on a mushroom foraging task. Our findings suggest that incorporating pragmatic feature preferences is a promising approach for more efficient user-aligned reward learning.