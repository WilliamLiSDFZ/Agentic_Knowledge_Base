---
title: "Statistical Properties of Robust Satisficing"
source: "https://proceedings.mlr.press/v235/li24cc.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/li24cc/li24cc.pdf"
categories: ['statistical-learning-robustness-uncertainty-quantification']
tags: ['robust-optimization', 'satisficing', 'statistical-theory']
venue: "ICML 2024"
tldr: "This paper provides the first comprehensive statistical theory for the Robust Satisficing model, analyzing its generalization properties."
---

# Statistical Properties of Robust Satisficing

**Source**: [https://proceedings.mlr.press/v235/li24cc.html](https://proceedings.mlr.press/v235/li24cc.html)

**TLDR**: This paper provides the first comprehensive statistical theory for the Robust Satisficing model, analyzing its generalization properties.

## Abstract

The Robust Satisficing (RS) model is an emerging approach to robust optimization, offering streamlined procedures and robust generalization across various applications. However, the statistical theory of RS remains unexplored in the literature. This paper fills in the gap by comprehensively analyzing the theoretical properties of the RS model. Notably, the RS structure offers a more straightforward path to deriving statistical guarantees compared to the seminal Distributionally Robust Optimization (DRO), resulting in a richer set of results. In particular, we establish two-sided confidence intervals for the optimal loss without the need to solve a minimax optimization problem explicitly. We further provide finite-sample generalization error bounds for the RS optimizer. Importantly, our results extend to scenarios involving distribution shifts, where discrepancies exist between the sampling and target distributions. Our numerical experiments show that the RS model consistently outperforms the baseline empirical risk minimization in small-sample regimes and under distribution shifts. Furthermore, compared to the DRO model, the RS model exhibits lower sensitivity to hyperparameter tuning, highlighting its practicability for robustness considerations.