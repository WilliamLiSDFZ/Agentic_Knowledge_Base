---
title: "Path-Guided Particle-based Sampling"
source: "https://proceedings.mlr.press/v235/fan24f.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/fan24f/fan24f.pdf"
categories: ['generative-models-and-variational-inference']
tags: ['particle-based-inference', 'SVGD', 'path-guided-sampling']
venue: "ICML 2024"
tldr: "Introduces a path-guided particle-based sampling method using a log-weighted shrinkage framework for improved Bayesian inference."
---

# Path-Guided Particle-based Sampling

**Source**: [https://proceedings.mlr.press/v235/fan24f.html](https://proceedings.mlr.press/v235/fan24f.html)

**TLDR**: Introduces a path-guided particle-based sampling method using a log-weighted shrinkage framework for improved Bayesian inference.

## Abstract

Particle-based Bayesian inference methods by sampling from a partition-free target (posterior) distribution, e.g., Stein variational gradient descent (SVGD), have attracted significant attention. We propose a path-guided particle-based sampling (PGPS) method based on a novel Log-weighted Shrinkage (LwS) density path linking an initial distribution to the target distribution. We propose to utilize a Neural network to learn a vector field motivated by the Fokker-Planck equation of the designed density path. Particles, initiated from the initial distribution, evolve according to the ordinary differential equation defined by the vector field. The distribution of these particles is guided along a density path from the initial distribution to the target distribution. The proposed LwS density path allows for an efficient search of modes of the target distribution while canonical methods fail. We theoretically analyze the Wasserstein distance of the distribution of the PGPS-generated samples and the target distribution due to approximation and discretization errors. Practically, the proposed PGPS-LwS method demonstrates higher Bayesian inference accuracy and better calibration ability in experiments conducted on both synthetic and real-world Bayesian learning tasks, compared to baselines, such as SVGD and Langevin dynamics, etc.