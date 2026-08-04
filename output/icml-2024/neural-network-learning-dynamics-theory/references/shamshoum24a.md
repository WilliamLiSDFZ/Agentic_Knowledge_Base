---
title: "DNCs Require More Planning Steps"
source: "https://proceedings.mlr.press/v235/shamshoum24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/shamshoum24a/shamshoum24a.pdf"
categories: ['neural-symbolic-combinatorial-optimization-learning', 'neural-network-learning-dynamics-theory']
tags: ['differentiable-neural-computers', 'algorithmic-reasoning', 'computational-complexity']
venue: "ICML 2024"
tldr: "This work investigates that Differentiable Neural Computers require more planning steps to correctly solve complex algorithmic problems by accounting for computational complexity."
---

# DNCs Require More Planning Steps

**Source**: [https://proceedings.mlr.press/v235/shamshoum24a.html](https://proceedings.mlr.press/v235/shamshoum24a.html)

**TLDR**: This work investigates that Differentiable Neural Computers require more planning steps to correctly solve complex algorithmic problems by accounting for computational complexity.

## Abstract

Many recent works use machine learning models to solve various complex algorithmic problems. However, these models attempt to reach a solution without considering the problem’s required computational complexity, which can be detrimental to their ability to solve it correctly. In this work we investigate the effect of computational time and memory on generalization of implicit algorithmic solvers. To do so, we focus on the Differentiable Neural Computer (DNC), a general problem solver that also lets us reason directly about its usage of time and memory. In this work, we argue that the number of planning steps the model is allowed to take, which we call ”planning budget”, is a constraint that can cause the model to generalize poorly and hurt its ability to fully utilize its external memory. We evaluate our method on Graph Shortest Path, Convex Hull, Graph MinCut and Associative Recall, and show how the planning budget can drastically change the behavior of the learned algorithm, in terms of learned time complexity, training time, stability and generalization to inputs larger than those seen during training.