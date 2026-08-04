---
title: "Delving into the Convergence of Generalized Smooth Minimax Optimization"
source: "https://proceedings.mlr.press/v235/xian24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/xian24a/xian24a.pdf"
categories: ['optimization-algorithms-convergence-theory', 'statistical-learning-robustness-uncertainty-quantification']
tags: ['minimax-optimization', 'generalized-smoothness', 'convergence']
venue: "ICML 2024"
tldr: "Analyzes convergence of minimax optimization algorithms under generalized smoothness conditions beyond standard Lipschitz assumptions."
---

# Delving into the Convergence of Generalized Smooth Minimax Optimization

**Source**: [https://proceedings.mlr.press/v235/xian24a.html](https://proceedings.mlr.press/v235/xian24a.html)

**TLDR**: Analyzes convergence of minimax optimization algorithms under generalized smoothness conditions beyond standard Lipschitz assumptions.

## Abstract

Minimax optimization is fundamental and important for enormous machine learning applications such as generative adversarial network, adversarial training, and robust optimization. Recently, a variety of minimax algorithms with theoretical guarantees based on Lipschitz smoothness have been proposed. However, these algorithms could fail to converge in practice because the requisite Lipschitz smooth condition may not hold even in some classic minimax problems. We will present some counterexamples to reveal this divergence issue. Thus, to fill this gap, we are motivated to delve into the convergence analysis of minimax algorithms under a relaxed Lipschitz smoothness condition, i.e., generalized smoothness. We prove that variants of basic minimax optimization algorithms GDA, SGDA, GDmax and SGDmax can still converge in generalized smooth problems, and hence their theoretical guarantees can be extended to a wider range of applications. We also conduct a numerical experiment to validate the performance of our proposed algorithms.