---
title: "Predictive Coding beyond Correlations"
source: "https://proceedings.mlr.press/v235/salvatori24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/salvatori24a/salvatori24a.pdf"
categories: ['neuromorphic-computing-and-neural-dynamics-modeling', 'neural-network-learning-dynamics-theory']
tags: ['predictive-coding', 'biologically-plausible-learning', 'neuromorphic', 'backpropagation-alternatives', 'causality']
venue: "ICML 2024"
tldr: "Predictive coding is analyzed beyond correlation-based learning to uncover causal and more biologically meaningful learning dynamics."
---

# Predictive Coding beyond Correlations

**Source**: [https://proceedings.mlr.press/v235/salvatori24a.html](https://proceedings.mlr.press/v235/salvatori24a.html)

**TLDR**: Predictive coding is analyzed beyond correlation-based learning to uncover causal and more biologically meaningful learning dynamics.

## Abstract

Biologically plausible learning algorithms offer a promising alternative to traditional deep learning techniques, especially in overcoming the limitations of backpropagation in fast and low-energy neuromorphic implementations. To this end, there has been extensive research in understanding what their capabilities are. In this work, we show how one of such algorithms, called predictive coding, is able to perform causal inference tasks. First, we show how a simple change in the inference process of predictive coding enables to compute interventions without the need to mutilate or redefine a causal graph. Then, we explore applications in cases where the graph is unknown, and has to be inferred from observational data. Empirically, we show how such findings can be used to improve the performance of predictive coding in image classification tasks, and conclude that such models are naturally able to perform causal inference tasks using a biologically plausible kind of message passing.