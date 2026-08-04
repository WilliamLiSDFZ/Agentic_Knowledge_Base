---
title: "Efficient Policy Evaluation with Offline Data Informed Behavior Policy Design"
source: "https://proceedings.mlr.press/v235/liu24ca.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/liu24ca/liu24ca.pdf"
categories: ['online-learning-and-sequential-decision-making', 'anomaly-and-out-of-distribution-detection']
tags: ['policy-evaluation', 'offline-data', 'behavior-policy', 'reinforcement-learning', 'Monte-Carlo']
venue: "ICML 2024"
tldr: "An offline-data-informed behavior policy design method that reduces environment interactions required for online policy evaluation in reinforcement learning."
---

# Efficient Policy Evaluation with Offline Data Informed Behavior Policy Design

**Source**: [https://proceedings.mlr.press/v235/liu24ca.html](https://proceedings.mlr.press/v235/liu24ca.html)

**TLDR**: An offline-data-informed behavior policy design method that reduces environment interactions required for online policy evaluation in reinforcement learning.

## Abstract

Most reinforcement learning practitioners evaluate their policies with online Monte Carlo estimators for either hyperparameter tuning or testing different algorithmic design choices, where the policy is repeatedly executed in the environment to get the average outcome. Such massive interactions with the environment are prohibitive in many scenarios. In this paper, we propose novel methods that improve the data efficiency of online Monte Carlo estimators while maintaining their unbiasedness. We first propose a tailored closed-form behavior policy that provably reduces the variance of an online Monte Carlo estimator. We then design efficient algorithms to learn this closed-form behavior policy from previously collected offline data. Theoretical analysis is provided to characterize how the behavior policy learning error affects the amount of reduced variance. Compared with previous works, our method achieves better empirical performance in a broader set of environments, with fewer requirements for offline data.