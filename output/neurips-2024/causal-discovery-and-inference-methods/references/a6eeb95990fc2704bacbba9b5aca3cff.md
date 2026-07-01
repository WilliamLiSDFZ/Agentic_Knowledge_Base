---
title: "Markov Equivalence and Consistency in Differentiable Structure Learning"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/a6eeb95990fc2704bacbba9b5aca3cff-Abstract-Conference.html"
categories: ['causal-discovery-and-inference-methods']
tags: ['structure-learning', 'DAGs', 'Markov-equivalence', 'acyclicity-constraints']
venue: "NeurIPS 2024"
tldr: "This work analyzes Markov equivalence and consistency in differentiable DAG structure learning without strong identifiability assumptions."
---

# Markov Equivalence and Consistency in Differentiable Structure Learning

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/a6eeb95990fc2704bacbba9b5aca3cff-Abstract-Conference.html](https://papers.nips.cc/paper_files/paper/2024/hash/a6eeb95990fc2704bacbba9b5aca3cff-Abstract-Conference.html)

**TLDR**: This work analyzes Markov equivalence and consistency in differentiable DAG structure learning without strong identifiability assumptions.

## Abstract

Existing approaches to differentiable structure learning of directed acyclic graphs (DAGs) rely on strong identifiability assumptions in order to guarantee that global minimizers of the acyclicity-constrained optimization problem identifies the true DAG. Moreover, it has been observed empirically that the optimizer may exploit undesirable artifacts in the loss function. We explain and remedy these issues by studying the behavior of differentiable acyclicity-constrained programs under general likelihoods with multiple global minimizers. By carefully regularizing the likelihood, it is possible to identify the sparsest model in the Markov equivalence class, even in the absence of an identifiable parametrization. We first study the Gaussian case in detail, showing how proper regularization of the likelihood defines a score that identifies the sparsest model. Assuming faithfulness, it also recovers the Markov equivalence class. These results are then generalized to general models and likelihoods, where the same claims hold. These theoretical results are validated empirically, showing how this can be done using standard gradient-based optimizers (without resorting to approximations such as Gumbel-Softmax), thus paving the way for differentiable structure learning under general models and losses. Open-source code is available at \url{https://github.com/duntrain/dagrad}.