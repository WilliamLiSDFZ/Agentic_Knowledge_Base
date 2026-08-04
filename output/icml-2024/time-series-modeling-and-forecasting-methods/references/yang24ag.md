---
title: "Neuro-Symbolic Temporal Point Processes"
source: "https://proceedings.mlr.press/v235/yang24ag.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/yang24ag/yang24ag.pdf"
categories: ['neural-symbolic-combinatorial-optimization-learning', 'time-series-modeling-and-forecasting-methods']
tags: ['temporal-logic', 'neural-symbolic', 'point-processes']
venue: "ICML 2024"
tldr: "A neuro-symbolic framework for efficiently discovering compact temporal logic rules to explain irregular events using temporal point process models."
---

# Neuro-Symbolic Temporal Point Processes

**Source**: [https://proceedings.mlr.press/v235/yang24ag.html](https://proceedings.mlr.press/v235/yang24ag.html)

**TLDR**: A neuro-symbolic framework for efficiently discovering compact temporal logic rules to explain irregular events using temporal point process models.

## Abstract

Our goal is to $\textit{efficiently}$ discover a compact set of temporal logic rules to explain irregular events of interest. We introduce a neural-symbolic rule induction framework within the temporal point process model. The negative log-likelihood is the loss that guides the learning, where the explanatory logic rules and their weights are learned end-to-end in a $\textit{differentiable}$ way. Specifically, predicates and logic rules are represented as $\textit{vector embeddings}$, where the predicate embeddings are fixed and the rule embeddings are trained via gradient descent to obtain the most appropriate compositional representations of the predicate embeddings. To make the rule learning process more efficient and flexible, we adopt a $\textit{sequential covering algorithm}$, which progressively adds rules to the model and removes the event sequences that have been explained until all event sequences have been covered. All the found rules will be fed back to the models for a final rule embedding and weight refinement. Our approach showcases notable efficiency and accuracy across synthetic and real datasets, surpassing state-of-the-art baselines by a wide margin in terms of efficiency.