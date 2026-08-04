---
title: "Learning in Deep Factor Graphs with Gaussian Belief Propagation"
source: "https://proceedings.mlr.press/v235/nabarro24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/nabarro24a/nabarro24a.pdf"
categories: ['bayesian-filtering-and-dynamical-systems-learning']
tags: ['gaussian-belief-propagation', 'factor-graphs', 'probabilistic-inference']
venue: "ICML 2024"
tldr: "Learning in deep Gaussian factor graphs is formulated as inference, treating weights and activations as random variables updated via belief propagation."
---

# Learning in Deep Factor Graphs with Gaussian Belief Propagation

**Source**: [https://proceedings.mlr.press/v235/nabarro24a.html](https://proceedings.mlr.press/v235/nabarro24a.html)

**TLDR**: Learning in deep Gaussian factor graphs is formulated as inference, treating weights and activations as random variables updated via belief propagation.

## Abstract

We propose an approach to do learning in Gaussian factor graphs. We treat all relevant quantities (inputs, outputs, parameters, activations) as random variables in a graphical model, and view training and prediction as inference problems with different observed nodes. Our experiments show that these problems can be efficiently solved with belief propagation (BP), whose updates are inherently local, presenting exciting opportunities for distributed and asynchronous training. Our approach can be scaled to deep networks and provides a natural means to do continual learning: use the BP-estimated posterior of the current task as a prior for the next. On a video denoising task we demonstrate the benefit of learnable parameters over a classical factor graph approach and we show encouraging performance of deep factor graphs for continual image classification.