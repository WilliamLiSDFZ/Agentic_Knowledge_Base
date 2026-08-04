---
title: "Learning Causal Dynamics Models in Object-Oriented Environments"
source: "https://proceedings.mlr.press/v235/yu24j.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/yu24j/yu24j.pdf"
categories: ['causal-inference-and-discovery-methods', 'bayesian-filtering-and-dynamical-systems-learning']
tags: ['causal-dynamics-model', 'reinforcement-learning', 'object-oriented-environments']
venue: "ICML 2024"
tldr: "A method for learning causal dynamics models in object-oriented environments by discovering causal dependencies among environmental variables."
---

# Learning Causal Dynamics Models in Object-Oriented Environments

**Source**: [https://proceedings.mlr.press/v235/yu24j.html](https://proceedings.mlr.press/v235/yu24j.html)

**TLDR**: A method for learning causal dynamics models in object-oriented environments by discovering causal dependencies among environmental variables.

## Abstract

Causal dynamics models (CDMs) have demonstrated significant potential in addressing various challenges in reinforcement learning. To learn CDMs, recent studies have performed causal discovery to capture the causal dependencies among environmental variables. However, the learning of CDMs is still confined to small-scale environments due to computational complexity and sample efficiency constraints. This paper aims to extend CDMs to large-scale object-oriented environments, which consist of a multitude of objects classified into different categories. We introduce the Object-Oriented CDM (OOCDM) that shares causalities and parameters among objects belonging to the same class. Furthermore, we propose a learning method for OOCDM that enables it to adapt to a varying number of objects. Experiments on large-scale tasks indicate that OOCDM outperforms existing CDMs in terms of causal discovery, prediction accuracy, generalization, and computational efficiency.