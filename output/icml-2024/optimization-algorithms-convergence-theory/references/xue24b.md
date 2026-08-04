---
title: "Offline Multi-Objective Optimization"
source: "https://proceedings.mlr.press/v235/xue24b.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/xue24b/xue24b.pdf"
categories: ['bayesian-optimization-and-surrogate-methods', 'optimization-algorithms-convergence-theory']
tags: ['offline-optimization', 'multi-objective', 'Pareto-front']
venue: "ICML 2024"
tldr: "Extends offline black-box optimization to the multi-objective setting, optimizing conflicting objectives from a static dataset without environment interaction."
---

# Offline Multi-Objective Optimization

**Source**: [https://proceedings.mlr.press/v235/xue24b.html](https://proceedings.mlr.press/v235/xue24b.html)

**TLDR**: Extends offline black-box optimization to the multi-objective setting, optimizing conflicting objectives from a static dataset without environment interaction.

## Abstract

Offline optimization aims to maximize a black-box objective function with a static dataset and has wide applications. In addition to the objective function being black-box and expensive to evaluate, numerous complex real-world problems entail optimizing multiple conflicting objectives, i.e., multi-objective optimization (MOO). Nevertheless, offline MOO has not progressed as much as offline single-objective optimization (SOO), mainly due to the lack of benchmarks like Design-Bench for SOO. To bridge this gap, we propose a first benchmark for offline MOO, covering a range of problems from synthetic to real-world tasks. This benchmark provides tasks, datasets, and open-source examples, which can serve as a foundation for method comparisons and advancements in offline MOO. Furthermore, we analyze how the current related methods can be adapted to offline MOO from four fundamental perspectives, including data, model architecture, learning algorithm, and search algorithm. Empirical results show improvements over the best value of the training set, demonstrating the effectiveness of offline MOO methods. As no particular method stands out significantly, there is still an open challenge in further enhancing the effectiveness of offline MOO. We finally discuss future challenges for offline MOO, with the hope of shedding some light on this emerging field. Our code is available at https://github.com/lamda-bbo/offline-moo.