---
title: "Understanding Adam Optimizer via Online Learning of Updates: Adam is FTRL in Disguise"
source: "https://proceedings.mlr.press/v235/ahn24b.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/ahn24b/ahn24b.pdf"
categories: ['optimization-algorithms-convergence-theory']
tags: ['adam-optimizer', 'online-learning', 'FTRL', 'adaptive-optimization']
venue: "ICML 2024"
tldr: "Shows that the Adam optimizer is equivalent to Follow-The-Regularized-Leader, providing new theoretical insight into its behavior."
---

# Understanding Adam Optimizer via Online Learning of Updates: Adam is FTRL in Disguise

**Source**: [https://proceedings.mlr.press/v235/ahn24b.html](https://proceedings.mlr.press/v235/ahn24b.html)

**TLDR**: Shows that the Adam optimizer is equivalent to Follow-The-Regularized-Leader, providing new theoretical insight into its behavior.

## Abstract

Despite the success of the Adam optimizer in practice, the theoretical understanding of its algorithmic components still remains limited. In particular, most existing analyses of Adam show the convergence rate that can be simply achieved by non-adative algorithms like SGD. In this work, we provide a different perspective based on online learning that underscores the importance of Adam’s algorithmic components. Inspired by Cutkosky et al. (2023), we consider the framework called online learning of updates/increments, where we choose the updates/increments of an optimizer based on an online learner. With this framework, the design of a good optimizer is reduced to the design of a good online learner. Our main observation is that Adam corresponds to a principled online learning framework called Follow-the-Regularized-Leader (FTRL). Building on this observation, we study the benefits of its algorithmic components from the online learning perspective.