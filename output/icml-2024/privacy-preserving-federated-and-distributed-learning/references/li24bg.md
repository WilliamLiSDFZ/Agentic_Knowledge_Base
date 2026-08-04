---
title: "Privacy Preserving Adaptive Experiment Design"
source: "https://proceedings.mlr.press/v235/li24bg.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/li24bg/li24bg.pdf"
categories: ['privacy-preserving-federated-and-distributed-learning', 'causal-ml-for-clinical-decision-making']
tags: ['differential-privacy', 'adaptive-experiment-design', 'CATE-estimation']
venue: "ICML 2024"
tldr: "Proposes a privacy-preserving adaptive experiment design framework for estimating conditional average treatment effects in clinical trials."
---

# Privacy Preserving Adaptive Experiment Design

**Source**: [https://proceedings.mlr.press/v235/li24bg.html](https://proceedings.mlr.press/v235/li24bg.html)

**TLDR**: Proposes a privacy-preserving adaptive experiment design framework for estimating conditional average treatment effects in clinical trials.

## Abstract

Adaptive experiment is widely adopted to estimate conditional average treatment effect (CATE) in clinical trials and many other scenarios. While the primary goal in experiment is to maximize estimation accuracy, due to the imperative of social welfare, it’s also crucial to provide treatment with superior outcomes to patients, which is measured by regret in contextual bandit framework. Furthermore, privacy concerns arise in clinical scenarios containing sensitive data like patients health records. Therefore, it’s essential for the treatment allocation mechanism to incorporate robust privacy protection measures. In this paper, we investigate the tradeoff between loss of social welfare and statistical power of CATE estimation in contextual bandit experiment. We propose a matched upper and lower bound for the multi-objective optimization problem, and then adopt the concept of Pareto optimality to mathematically characterize the optimality condition. Furthermore, we propose differentially private algorithms which still matches the lower bound, showing that privacy is "almost free". Additionally, we derive the asymptotic normality of the estimator, which is essential in statistical inference and hypothesis testing.