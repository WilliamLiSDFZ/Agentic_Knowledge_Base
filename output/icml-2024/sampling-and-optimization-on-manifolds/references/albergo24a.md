---
title: "Stochastic Interpolants with Data-Dependent Couplings"
source: "https://proceedings.mlr.press/v235/albergo24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/albergo24a/albergo24a.pdf"
categories: ['generative-models-and-variational-inference', 'sampling-and-optimization-on-manifolds']
tags: ['generative-models', 'stochastic-interpolants', 'data-dependent-couplings']
venue: "ICML 2024"
tldr: "This paper extends stochastic interpolant generative models to use data-dependent couplings between source and target densities for improved transport."
---

# Stochastic Interpolants with Data-Dependent Couplings

**Source**: [https://proceedings.mlr.press/v235/albergo24a.html](https://proceedings.mlr.press/v235/albergo24a.html)

**TLDR**: This paper extends stochastic interpolant generative models to use data-dependent couplings between source and target densities for improved transport.

## Abstract

Generative models inspired by dynamical transport of measure – such as flows and diffusions – construct a continuous-time map between two probability densities. Conventionally, one of these is the target density, only accessible through samples, while the other is taken as a simple base density that is data-agnostic. In this work, using the framework of stochastic interpolants, we formalize how to couple the base and the target densities, whereby samples from the base are computed conditionally given samples from the target in a way that is different from (but does not preclude) incorporating information about class labels or continuous embeddings. This enables us to construct dynamical transport maps that serve as conditional generative models. We show that these transport maps can be learned by solving a simple square loss regression problem analogous to the standard independent setting. We demonstrate the usefulness of constructing dependent couplings in practice through experiments in super-resolution and in-painting. The code is available at https://github.com/interpolants/couplings.