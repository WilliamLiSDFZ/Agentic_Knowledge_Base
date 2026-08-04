---
title: "Integrating Multimodal Data for Joint Generative Modeling of Complex Dynamics"
source: "https://proceedings.mlr.press/v235/brenner24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/brenner24a/brenner24a.pdf"
categories: ['generative-models-and-variational-inference', 'bayesian-filtering-and-dynamical-systems-learning']
tags: ['multimodal-data', 'generative-modeling', 'nonlinear-dynamical-systems', 'time-series']
venue: "ICML 2024"
tldr: "This paper introduces a joint generative framework for integrating multimodal time series data to model complex nonlinear dynamical systems."
---

# Integrating Multimodal Data for Joint Generative Modeling of Complex Dynamics

**Source**: [https://proceedings.mlr.press/v235/brenner24a.html](https://proceedings.mlr.press/v235/brenner24a.html)

**TLDR**: This paper introduces a joint generative framework for integrating multimodal time series data to model complex nonlinear dynamical systems.

## Abstract

Many, if not most, systems of interest in science are naturally described as nonlinear dynamical systems. Empirically, we commonly access these systems through time series measurements. Often such time series may consist of discrete random variables rather than continuous measurements, or may be composed of measurements from multiple data modalities observed simultaneously. For instance, in neuroscience we may have behavioral labels in addition to spike counts and continuous physiological recordings. While by now there is a burgeoning literature on deep learning for dynamical systems reconstruction (DSR), multimodal data integration has hardly been considered in this context. Here we provide such an efficient and flexible algorithmic framework that rests on a multimodal variational autoencoder for generating a sparse teacher signal that guides training of a reconstruction model, exploiting recent advances in DSR training techniques. It enables to combine various sources of information for optimal reconstruction, even allows for reconstruction from symbolic data (class labels) alone, and connects different types of observations within a common latent dynamics space. In contrast to previous multimodal data integration techniques for scientific applications, our framework is fully generative, producing, after training, trajectories with the same geometrical and temporal structure as those of the ground truth system.