---
title: "Multi-Region Markovian Gaussian Process: An Efficient Method to Discover Directional Communications Across Multiple Brain Regions"
source: "https://proceedings.mlr.press/v235/li24ak.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/li24ak/li24ak.pdf"
categories: ['multi-region-brain-connectivity-modeling', 'bayesian-filtering-and-dynamical-systems-learning']
tags: ['Gaussian-process', 'brain-regions', 'directional-communication', 'Markovian', 'neuroscience']
venue: "ICML 2024"
tldr: "A Multi-Region Markovian Gaussian Process efficiently models directional communications across multiple brain regions."
---

# Multi-Region Markovian Gaussian Process: An Efficient Method to Discover Directional Communications Across Multiple Brain Regions

**Source**: [https://proceedings.mlr.press/v235/li24ak.html](https://proceedings.mlr.press/v235/li24ak.html)

**TLDR**: A Multi-Region Markovian Gaussian Process efficiently models directional communications across multiple brain regions.

## Abstract

Studying the complex interactions between different brain regions is crucial in neuroscience. Various statistical methods have explored the latent communication across multiple brain regions. Two main categories are the Gaussian Process (GP) and Linear Dynamical System (LDS), each with unique strengths. The GP-based approach effectively discovers latent variables with frequency bands and communication directions. Conversely, the LDS-based approach is computationally efficient but lacks powerful expressiveness in latent representation. In this study, we merge both methodologies by creating an LDS mirroring a multi-output GP, termed Multi-Region Markovian Gaussian Process (MRM-GP). Our work establishes a connection between an LDS and a multi-output GP that explicitly models frequencies and phase delays within the latent space of neural recordings. Consequently, the model achieves a linear inference cost over time points and provides an interpretable low-dimensional representation, revealing communication directions across brain regions and separating oscillatory communications into different frequency bands.