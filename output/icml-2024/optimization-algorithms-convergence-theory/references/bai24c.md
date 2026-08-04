---
title: "On the Complexity of Finite-Sum Smooth Optimization under the Polyak–Łojasiewicz Condition"
source: "https://proceedings.mlr.press/v235/bai24c.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/bai24c/bai24c.pdf"
categories: ['optimization-algorithms-convergence-theory']
tags: ['PL-condition', 'finite-sum-optimization', 'convergence-complexity']
venue: "ICML 2024"
tldr: "This paper establishes complexity bounds for finite-sum smooth optimization under the Polyak-Łojasiewicz condition."
---

# On the Complexity of Finite-Sum Smooth Optimization under the Polyak–Łojasiewicz Condition

**Source**: [https://proceedings.mlr.press/v235/bai24c.html](https://proceedings.mlr.press/v235/bai24c.html)

**TLDR**: This paper establishes complexity bounds for finite-sum smooth optimization under the Polyak-Łojasiewicz condition.

## Abstract

This paper considers the optimization problem of the form $\min_{{\bf x}\in{\mathbb R}^d} f({\bf x})\triangleq \frac{1}{n}\sum_{i=1}^n f_i({\bf x})$, where $f(\cdot)$ satisfies the Polyak–Łojasiewicz (PL) condition with parameter $\mu$ and $\{f_i(\cdot)\}_{i=1}^n$ is $L$-mean-squared smooth. We show that any gradient method requires at least $\Omega(n+\kappa\sqrt{n}\log(1/\epsilon))$ incremental first-order oracle (IFO) calls to find an $\epsilon$-suboptimal solution, where $\kappa\triangleq L/\mu$ is the condition number of the problem. This result nearly matches upper bounds of IFO complexity for best-known first-order methods. We also study the problem of minimizing the PL function in the distributed setting such that the individuals $f_1(\cdot),…,f_n(\cdot)$ are located on a connected network of $n$ agents. We provide lower bounds of $\Omega(\kappa/\sqrt{\gamma}\log(1/\epsilon))$, $\Omega((\kappa+\tau\kappa/\sqrt{\gamma})\log(1/\epsilon))$ and $\Omega\big(n+\kappa\sqrt{n}\log(1/\epsilon)\big)$ for communication rounds, time cost and local first-order oracle calls respectively, where $\gamma\in(0,1]$ is the spectral gap of the mixing matrix associated with the network and $\tau>0$ is the time cost of per communication round. Furthermore, we propose a decentralized first-order method that nearly matches above lower bounds in expectation.