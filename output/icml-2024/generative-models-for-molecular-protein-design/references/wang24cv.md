---
title: "Protein Conformation Generation via Force-Guided SE(3) Diffusion Models"
source: "https://proceedings.mlr.press/v235/wang24cv.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/wang24cv/wang24cv.pdf"
categories: ['generative-models-for-molecular-protein-design']
tags: ['protein-conformation', 'SE3-diffusion', 'force-guided', 'molecular-dynamics']
venue: "ICML 2024"
tldr: "A force-guided SE(3) diffusion model is proposed to generate diverse protein conformations more efficiently than molecular dynamics simulations."
---

# Protein Conformation Generation via Force-Guided SE(3) Diffusion Models

**Source**: [https://proceedings.mlr.press/v235/wang24cv.html](https://proceedings.mlr.press/v235/wang24cv.html)

**TLDR**: A force-guided SE(3) diffusion model is proposed to generate diverse protein conformations more efficiently than molecular dynamics simulations.

## Abstract

The conformational landscape of proteins is crucial to understanding their functionality in complex biological processes. Traditional physics-based computational methods, such as molecular dynamics (MD) simulations, suffer from rare event sampling and long equilibration time problems, hindering their applications in general protein systems. Recently, deep generative modeling techniques, especially diffusion models, have been employed to generate novel protein conformations. However, existing score-based diffusion methods cannot properly incorporate important physical prior knowledge to guide the generation process, causing large deviations in the sampled protein conformations from the equilibrium distribution. In this paper, to overcome these limitations, we propose a force-guided $\mathrm{SE}(3)$ diffusion model, ConfDiff, for protein conformation generation. By incorporating a force-guided network with a mixture of data-based score models, ConfDiff can generate protein conformations with rich diversity while preserving high fidelity. Experiments on a variety of protein conformation prediction tasks, including 12 fast-folding proteins and the Bovine Pancreatic Trypsin Inhibitor (BPTI), demonstrate that our method surpasses the state-of-the-art method.