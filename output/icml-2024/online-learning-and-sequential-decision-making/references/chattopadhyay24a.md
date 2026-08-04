---
title: "Performance Bounds for Active Binary Testing with Information Maximization"
source: "https://proceedings.mlr.press/v235/chattopadhyay24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/chattopadhyay24a/chattopadhyay24a.pdf"
categories: ['data-selection-and-active-learning-methods', 'online-learning-and-sequential-decision-making']
tags: ['active-testing', 'binary-tests', 'information-maximization', 'performance-bounds']
venue: "ICML 2024"
tldr: "Performance bounds are derived for adaptive binary testing strategies that select tests to maximize information about an unknown random variable."
---

# Performance Bounds for Active Binary Testing with Information Maximization

**Source**: [https://proceedings.mlr.press/v235/chattopadhyay24a.html](https://proceedings.mlr.press/v235/chattopadhyay24a.html)

**TLDR**: Performance bounds are derived for adaptive binary testing strategies that select tests to maximize information about an unknown random variable.

## Abstract

In many applications like experimental design, group testing, and medical diagnosis, the state of a random variable $Y$ is revealed by successively observing the outcomes of binary tests about $Y$. New tests are selected adaptively based on the history of outcomes observed so far. If the number of states of $Y$ is finite, the process ends when $Y$ can be predicted with a desired level of confidence or all available tests have been used. Finding the strategy that minimizes the expected number of tests needed to predict $Y$ is virtually impossible in most real applications. Therefore, the commonly used strategy is the greedy heuristic of Information Maximization (InfoMax) that selects tests sequentially in order of information gain. Despite its widespread use, existing guarantees on its performance are often vacuous when compared to its empirical efficiency. In this paper, for the first time to the best of our knowledge, we establish tight non-vacuous bounds on InfoMax’s performance. Our analysis is based on the assumption that at any iteration of the greedy strategy, there is always a binary test available whose conditional probability of being ’true’, given the history, is within $\delta$ units of one-half. This assumption is motivated by practical applications where the available set of tests often satisfies this property for modest values of $\delta$, say, ${0.1 \leq \delta \leq 0.4}$. Specifically, we analyze two distinct scenarios: (i) all tests are functions of $Y$, and (ii) test outcomes are corrupted by a binary symmetric channel. For both cases, our bounds guarantee the near-optimal performance of InfoMax for modest $\delta$ values. It requires only a small multiplicative factor of the entropy of $Y$, in terms of the average number of tests needed to make accurate predictions.