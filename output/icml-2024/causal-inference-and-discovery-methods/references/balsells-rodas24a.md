---
title: "On the Identifiability of Switching Dynamical Systems"
source: "https://proceedings.mlr.press/v235/balsells-rodas24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/balsells-rodas24a/balsells-rodas24a.pdf"
categories: ['causal-inference-and-discovery-methods', 'bayesian-filtering-and-dynamical-systems-learning']
tags: ['identifiability', 'switching-dynamical-systems', 'latent-variables']
venue: "ICML 2024"
tldr: "This work studies the identifiability of switching dynamical systems, extending identifiability analysis to hybrid latent variable models."
---

# On the Identifiability of Switching Dynamical Systems

**Source**: [https://proceedings.mlr.press/v235/balsells-rodas24a.html](https://proceedings.mlr.press/v235/balsells-rodas24a.html)

**TLDR**: This work studies the identifiability of switching dynamical systems, extending identifiability analysis to hybrid latent variable models.

## Abstract

The identifiability of latent variable models has received increasing attention due to its relevance in interpretability and out-of-distribution generalisation. In this work, we study the identifiability of Switching Dynamical Systems, taking an initial step toward extending identifiability analysis to sequential latent variable models. We first prove the identifiability of Markov Switching Models, which commonly serve as the prior distribution for the continuous latent variables in Switching Dynamical Systems. We present identification conditions for first-order Markov dependency structures, whose transition distribution is parametrised via non-linear Gaussians. We then establish the identifiability of the latent variables and non-linear mappings in Switching Dynamical Systems up to affine transformations, by leveraging identifiability analysis techniques from identifiable deep latent variable models. We finally develop estimation algorithms for identifiable Switching Dynamical Systems. Throughout empirical studies, we demonstrate the practicality of identifiable Switching Dynamical Systems for segmenting high-dimensional time series such as videos, and showcase the use of identifiable Markov Switching Models for regime-dependent causal discovery in climate data.