---
title: "Principled Penalty-based Methods for Bilevel Reinforcement Learning and RLHF"
source: "https://proceedings.mlr.press/v235/shen24g.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/shen24g/shen24g.pdf"
categories: ['quantum-algorithms-for-machine-learning-optimization', 'optimization-algorithms-convergence-theory']
tags: ['bilevel-optimization', 'reinforcement-learning', 'RLHF']
venue: "ICML 2024"
tldr: "This paper introduces principled penalty-based methods for bilevel reinforcement learning problems including incentive design and RLHF with convergence guarantees."
---

# Principled Penalty-based Methods for Bilevel Reinforcement Learning and RLHF

**Source**: [https://proceedings.mlr.press/v235/shen24g.html](https://proceedings.mlr.press/v235/shen24g.html)

**TLDR**: This paper introduces principled penalty-based methods for bilevel reinforcement learning problems including incentive design and RLHF with convergence guarantees.

## Abstract

Bilevel optimization has been recently applied to many machine learning tasks. However, their applications have been restricted to the supervised learning setting, where static objective functions with benign structures are considered. But bilevel problems such as incentive design, inverse reinforcement learning (RL), and RL from human feedback (RLHF) are often modeled as dynamic objective functions that go beyond the simple static objective structures, which pose significant challenges of using existing bilevel solutions. To tackle this new class of bilevel problems, we introduce the first principled algorithmic framework for solving bilevel RL problems through the lens of penalty formulation. We provide theoretical studies of the problem landscape and its penalty-based (policy) gradient algorithms. We demonstrate the effectiveness of our algorithms via simulations in the Stackelberg game and RLHF.