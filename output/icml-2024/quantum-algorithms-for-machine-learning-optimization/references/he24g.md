---
title: "Quantum Algorithm for Online Exp-concave Optimization"
source: "https://proceedings.mlr.press/v235/he24g.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/he24g/he24g.pdf"
categories: ['quantum-algorithms-for-machine-learning-optimization', 'online-learning-and-sequential-decision-making']
tags: ['quantum-computing', 'online-learning', 'exp-concave-optimization']
venue: "ICML 2024"
tldr: "Quantum online quasi-Newton methods are proposed for bandit exp-concave optimization, demonstrating quantum advantage over classical algorithms."
---

# Quantum Algorithm for Online Exp-concave Optimization

**Source**: [https://proceedings.mlr.press/v235/he24g.html](https://proceedings.mlr.press/v235/he24g.html)

**TLDR**: Quantum online quasi-Newton methods are proposed for bandit exp-concave optimization, demonstrating quantum advantage over classical algorithms.

## Abstract

We explore whether quantum advantages can be found for the zeroth-order feedback online exp-concave optimization problem, which is also known as bandit exp-concave optimization with multi-point feedback. We present quantum online quasi-Newton methods to tackle the problem and show that there exists quantum advantages for such problems. Our method approximates the Hessian by quantum estimated inexact gradient and can achieve $O(n\log T)$ regret with $O(1)$ queries at each round, where $n$ is the dimension of the decision set and $T$ is the total decision rounds. Such regret improves the optimal classical algorithm by a factor of $T^{2/3}$.