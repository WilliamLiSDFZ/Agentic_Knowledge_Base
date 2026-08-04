---
title: "NeuralIndicator: Implicit Surface Reconstruction from Neural Indicator Priors"
source: "https://proceedings.mlr.press/v235/huang24b.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/huang24b/huang24b.pdf"
categories: ['3d-vision-and-scene-understanding', 'generative-models-and-variational-inference']
tags: ['implicit-surface-reconstruction', 'neural-indicator', 'point-clouds']
venue: "ICML 2024"
tldr: "Proposes NeuralIndicator, a neural implicit surface reconstruction method leveraging indicator priors for incomplete and noisy point clouds."
---

# NeuralIndicator: Implicit Surface Reconstruction from Neural Indicator Priors

**Source**: [https://proceedings.mlr.press/v235/huang24b.html](https://proceedings.mlr.press/v235/huang24b.html)

**TLDR**: Proposes NeuralIndicator, a neural implicit surface reconstruction method leveraging indicator priors for incomplete and noisy point clouds.

## Abstract

The neural implicit surface reconstruction from unorganized points is still challenging, especially when the point clouds are incomplete and/or noisy with complex topology structure. Unlike previous approaches performing neural implicit surface learning relying on local shape priors, this paper proposes to utilize global shape priors to regularize the neural implicit function learning for more reliable surface reconstruction. To this end, we first introduce a differentiable module to generate a smooth indicator function, which globally encodes both the indicative prior and local SDFs of the entire input point cloud. Benefit from this, we propose a new framework, called NeuralIndicator, to jointly learn both the smooth indicator function and neural implicit function simultaneously, using the global shape prior encoded by smooth indicator function to effectively regularize the neural implicit function learning, towards reliable and high-fidelity surface reconstruction from unorganized points without any normal information. Extensive evaluations on synthetic and real-scan datasets show that our approach consistently outperforms previous approaches, especially when point clouds are incomplete and/or noisy with complex topology structure.