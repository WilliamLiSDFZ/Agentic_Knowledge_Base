---
title: "Nesting Particle Filters for Experimental Design in Dynamical Systems"
source: "https://proceedings.mlr.press/v235/iqbal24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/iqbal24a/iqbal24a.pdf"
categories: ['bayesian-filtering-and-dynamical-systems-learning', 'bayesian-optimization-and-surrogate-methods']
tags: ['Bayesian-experimental-design', 'sequential-Monte-Carlo', 'nested-particle-filters', 'dynamical-systems', 'policy-optimization']
venue: "ICML 2024"
tldr: "Inside-Out SMC² is a nested sequential Monte Carlo algorithm for Bayesian experimental design in dynamical systems framed as risk-sensitive policy optimization."
---

# Nesting Particle Filters for Experimental Design in Dynamical Systems

**Source**: [https://proceedings.mlr.press/v235/iqbal24a.html](https://proceedings.mlr.press/v235/iqbal24a.html)

**TLDR**: Inside-Out SMC² is a nested sequential Monte Carlo algorithm for Bayesian experimental design in dynamical systems framed as risk-sensitive policy optimization.

## Abstract

In this paper, we propose a novel approach to Bayesian experimental design for non-exchangeable data that formulates it as risk-sensitive policy optimization. We develop the Inside-Out SMC$^2$ algorithm, a nested sequential Monte Carlo technique to infer optimal designs, and embed it into a particle Markov chain Monte Carlo framework to perform gradient-based policy amortization. Our approach is distinct from other amortized experimental design techniques, as it does not rely on contrastive estimators. Numerical validation on a set of dynamical systems showcases the efficacy of our method in comparison to other state-of-the-art strategies.