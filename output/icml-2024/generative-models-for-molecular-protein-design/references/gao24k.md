---
title: "Rethinking Specificity in SBDD: Leveraging Delta Score and Energy-Guided Diffusion"
source: "https://proceedings.mlr.press/v235/gao24k.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/gao24k/gao24k.pdf"
categories: ['generative-models-for-molecular-protein-design', 'generative-models-and-variational-inference']
tags: ['structure-based-drug-design', 'diffusion-models', 'specificity', 'docking-score']
venue: "ICML 2024"
tldr: "A delta score and energy-guided diffusion approach improves molecular specificity in structure-based drug design beyond optimizing raw docking scores."
---

# Rethinking Specificity in SBDD: Leveraging Delta Score and Energy-Guided Diffusion

**Source**: [https://proceedings.mlr.press/v235/gao24k.html](https://proceedings.mlr.press/v235/gao24k.html)

**TLDR**: A delta score and energy-guided diffusion approach improves molecular specificity in structure-based drug design beyond optimizing raw docking scores.

## Abstract

In the field of Structure-based Drug Design (SBDD), deep learning-based generative models have achieved outstanding performance in terms of docking score. However, further study shows that the existing molecular generative methods and docking scores both have lacked consideration in terms of specificity, which means that generated molecules bind to almost every protein pocket with high affinity. To address this, we introduce the Delta Score, a new metric for evaluating the specificity of molecular binding. To further incorporate this insight for generation, we develop an innovative energy-guided approach using contrastive learning, with active compounds as decoys, to direct generative models toward creating molecules with high specificity. Our empirical results show that this method not only enhances the delta score but also maintains or improves traditional docking scores, successfully bridging the gap between SBDD and real-world needs.