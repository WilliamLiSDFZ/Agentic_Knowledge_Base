---
title: "Tilting the Odds at the Lottery: the Interplay of Overparameterisation and Curricula in Neural Networks"
source: "https://proceedings.mlr.press/v235/mannelli24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/mannelli24a/mannelli24a.pdf"
categories: ['neural-network-learning-dynamics-theory', 'learning-with-imperfect-data-and-bias']
tags: ['overparameterization', 'lottery-ticket-hypothesis', 'curriculum-learning']
venue: "ICML 2024"
tldr: "A theoretical and empirical study on how overparameterization and curriculum learning interact to improve neural network training via the lottery ticket hypothesis."
---

# Tilting the Odds at the Lottery: the Interplay of Overparameterisation and Curricula in Neural Networks

**Source**: [https://proceedings.mlr.press/v235/mannelli24a.html](https://proceedings.mlr.press/v235/mannelli24a.html)

**TLDR**: A theoretical and empirical study on how overparameterization and curriculum learning interact to improve neural network training via the lottery ticket hypothesis.

## Abstract

A wide range of empirical and theoretical works have shown that overparameterisation can amplify the performance of neural networks. According to the lottery ticket hypothesis, overparameterised networks have an increased chance of containing a sub-network that is well-initialised to solve the task at hand. A more parsimonious approach, inspired by animal learning, consists in guiding the learner towards solving the task by curating the order of the examples, ie. providing a curriculum. However, this learning strategy seems to be hardly beneficial in deep learning applications. In this work, we propose a theoretical analysis that connects curriculum learning and overparameterisation. In particular, we investigate their interplay in the online learning setting for a 2-layer network in the XOR-like Gaussian Mixture problem. Our results show that a high degree of overparameterisation—while simplifying the problem—can limit the benefit from curricula, providing a theoretical account of the ineffectiveness of curricula in deep learning.