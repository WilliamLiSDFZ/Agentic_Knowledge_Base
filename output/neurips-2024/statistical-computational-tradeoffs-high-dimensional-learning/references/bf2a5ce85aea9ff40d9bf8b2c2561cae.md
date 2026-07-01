---
title: "Tight Bounds for Learning RUMs from Small Slates"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/bf2a5ce85aea9ff40d9bf8b2c2561cae-Abstract-Conference.html"
categories: ['machine-learning-theory-and-evaluation-methods', 'statistical-computational-tradeoffs-high-dimensional-learning']
tags: ['random-utility-models', 'learning-from-rankings', 'sample-complexity']
venue: "NeurIPS 2024"
tldr: "This paper establishes tight sample complexity bounds for learning Random Utility Models from small slates of user choices."
---

# Tight Bounds for Learning RUMs from Small Slates

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/bf2a5ce85aea9ff40d9bf8b2c2561cae-Abstract-Conference.html](https://papers.nips.cc/paper_files/paper/2024/hash/bf2a5ce85aea9ff40d9bf8b2c2561cae-Abstract-Conference.html)

**TLDR**: This paper establishes tight sample complexity bounds for learning Random Utility Models from small slates of user choices.

## Abstract

A Random Utility Model (RUM) is a classical model of user behavior defined by a distribution over $\mathbb{R}^n$. A user, presented with a subset of $\\{1,\ldots,n\\}$, will select the item of the subset with the highest utility, according to a utility vector drawn from the specified distribution. In practical settings, the subset is often of small size, as in the ``ten blue links'' of web search. In this paper, we consider a learning setting with complete information on user choices from subsets of size at most $k$. We show that $k=\Theta(\sqrt{n})$ is both necessary and sufficient to predict the distribution of all user choices with an arbitrarily small, constant error.Based on the upper bound, we obtain new algorithms for approximate RUM learning and variations thereof. Furthermore, we employ our lower bound for approximate RUM learning to derive lower bounds to fractional extensions of the well-studied $k$-deck and trace reconstruction problems.