---
title: "Small-loss Adaptive Regret for Online Convex Optimization"
source: "https://proceedings.mlr.press/v235/yang24l.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/yang24l/yang24l.pdf"
categories: ['online-learning-and-sequential-decision-making', 'optimization-algorithms-convergence-theory']
tags: ['adaptive-regret', 'online-convex-optimization', 'small-loss-bounds']
venue: "ICML 2024"
tldr: "A new small-loss adaptive regret bound for online convex optimization that handles changing environments more tightly than minimax bounds."
---

# Small-loss Adaptive Regret for Online Convex Optimization

**Source**: [https://proceedings.mlr.press/v235/yang24l.html](https://proceedings.mlr.press/v235/yang24l.html)

**TLDR**: A new small-loss adaptive regret bound for online convex optimization that handles changing environments more tightly than minimax bounds.

## Abstract

To deal with changing environments, adaptive regret has been proposed to minimize the regret over every interval. Previous studies have established a small-loss adaptive regret bound for general convex functions under the smoothness condition, offering the advantage of being much tighter than minimax rates for benign problems. However, it remains unclear whether similar bounds are attainable for other types of convex functions, such as exp-concave and strongly convex functions. In this paper, we first propose a novel algorithm that achieves a small-loss adaptive regret bound for exp-concave and smooth function. Subsequently, to address the limitation that existing algorithms can only handle one type of convex functions, we further design a universal algorithm capable of delivering small-loss adaptive regret bounds for general convex, exp-concave, and strongly convex functions simultaneously. That is challenging because the universal algorithm follows the meta-expert framework, and we need to ensure that upper bounds for both meta-regret and expert-regret are of small-loss types. Moreover, we provide a novel analysis demonstrating that our algorithms are also equipped with minimax adaptive regret bounds when functions are non-smooth.