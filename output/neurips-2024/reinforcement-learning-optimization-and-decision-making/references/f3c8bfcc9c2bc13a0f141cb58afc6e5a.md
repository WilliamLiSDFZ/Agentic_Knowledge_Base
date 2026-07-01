---
title: "Practical Bayesian Algorithm Execution via Posterior Sampling"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/f3c8bfcc9c2bc13a0f141cb58afc6e5a-Abstract-Conference.html"
categories: ['reinforcement-learning-optimization-and-decision-making', 'query-efficient-algorithms-with-imperfect-oracles']
tags: ['Bayesian-algorithm-execution', 'posterior-sampling', 'active-learning']
venue: "NeurIPS 2024"
tldr: "Proposes practical posterior sampling methods for Bayesian algorithm execution to efficiently infer algorithm outputs from expensive functions."
---

# Practical Bayesian Algorithm Execution via Posterior Sampling

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/f3c8bfcc9c2bc13a0f141cb58afc6e5a-Abstract-Conference.html](https://papers.nips.cc/paper_files/paper/2024/hash/f3c8bfcc9c2bc13a0f141cb58afc6e5a-Abstract-Conference.html)

**TLDR**: Proposes practical posterior sampling methods for Bayesian algorithm execution to efficiently infer algorithm outputs from expensive functions.

## Abstract

We consider Bayesian algorithm execution (BAX), a framework for efficiently selecting evaluation points of an expensive function to infer a property of interest encoded as the output of a base algorithm. Since the base algorithm typically requires more evaluations than are feasible, it cannot be directly applied. Instead, BAX methods sequentially select evaluation points using a probabilistic numerical approach. Current BAX methods use expected information gain to guide this selection. However, this approach is computationally intensive.  Observing that, in many tasks, the property of interest corresponds to a target set of points defined by the function, we introduce PS-BAX, a simple, effective, and scalable BAX method based on posterior sampling. PS-BAX is applicable to a wide range of problems, including many optimization variants and level set estimation. Experiments across diverse tasks demonstrate that PS-BAX performs competitively with existing baselines while being significantly faster, simpler to implement, and easily parallelizable, setting a strong baseline for future research.  Additionally, we establish conditions under which PS-BAX is asymptotically convergent, offering new insights into posterior sampling as an algorithm design paradigm.