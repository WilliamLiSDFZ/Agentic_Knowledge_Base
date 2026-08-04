---
title: "Vanilla Bayesian Optimization Performs Great in High Dimensions"
source: "https://proceedings.mlr.press/v235/hvarfner24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/hvarfner24a/hvarfner24a.pdf"
categories: ['bayesian-optimization-and-surrogate-methods', 'optimization-algorithms-convergence-theory']
tags: ['bayesian-optimization', 'high-dimensions', 'curse-of-dimensionality', 'gaussian-processes', 'surrogate-models']
venue: "ICML 2024"
tldr: "Demonstrates that vanilla Bayesian optimization without special modifications performs surprisingly well in high-dimensional settings."
---

# Vanilla Bayesian Optimization Performs Great in High Dimensions

**Source**: [https://proceedings.mlr.press/v235/hvarfner24a.html](https://proceedings.mlr.press/v235/hvarfner24a.html)

**TLDR**: Demonstrates that vanilla Bayesian optimization without special modifications performs surprisingly well in high-dimensional settings.

## Abstract

High-dimensional optimization problems have long been considered the Achilles’ heel of Bayesian optimization algorithms. Spurred by the curse of dimensionality, a large collection of algorithms aim to make BO more performant in this setting, commonly by imposing various simplifying assumptions on the objective, thereby decreasing its presumed complexity. In this paper, we identify the degeneracies that make vanilla BO poorly suited to high-dimensional tasks, and further show how existing algorithms address these degeneracies through the lens of model complexity. Motivated by the model complexity measure, we derive an enhancement to the prior assumptions that are typical of the vanilla BO algorithm, which reduces the complexity to manageable levels without imposing structural restrictions on the objective. Our modification - a simple scaling of the Gaussian process lengthscale prior in the dimensionality - reveals that standard BO works drastically better than previously thought in high dimensions. Our insights are supplemented by substantial out-performance of existing state-of-the-art on multiple commonly considered real-world high-dimensional tasks.