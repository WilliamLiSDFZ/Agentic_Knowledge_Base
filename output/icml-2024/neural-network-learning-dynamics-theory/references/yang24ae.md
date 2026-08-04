---
title: "How Graph Neural Networks Learn: Lessons from Training Dynamics"
source: "https://proceedings.mlr.press/v235/yang24ae.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/yang24ae/yang24ae.pdf"
categories: ['graph-neural-networks-and-topology', 'neural-network-learning-dynamics-theory']
tags: ['graph-neural-networks', 'training-dynamics', 'learning-behavior']
venue: "ICML 2024"
tldr: "An empirical and theoretical study of how graph neural networks learn, drawing lessons from their training dynamics."
---

# How Graph Neural Networks Learn: Lessons from Training Dynamics

**Source**: [https://proceedings.mlr.press/v235/yang24ae.html](https://proceedings.mlr.press/v235/yang24ae.html)

**TLDR**: An empirical and theoretical study of how graph neural networks learn, drawing lessons from their training dynamics.

## Abstract

A long-standing goal in deep learning has been to characterize the learning behavior of black-box models in a more interpretable manner. For graph neural networks (GNNs), considerable advances have been made in formalizing what functions they can represent, but whether GNNs will learn desired functions during the optimization process remains less clear. To fill this gap, we study their training dynamics in function space. In particular, we find that the optimization of GNNs through gradient descent implicitly leverages the graph structure to update the learned function. This phenomenon is dubbed as kernel-graph alignment, which has been empirically and theoretically corroborated. This new analytical framework from the optimization perspective enables interpretable explanations of when and why the learned GNN functions generalize, which are relevant to their limitations on heterophilic graphs. From a practical standpoint, it also provides high-level principles for designing new algorithms. We exemplify this by showing that a simple and efficient non-parametric algorithm, obtained by explicitly using graph structure to update the learned function, can consistently compete with nonlinear GNNs.