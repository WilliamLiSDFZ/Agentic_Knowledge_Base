---
title: "Asymptotically Optimal and Computationally Efficient Average Treatment Effect Estimation in A/B testing"
source: "https://proceedings.mlr.press/v235/deep24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/deep24a/deep24a.pdf"
categories: ['causal-inference-and-discovery-methods', 'statistical-learning-robustness-uncertainty-quantification']
tags: ['A/B-testing', 'average-treatment-effect', 'sequential-testing', 'optimal-stopping', 'confidence-intervals']
venue: "ICML 2024"
tldr: "Develops an asymptotically optimal and computationally efficient method for estimating average treatment effects with minimum expected sample size in A/B testing."
---

# Asymptotically Optimal and Computationally Efficient Average Treatment Effect Estimation in A/B testing

**Source**: [https://proceedings.mlr.press/v235/deep24a.html](https://proceedings.mlr.press/v235/deep24a.html)

**TLDR**: Develops an asymptotically optimal and computationally efficient method for estimating average treatment effects with minimum expected sample size in A/B testing.

## Abstract

Motivated by practical applications in clinical trials and online platforms, we study A/B testing with the aim of estimating a confidence interval (CI) for the average treatment effect (ATE) using the minimum expected sample size. This CI should have a width at most $\epsilon$ while ensuring that the probability of the CI not containing the true ATE is at most $\delta$. To answer this, we first establish a lower bound on the expected sample size needed for any adaptive policy which constructs a CI of ATE with desired properties. Specifically, we prove that the lower bound is based on the solution to a max-min non-convex optimization problem for small $\delta$. Tailoring the “plug-in” approach for the ATE problem, we construct an adaptive policy that is asymptotically optimal, i.e., matches the lower bound on the expected sample size for small $\delta$. Interestingly, we find that, for small $\epsilon$ and $\delta$, the asymptotically optimal fraction of treatment assignment for A and B is proportional to the standard deviation of the outcome distributions of treatments A and B, respectively. However, as the proposed approach can be computationally intensive, we propose an alternative adaptive policy. This new policy, informed by insights from our lower bound analysis, is computationally efficient while remaining asymptotically optimal for small values of $\epsilon$ and $\delta$. Numerical comparisons demonstrate that both policies perform similarly across practical values of $\epsilon$ and $\delta$, offering efficient solutions for A/B testing.