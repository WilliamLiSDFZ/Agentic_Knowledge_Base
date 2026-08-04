---
title: "BeigeMaps: Behavioral Eigenmaps for Reinforcement Learning from Images"
source: "https://proceedings.mlr.press/v235/adhikary24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/adhikary24a/adhikary24a.pdf"
categories: ['generative-models-and-variational-inference']
tags: ['reinforcement-learning', 'bisimulation', 'behavioral-eigenmaps', 'representation-learning', 'images']
venue: "ICML 2024"
tldr: "BeigeMaps learns behavioral eigenmaps from images for RL by approximating bisimulation metrics via spectral decomposition."
---

# BeigeMaps: Behavioral Eigenmaps for Reinforcement Learning from Images

**Source**: [https://proceedings.mlr.press/v235/adhikary24a.html](https://proceedings.mlr.press/v235/adhikary24a.html)

**TLDR**: BeigeMaps learns behavioral eigenmaps from images for RL by approximating bisimulation metrics via spectral decomposition.

## Abstract

Training reinforcement learning (RL) agents directly from high-dimensional image observations continues to be a challenging problem. Recent line of work on behavioral distances proposes to learn representations that encode behavioral similarities quantified by the bisimulation metric. By learning an isometric mapping to a lower dimensional space that preserves this metric, such methods attempt to learn representations that group together functionally similar states. However, such an isometric mapping may not exist, making the learning objective ill-defined. We propose an alternative objective that allows distortions in long-range distances, while preserving local metric structure – inducing representations that highlight natural clusters in the state space. This leads to new representations, which we term Behavioral Eigenmaps (BeigeMaps), corresponding to the eigenfunctions of similarity kernels induced by behavioral distances. We empirically demonstrate that when added as a drop-in modification, BeigeMaps improve the policy performance of prior behavioral distance based RL algorithms.