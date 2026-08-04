---
title: "Efficient PAC Learnability of Dynamical Systems Over Multilayer Networks"
source: "https://proceedings.mlr.press/v235/qiu24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/qiu24a/qiu24a.pdf"
categories: ['graph-neural-networks-and-topology', 'optimization-algorithms-convergence-theory']
tags: ['networked-dynamical-systems', 'PAC-learning', 'multilayer-networks', 'cascading-phenomena', 'learnability']
venue: "ICML 2024"
tldr: "Efficient PAC learning algorithms for dynamical systems over multilayer networks with theoretical guarantees."
---

# Efficient PAC Learnability of Dynamical Systems Over Multilayer Networks

**Source**: [https://proceedings.mlr.press/v235/qiu24a.html](https://proceedings.mlr.press/v235/qiu24a.html)

**TLDR**: Efficient PAC learning algorithms for dynamical systems over multilayer networks with theoretical guarantees.

## Abstract

Networked dynamical systems are widely used as formal models of real-world cascading phenomena, such as the spread of diseases and information. Prior research has addressed the problem of learning the behavior of an unknown dynamical system when the underlying network has a single layer. In this work, we study the learnability of dynamical systems over multilayer networks, which are more realistic and challenging. First, we present an efficient PAC learning algorithm with provable guarantees to show that the learner only requires a small number of training examples to infer an unknown system. We further provide a tight analysis of the Natarajan dimension which measures the model complexity. Asymptotically, our bound on the Nararajan dimension is tight for almost all multilayer graphs. The techniques and insights from our work provide the theoretical foundations for future investigations of learning problems for multilayer dynamical systems.