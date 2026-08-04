---
title: "Hierarchical State Space Models for Continuous Sequence-to-Sequence Modeling"
source: "https://proceedings.mlr.press/v235/bhirangi24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/bhirangi24a/bhirangi24a.pdf"
categories: ['sequence-models-for-memory-and-state', 'time-series-modeling-and-forecasting-methods']
tags: ['state-space-models', 'sequence-to-sequence', 'hierarchical', 'sensory-data']
venue: "ICML 2024"
tldr: "This paper proposes hierarchical state space models for continuous sequence-to-sequence modeling of long raw sensory data streams for physical quantity prediction."
---

# Hierarchical State Space Models for Continuous Sequence-to-Sequence Modeling

**Source**: [https://proceedings.mlr.press/v235/bhirangi24a.html](https://proceedings.mlr.press/v235/bhirangi24a.html)

**TLDR**: This paper proposes hierarchical state space models for continuous sequence-to-sequence modeling of long raw sensory data streams for physical quantity prediction.

## Abstract

Reasoning from sequences of raw sensory data is a ubiquitous problem across fields ranging from medical devices to robotics. These problems often involve using long sequences of raw sensor data (e.g. magnetometers, piezoresistors) to predict sequences of desirable physical quantities (e.g. force, inertial measurements). While classical approaches are powerful for locally-linear prediction problems, they often fall short when using real-world sensors. These sensors are typically non-linear, are affected by extraneous variables (e.g. vibration), and exhibit data-dependent drift. For many problems, the prediction task is exacerbated by small labeled datasets since obtaining ground-truth labels requires expensive equipment. In this work, we present Hierarchical State-Space models (HiSS), a conceptually simple, new technique for continuous sequential prediction. HiSS stacks structured state-space models on top of each other to create a temporal hierarchy. Across six real-world sensor datasets, from tactile-based state prediction to accelerometer-based inertial measurement, HiSS outperforms state-of-the-art sequence models such as causal Transformers, LSTMs, S4, and Mamba by at least 23% on MSE. Our experiments further indicate that HiSS demonstrates efficient scaling to smaller datasets and is compatible with existing data-filtering techniques. Code, datasets and videos can be found on https://hiss-csp.github.io.