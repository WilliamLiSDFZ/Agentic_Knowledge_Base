---
title: "Out-of-Domain Generalization in Dynamical Systems Reconstruction"
source: "https://proceedings.mlr.press/v235/goring24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/goring24a/goring24a.pdf"
categories: ['bayesian-filtering-and-dynamical-systems-learning', 'difference-in-differences-based-policy-evaluation']
tags: ['dynamical-systems', 'out-of-domain-generalization', 'neural-ode']
venue: "ICML 2024"
tldr: "This work studies out-of-domain generalization in deep learning-based dynamical systems reconstruction and proposes methods to improve extrapolation."
---

# Out-of-Domain Generalization in Dynamical Systems Reconstruction

**Source**: [https://proceedings.mlr.press/v235/goring24a.html](https://proceedings.mlr.press/v235/goring24a.html)

**TLDR**: This work studies out-of-domain generalization in deep learning-based dynamical systems reconstruction and proposes methods to improve extrapolation.

## Abstract

In science we are interested in finding the governing equations, the dynamical rules, underlying empirical phenomena. While traditionally scientific models are derived through cycles of human insight and experimentation, recently deep learning (DL) techniques have been advanced to reconstruct dynamical systems (DS) directly from time series data. State-of-the-art dynamical systems reconstruction (DSR) methods show promise in capturing invariant and long-term properties of observed DS, but their ability to generalize to unobserved domains remains an open challenge. Yet, this is a crucial property we would expect from any viable scientific theory. In this work, we provide a formal framework that addresses generalization in DSR. We explain why and how out-of-domain (OOD) generalization (OODG) in DSR profoundly differs from OODG considered elsewhere in machine learning. We introduce mathematical notions based on topological concepts and ergodic theory to formalize the idea of learnability of a DSR model. We formally prove that black-box DL techniques, without adequate structural priors, generally will not be able to learn a generalizing DSR model. We also show this empirically, considering major classes of DSR algorithms proposed so far, and illustrate where and why they fail to generalize across the whole phase space. Our study provides the first comprehensive mathematical treatment of OODG in DSR, and gives a deeper conceptual understanding of where the fundamental problems in OODG lie and how they could possibly be addressed in practice.