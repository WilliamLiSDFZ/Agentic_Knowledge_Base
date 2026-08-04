---
title: "Graph Adversarial Diffusion Convolution"
source: "https://proceedings.mlr.press/v235/liu24h.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/liu24h/liu24h.pdf"
categories: ['graph-neural-networks-and-topology']
tags: ['graph-signal-denoising', 'adversarial-diffusion', 'min-max-optimization']
venue: "ICML 2024"
tldr: "A min-max optimization formulation for graph signal denoising introduces adversarial perturbations to graph structure yielding improved convolution operators."
---

# Graph Adversarial Diffusion Convolution

**Source**: [https://proceedings.mlr.press/v235/liu24h.html](https://proceedings.mlr.press/v235/liu24h.html)

**TLDR**: A min-max optimization formulation for graph signal denoising introduces adversarial perturbations to graph structure yielding improved convolution operators.

## Abstract

This paper introduces a min-max optimization formulation for the Graph Signal Denoising (GSD) problem. In this formulation, we first maximize the second term of GSD by introducing perturbations to the graph structure based on Laplacian distance and then minimize the overall loss of the GSD. By solving the min-max optimization problem, we derive a new variant of the Graph Diffusion Convolution (GDC) architecture, called Graph Adversarial Diffusion Convolution (GADC). GADC differs from GDC by incorporating an additional term that enhances robustness against adversarial attacks on the graph structure and noise in node features. Moreover, GADC improves the performance of GDC on heterophilic graphs. Extensive experiments demonstrate the effectiveness of GADC across various datasets. Code is available at https://github.com/SongtaoLiu0823/GADC.