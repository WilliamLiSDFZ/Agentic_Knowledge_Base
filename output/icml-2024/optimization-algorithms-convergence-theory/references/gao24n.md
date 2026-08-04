---
title: "Decoupling Learning and Decision-Making: Breaking the $\mathcalO(\sqrtT)$ Barrier in Online Resource Allocation with First-Order Methods"
source: "https://proceedings.mlr.press/v235/gao24n.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/gao24n/gao24n.pdf"
categories: ['online-learning-matching-market-algorithms', 'optimization-algorithms-convergence-theory']
tags: ['online-linear-programming', 'resource-allocation', 'first-order-methods', 'regret-bounds']
venue: "ICML 2024"
tldr: "A decoupled learning and decision-making framework breaks the O(√T) regret barrier for online resource allocation using first-order methods."
---

# Decoupling Learning and Decision-Making: Breaking the $\mathcalO(\sqrtT)$ Barrier in Online Resource Allocation with First-Order Methods

**Source**: [https://proceedings.mlr.press/v235/gao24n.html](https://proceedings.mlr.press/v235/gao24n.html)

**TLDR**: A decoupled learning and decision-making framework breaks the O(√T) regret barrier for online resource allocation using first-order methods.

## Abstract

Online linear programming plays an important role in both revenue management and resource allocation, and recent research has focused on developing efficient first-order online learning algorithms. Despite the empirical success of first-order methods, they typically achieve regret no better than $\mathcal{O}(\sqrt{T})$, which is suboptimal compared to the $\mathcal{O}(\log T)$ result guaranteed by the state-of-the-art linear programming (LP)-based online algorithms. This paper establishes several important facts about online linear programming, which unveils the challenge for first-order online algorithms to achieve beyond $\mathcal{O}(\sqrt{T})$ regret. To address this challenge, we introduce a new algorithmic framework which decouples learning from decision-making. For the first time, we show that first-order methods can achieve regret $\mathcal{O}(T^{1/3})$ with this new framework.