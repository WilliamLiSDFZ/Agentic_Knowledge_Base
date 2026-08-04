---
title: "A Single-Loop Robust Policy Gradient Method for Robust Markov Decision Processes"
source: "https://proceedings.mlr.press/v235/lin24u.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/lin24u/lin24u.pdf"
categories: ['online-learning-and-sequential-decision-making', 'statistical-learning-robustness-uncertainty-quantification']
tags: ['robust-MDP', 'policy-gradient', 'single-loop']
venue: "ICML 2024"
tldr: "A single-loop robust policy gradient method for solving robust Markov decision processes under transition uncertainty."
---

# A Single-Loop Robust Policy Gradient Method for Robust Markov Decision Processes

**Source**: [https://proceedings.mlr.press/v235/lin24u.html](https://proceedings.mlr.press/v235/lin24u.html)

**TLDR**: A single-loop robust policy gradient method for solving robust Markov decision processes under transition uncertainty.

## Abstract

Robust Markov Decision Processes (RMDPs) have recently been recognized as a valuable and promising approach to discovering a policy with creditable performance, particularly in the presence of a dynamic environment and estimation errors in the transition matrix due to limited data. Despite extensive exploration of dynamic programming algorithms for solving RMDPs, there has been a notable upswing in interest in developing efficient algorithms using the policy gradient method. In this paper, we propose the first single-loop robust policy gradient (SRPG) method with the global optimality guarantee for solving RMDPs through its minimax formulation. Moreover, we complement the convergence analysis of the nonconvex-nonconcave min-max optimization problem with the objective function’s gradient dominance property, which is not explored in the prior literature. Numerical experiments validate the efficacy of SRPG, demonstrating its faster and more robust convergence behavior compared to its nested-loop counterpart.