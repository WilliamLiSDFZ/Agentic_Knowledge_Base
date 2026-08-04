---
title: "MolCRAFT: Structure-Based Drug Design in Continuous Parameter Space"
source: "https://proceedings.mlr.press/v235/qu24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/qu24a/qu24a.pdf"
categories: ['generative-models-for-molecular-protein-design', 'generative-models-and-variational-inference']
tags: ['drug-design', 'structure-based', 'generative-models', 'continuous-parameter-space', 'binding-affinity']
venue: "ICML 2024"
tldr: "MolCRAFT generates drug molecules in continuous parameter space for structure-based design with improved 3D pose feasibility."
---

# MolCRAFT: Structure-Based Drug Design in Continuous Parameter Space

**Source**: [https://proceedings.mlr.press/v235/qu24a.html](https://proceedings.mlr.press/v235/qu24a.html)

**TLDR**: MolCRAFT generates drug molecules in continuous parameter space for structure-based design with improved 3D pose feasibility.

## Abstract

Generative models for structure-based drug design (SBDD) have shown promising results in recent years. Existing works mainly focus on how to generate molecules with higher binding affinity, ignoring the feasibility prerequisites for generated 3D poses and resulting in false positives. We conduct thorough studies on key factors of ill-conformational problems when applying autoregressive methods and diffusion to SBDD, including mode collapse and hybrid continuous-discrete space. In this paper, we introduce MolCRAFT, the first SBDD model that operates in the continuous parameter space, together with a novel noise reduced sampling strategy. Empirical results show that our model consistently achieves superior performance in binding affinity with more stable 3D structure, demonstrating our ability to accurately model interatomic interactions. To our best knowledge, MolCRAFT is the first to achieve reference-level Vina Scores (-6.59 kcal/mol) with comparable molecular size, outperforming other strong baselines by a wide margin (-0.84 kcal/mol). Code is available at https://github.com/AlgoMole/MolCRAFT.