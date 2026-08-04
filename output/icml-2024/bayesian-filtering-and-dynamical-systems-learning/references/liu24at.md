---
title: "Amortized Equation Discovery in Hybrid Dynamical Systems"
source: "https://proceedings.mlr.press/v235/liu24at.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/liu24at/liu24at.pdf"
categories: ['amortized-hybrid-dynamical-system-discovery', 'bayesian-filtering-and-dynamical-systems-learning']
tags: ['hybrid-dynamical-systems', 'equation-discovery', 'amortized-inference']
venue: "ICML 2024"
tldr: "An amortized framework for simultaneously discovering equations and segmenting hybrid dynamical systems in a single end-to-end stage."
---

# Amortized Equation Discovery in Hybrid Dynamical Systems

**Source**: [https://proceedings.mlr.press/v235/liu24at.html](https://proceedings.mlr.press/v235/liu24at.html)

**TLDR**: An amortized framework for simultaneously discovering equations and segmenting hybrid dynamical systems in a single end-to-end stage.

## Abstract

Hybrid dynamical systems are prevalent in science and engineering to express complex systems with continuous and discrete states. To learn laws of systems, all previous methods for equation discovery in hybrid systems follow a two-stage paradigm, i.e. they first group time series into small cluster fragments and then discover equations in each fragment separately through methods in non-hybrid systems. Although effective, performance is then limited because these methods ignore the commonalities in the shared dynamics of fragments that are driven by the same equations. Besides, the two-stage paradigm breaks the interdependence between categorizing and representing dynamics that jointly form hybrid systems. In this paper, we reformulate the problem and propose an end-to-end learning framework, i.e. Amortized Equation Discovery (AMORE), to jointly categorize modes and discover equations characterizing motion dynamics of each mode by all segments of the mode. Experiments on four hybrid and six non-hybrid systems demonstrate the superior performance of our method against previous methods on equation discovery, segmentation, and forecasting.