---
title: "The Role of Learning Algorithms in Collective Action"
source: "https://proceedings.mlr.press/v235/ben-dov24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/ben-dov24a/ben-dov24a.pdf"
categories: ['strategic-information-manipulation-and-classification', 'online-learning-and-sequential-decision-making']
tags: ['collective-action', 'machine-learning', 'strategic-manipulation', 'learning-algorithms', 'coordinated-groups']
venue: "ICML 2024"
tldr: "Studies how coordinated groups can influence machine learning algorithms beyond Bayes-optimal classifiers, examining the role of learning algorithms in collective action."
---

# The Role of Learning Algorithms in Collective Action

**Source**: [https://proceedings.mlr.press/v235/ben-dov24a.html](https://proceedings.mlr.press/v235/ben-dov24a.html)

**TLDR**: Studies how coordinated groups can influence machine learning algorithms beyond Bayes-optimal classifiers, examining the role of learning algorithms in collective action.

## Abstract

Collective action in machine learning is the study of the control that a coordinated group can have over machine learning algorithms. While previous research has concentrated on assessing the impact of collectives against Bayes (sub-)optimal classifiers, this perspective is limited in that it does not account for the choice of learning algorithm. Since classifiers seldom behave like Bayes classifiers and are influenced by the choice of learning algorithms along with their inherent biases, in this work we initiate the study of how the choice of the learning algorithm plays a role in the success of a collective in practical settings. Specifically, we focus on distributionally robust optimization (DRO), popular for improving a worst group error, and on the ubiquitous stochastic gradient descent (SGD), due to its inductive bias for "simpler" functions. Our empirical results, supported by a theoretical foundation, show that the effective size and success of the collective are highly dependent on properties of the learning algorithm. This highlights the necessity of taking the learning algorithm into account when studying the impact of collective action in machine learning.