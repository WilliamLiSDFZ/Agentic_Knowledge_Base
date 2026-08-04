---
title: "Grokking Group Multiplication with Cosets"
source: "https://proceedings.mlr.press/v235/stander24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/stander24a/stander24a.pdf"
categories: ['neural-network-learning-dynamics-theory', 'algebraic-structures-in-machine-learning']
tags: ['grokking', 'group-theory', 'cosets', 'mechanistic-interpretability']
venue: "ICML 2024"
tldr: "Coset structures are used to explain how neural networks generalize to group multiplication tasks, providing mechanistic insights into the grokking phenomenon."
---

# Grokking Group Multiplication with Cosets

**Source**: [https://proceedings.mlr.press/v235/stander24a.html](https://proceedings.mlr.press/v235/stander24a.html)

**TLDR**: Coset structures are used to explain how neural networks generalize to group multiplication tasks, providing mechanistic insights into the grokking phenomenon.

## Abstract

The complex and unpredictable nature of deep neural networks prevents their safe use in many high-stakes applications. There have been many techniques developed to interpret deep neural networks, but all have substantial limitations. Algorithmic tasks have proven to be a fruitful test ground for interpreting a neural network end-to-end. Building on previous work, we completely reverse engineer fully connected one-hidden layer networks that have “grokked” the arithmetic of the permutation groups $S_5$ and $S_6$. The models discover the true subgroup structure of the full group and converge on neural circuits that decompose the group arithmetic using the permutation group’s subgroups. We relate how we reverse engineered the model’s mechanisms and confirmed our theory was a faithful description of the circuit’s functionality. We also draw attention to current challenges in conducting interpretability research by comparing our work to Chughtai et al. (2023) which alleges to find a different algorithm for this same problem.