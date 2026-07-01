---
title: "On Feature Learning in Structured State Space Models"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/9c7eeda2dc98e61baa9a5884afd231bc-Abstract-Conference.html"
categories: ['recurrent-and-spiking-neural-network-dynamics', 'deep-learning-optimization-and-generalization-theory']
tags: ['state-space-models', 'Mamba', 'feature-learning', 'scaling', 'structured-SSMs']
venue: "NeurIPS 2024"
tldr: "Analyzes feature learning and scaling behavior of structured state space models like Mamba as alternatives to transformer architectures."
---

# On Feature Learning in Structured State Space Models

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/9c7eeda2dc98e61baa9a5884afd231bc-Abstract-Conference.html](https://papers.nips.cc/paper_files/paper/2024/hash/9c7eeda2dc98e61baa9a5884afd231bc-Abstract-Conference.html)

**TLDR**: Analyzes feature learning and scaling behavior of structured state space models like Mamba as alternatives to transformer architectures.

## Abstract

This paper studies the scaling behavior of state-space models (SSMs) and their structured variants, such as Mamba, that have recently arisen in popularity as alternatives to transformer-based neural network architectures. Specifically, we focus on the capability of SSMs to learn features as their network width approaches infinity. Our findings reveal that established scaling rules, such as the Maximal Update Parameterization, fail to support feature learning as these models cannot be represented in the form of Tensor Programs. Additionally, we demonstrate that spectral scaling conditions, shown to be effective for feature learning in a host of other architectures, do not hold the same implications for SSMs. Through a detailed signal propagation analysis in SSMs, both forward and backward, we identify the appropriate scaling necessary for non-trivial feature evolution in the infinite-width limit. Our proposed scaling shows behavior akin to the Maximal Update Parameterization, such as improved stability, better generalization, and transferability of optimal hyper-parameters from small to large scale SSMs.