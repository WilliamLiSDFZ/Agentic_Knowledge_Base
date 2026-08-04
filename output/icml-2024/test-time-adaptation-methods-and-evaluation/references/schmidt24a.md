---
title: "Tilt your Head: Activating the Hidden Spatial-Invariance of Classifiers"
source: "https://proceedings.mlr.press/v235/schmidt24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/schmidt24a/schmidt24a.pdf"
categories: ['adversarial-robustness-and-model-security', 'test-time-adaptation-methods-and-evaluation']
tags: ['spatial-invariance', 'test-time-adaptation', 'rotation-robustness', 'classifiers', 'deep-neural-networks']
venue: "ICML 2024"
tldr: "Activating hidden spatial invariance in classifiers at test time by tilting the input head improves robustness to spatial transformations without retraining."
---

# Tilt your Head: Activating the Hidden Spatial-Invariance of Classifiers

**Source**: [https://proceedings.mlr.press/v235/schmidt24a.html](https://proceedings.mlr.press/v235/schmidt24a.html)

**TLDR**: Activating hidden spatial invariance in classifiers at test time by tilting the input head improves robustness to spatial transformations without retraining.

## Abstract

Deep neural networks are applied in more and more areas of everyday life. However, they still lack essential abilities, such as robustly dealing with spatially transformed input signals. Approaches to mitigate this severe robustness issue are limited to two pathways: Either models are implicitly regularised by increased sample variability (data augmentation) or explicitly constrained by hard-coded inductive biases. The limiting factor of the former is the size of the data space, which renders sufficient sample coverage intractable. The latter is limited by the engineering effort required to develop such inductive biases for every possible scenario. Instead, we take inspiration from human behaviour, where percepts are modified by mental or physical actions during inference. We propose a novel technique to emulate such an inference process for neural nets. This is achieved by traversing a sparsified inverse transformation tree during inference using parallel energy-based evaluations. Our proposed inference algorithm, called Inverse Transformation Search (ITS), is model-agnostic and equips the model with zero-shot pseudo-invariance to spatially transformed inputs. We evaluated our method on several benchmark datasets, including a synthesised ImageNet test set. ITS outperforms the utilised baselines on all zero-shot test scenarios.