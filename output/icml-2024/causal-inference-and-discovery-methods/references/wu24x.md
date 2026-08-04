---
title: "Policy Learning for Balancing Short-Term and Long-Term Rewards"
source: "https://proceedings.mlr.press/v235/wu24x.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/wu24x/wu24x.pdf"
categories: ['causal-inference-and-discovery-methods', 'causal-ml-for-clinical-decision-making']
tags: ['policy-learning', 'long-term-rewards', 'short-term-rewards', 'causal-inference', 'decision-making']
venue: "ICML 2024"
tldr: "Develops a policy learning framework that balances short-term and long-term intervention rewards for empirical researchers and decision-makers."
---

# Policy Learning for Balancing Short-Term and Long-Term Rewards

**Source**: [https://proceedings.mlr.press/v235/wu24x.html](https://proceedings.mlr.press/v235/wu24x.html)

**TLDR**: Develops a policy learning framework that balances short-term and long-term intervention rewards for empirical researchers and decision-makers.

## Abstract

Empirical researchers and decision-makers spanning various domains frequently seek profound insights into the long-term impacts of interventions. While the significance of long-term outcomes is undeniable, an overemphasis on them may inadvertently overshadow short-term gains. Motivated by this, this paper formalizes a new framework for learning the optimal policy that effectively balances both long-term and short-term rewards, where some long-term outcomes are allowed to be missing. In particular, we first present the identifiability of both rewards under mild assumptions. Next, we deduce the semiparametric efficiency bounds, along with the consistency and asymptotic normality of their estimators. We also reveal that short-term outcomes, if associated, contribute to improving the estimator of the long-term reward. Based on the proposed estimators, we develop a principled policy learning approach and further derive the convergence rates of regret and estimation errors associated with the learned policy. Extensive experiments are conducted to validate the effectiveness of the proposed method, demonstrating its practical applicability.