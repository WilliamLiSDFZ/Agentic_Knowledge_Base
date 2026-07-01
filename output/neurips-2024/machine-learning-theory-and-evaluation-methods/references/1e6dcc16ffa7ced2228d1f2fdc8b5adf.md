---
title: "Abstract Reward Processes: Leveraging State Abstraction for Consistent Off-Policy Evaluation"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/1e6dcc16ffa7ced2228d1f2fdc8b5adf-Abstract-Conference.html"
categories: ['reinforcement-learning-optimization-and-decision-making', 'machine-learning-theory-and-evaluation-methods']
tags: ['off-policy-evaluation', 'state-abstraction', 'markov-decision-processes']
venue: "NeurIPS 2024"
tldr: "Leverages state abstraction to define abstract reward processes that reduce variance and bias in off-policy policy evaluation."
---

# Abstract Reward Processes: Leveraging State Abstraction for Consistent Off-Policy Evaluation

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/1e6dcc16ffa7ced2228d1f2fdc8b5adf-Abstract-Conference.html](https://papers.nips.cc/paper_files/paper/2024/hash/1e6dcc16ffa7ced2228d1f2fdc8b5adf-Abstract-Conference.html)

**TLDR**: Leverages state abstraction to define abstract reward processes that reduce variance and bias in off-policy policy evaluation.

## Abstract

Evaluating policies using off-policy data is crucial for applying reinforcement learning to real-world problems such as healthcare and autonomous driving. Previous methods for off-policy evaluation (OPE) generally suffer from high variance or irreducible bias, leading to unacceptably high prediction errors. In this work, we introduce STAR, a framework for OPE that encompasses a broad range of estimators -- which include existing OPE methods as special cases -- that achieve lower mean squared prediction errors. STAR leverages state abstraction to distill complex, potentially continuous problems into compact, discrete models which we call abstract reward processes (ARPs). Predictions from ARPs estimated from off-policy data are provably consistent (asymptotically correct). Rather than proposing a specific estimator, we present a new framework for OPE and empirically demonstrate that estimators within STAR outperform existing methods. The best STAR estimator outperforms baselines in all twelve cases studied, and even the median STAR estimator surpasses the baselines in seven out of the twelve cases.