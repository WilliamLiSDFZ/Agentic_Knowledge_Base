---
title: "Predicting Lagrangian Multipliers for Mixed Integer Linear Programs"
source: "https://proceedings.mlr.press/v235/demelas24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/demelas24a/demelas24a.pdf"
categories: ['neural-symbolic-combinatorial-optimization-learning', 'optimization-algorithms-convergence-theory']
tags: ['Lagrangian-relaxation', 'mixed-integer-programming', 'learning-to-optimize', 'Lagrangian-multipliers', 'combinatorial-optimization']
venue: "ICML 2024"
tldr: "Proposes a machine learning approach to predict high-quality Lagrangian multipliers for mixed integer linear programs to accelerate Lagrangian relaxation."
---

# Predicting Lagrangian Multipliers for Mixed Integer Linear Programs

**Source**: [https://proceedings.mlr.press/v235/demelas24a.html](https://proceedings.mlr.press/v235/demelas24a.html)

**TLDR**: Proposes a machine learning approach to predict high-quality Lagrangian multipliers for mixed integer linear programs to accelerate Lagrangian relaxation.

## Abstract

Lagrangian Relaxation stands among the most efficient approaches for solving Mixed Integer Linear Programs (MILPs) with difficult constraints. Given any duals for these constraints, called Lagrangian Multipliers (LMs), it returns a bound on the optimal value of the MILP, and Lagrangian methods seek the LMs giving the best such bound. But these methods generally rely on iterative algorithms resembling gradient descent to maximize the concave piecewise linear dual function: the computational burden grows quickly with the number of relaxed constraints. We introduce a deep learning approach that bypasses the descent, effectively amortizing per instance optimization. A probabilistic encoder based on a graph neural network computes, given a MILP instance and its Continuous Relaxation (CR) solution, high-dimensional representations of relaxed constraints, which are turned into LMs by a decoder. We train the encoder and the decoder jointly by directly optimizing the bound obtained from the predicted multipliers. Our method is applicable to any problem with a compact MILP formulation, and to any Lagrangian Relaxation providing a tighter bound than CR. Experiments on two widely known problems, Multi-Commodity Network Design and Generalized Assignment, show that our approach closes up to 85% of the gap between the continuous relaxation and the best Lagrangian bound, and provides a high-quality warm-start for descent-based Lagrangian methods.