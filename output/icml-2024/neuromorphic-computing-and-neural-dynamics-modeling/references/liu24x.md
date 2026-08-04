---
title: "On the Feasibility of Single-Pass Full-Capacity Learning in Linear Threshold Neurons with Binary Input Vectors"
source: "https://proceedings.mlr.press/v235/liu24x.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/liu24x/liu24x.pdf"
categories: ['neuromorphic-computing-and-neural-dynamics-modeling']
tags: ['single-pass-learning', 'linear-threshold-neurons', 'binary-inputs']
venue: "ICML 2024"
tldr: "This paper investigates the mathematical feasibility of single-pass learning rules that achieve full capacity in linear threshold neurons with binary inputs."
---

# On the Feasibility of Single-Pass Full-Capacity Learning in Linear Threshold Neurons with Binary Input Vectors

**Source**: [https://proceedings.mlr.press/v235/liu24x.html](https://proceedings.mlr.press/v235/liu24x.html)

**TLDR**: This paper investigates the mathematical feasibility of single-pass learning rules that achieve full capacity in linear threshold neurons with binary inputs.

## Abstract

Known learning rules tend to fall near one of two extremes: single-pass associative learning with low complexity and capacity, and multi-pass iterative learning with high complexity and capacity. In this work we investigate the mathematical feasibility of learning rules that are both single-pass and achieve the theoretical upper bound on capacity. We consider a fairly broad family of learning rules we call “span rules,” which include known rules such as Hebbian learning, perceptron learning, and backpropagation as special cases. To our knowledge, previous work has not determined whether single-pass, full-capacity span rules exist, even in the most fundamental case of a linear threshold neuron with binary input vectors, which is the focus of this study. We derive a necessary condition for the existence of such learning rules, which takes the form of a linear program, and show that the linear program is infeasible. This establishes an impossibility result that span rules can not be both single-pass and full-capacity.