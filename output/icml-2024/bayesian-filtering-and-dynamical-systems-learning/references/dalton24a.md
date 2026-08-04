---
title: "Physics and Lie symmetry informed Gaussian processes"
source: "https://proceedings.mlr.press/v235/dalton24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/dalton24a/dalton24a.pdf"
categories: ['bayesian-filtering-and-dynamical-systems-learning', 'equivariant-neural-networks-and-symmetry-learning']
tags: ['physics-informed-ml', 'Gaussian-processes', 'Lie-symmetry', 'PDEs', 'symmetry-reduction']
venue: "ICML 2024"
tldr: "Integrates Lie symmetry analysis with physics-informed Gaussian processes to incorporate PDE symmetries for improved scientific machine learning."
---

# Physics and Lie symmetry informed Gaussian processes

**Source**: [https://proceedings.mlr.press/v235/dalton24a.html](https://proceedings.mlr.press/v235/dalton24a.html)

**TLDR**: Integrates Lie symmetry analysis with physics-informed Gaussian processes to incorporate PDE symmetries for improved scientific machine learning.

## Abstract

Physics-informed machine learning (PIML) has established itself as a new scientific paradigm which enables the seamless integration of observational data with partial differential equation (PDE) based physics models. A powerful tool for the analysis, reduction and solution of PDEs is the Lie symmetry method. Nevertheless, only recently has the integration of such symmetries into PIML frameworks begun to be explored. The present work adds to this growing literature by introducing an approach for incorporating a Lie symmetry into a physics-informed Gaussian process (GP) model. The symmetry is introduced as a constraint on the GP; either in a soft manner via virtual observations of an induced PDE called the invariant surface condition, or explicitly through the design of the kernel. Experimental results demonstrate that the use of symmetry constraints improves the performance of the GP for both forward and inverse problems, and that our approach offers competitive performance with neural networks in the low-data environment.