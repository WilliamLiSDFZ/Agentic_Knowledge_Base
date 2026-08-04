---
title: "Risk-Sensitive Policy Optimization via Predictive CVaR Policy Gradient"
source: "https://proceedings.mlr.press/v235/kim24x.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/kim24x/kim24x.pdf"
categories: ['online-learning-and-sequential-decision-making', 'optimization-algorithms-convergence-theory']
tags: ['CVaR', 'risk-sensitive-RL', 'policy-gradient']
venue: "ICML 2024"
tldr: "Introduces a predictive CVaR policy gradient method that integrates risk sensitivity into standard policy gradient algorithms with minimal modifications."
---

# Risk-Sensitive Policy Optimization via Predictive CVaR Policy Gradient

**Source**: [https://proceedings.mlr.press/v235/kim24x.html](https://proceedings.mlr.press/v235/kim24x.html)

**TLDR**: Introduces a predictive CVaR policy gradient method that integrates risk sensitivity into standard policy gradient algorithms with minimal modifications.

## Abstract

This paper addresses a policy optimization task with the conditional value-at-risk (CVaR) objective. We introduce the predictive CVaR policy gradient, a novel approach that seamlessly integrates risk-neutral policy gradient algorithms with minimal modifications. Our method incorporates a reweighting strategy in gradient calculation – individual cost terms are reweighted in proportion to their predicted contribution to the objective. These weights can be easily estimated through a separate learning procedure. We provide theoretical and empirical analyses, demonstrating the validity and effectiveness of our proposed method.