---
title: "Context-Guided Diffusion for Out-of-Distribution Molecular and Protein Design"
source: "https://proceedings.mlr.press/v235/klarner24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/klarner24a/klarner24a.pdf"
categories: ['generative-models-for-molecular-protein-design', 'generative-models-and-variational-inference']
tags: ['diffusion-models', 'out-of-distribution', 'molecular-design', 'protein-design', 'guided-generation']
venue: "ICML 2024"
tldr: "A context-guided diffusion framework for generating novel molecules and proteins that generalizes beyond training distribution via data-driven guidance."
---

# Context-Guided Diffusion for Out-of-Distribution Molecular and Protein Design

**Source**: [https://proceedings.mlr.press/v235/klarner24a.html](https://proceedings.mlr.press/v235/klarner24a.html)

**TLDR**: A context-guided diffusion framework for generating novel molecules and proteins that generalizes beyond training distribution via data-driven guidance.

## Abstract

Generative models have the potential to accelerate key steps in the discovery of novel molecular therapeutics and materials. Diffusion models have recently emerged as a powerful approach, excelling at unconditional sample generation and, with data-driven guidance, conditional generation within their training domain. Reliably sampling from high-value regions beyond the training data, however, remains an open challenge—with current methods predominantly focusing on modifying the diffusion process itself. In this paper, we develop context-guided diffusion (CGD), a simple plug-and-play method that leverages unlabeled data and smoothness constraints to improve the out-of-distribution generalization of guided diffusion models. We demonstrate that this approach leads to substantial performance gains across various settings, including continuous, discrete, and graph-structured diffusion processes with applications across drug discovery, materials science, and protein design.