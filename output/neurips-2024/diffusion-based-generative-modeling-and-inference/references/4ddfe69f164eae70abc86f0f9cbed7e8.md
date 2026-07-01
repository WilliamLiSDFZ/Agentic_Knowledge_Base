---
title: "Aligning Target-Aware Molecule Diffusion Models with Exact Energy Optimization"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/4ddfe69f164eae70abc86f0f9cbed7e8-Abstract-Conference.html"
categories: ['machine-learning-for-molecular-biology', 'diffusion-based-generative-modeling-and-inference']
tags: ['structure-based-drug-design', 'diffusion-models', 'energy-optimization']
venue: "NeurIPS 2024"
tldr: "Aligns target-aware molecule diffusion models with exact energy optimization for improved structure-based drug design."
---

# Aligning Target-Aware Molecule Diffusion Models with Exact Energy Optimization

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/4ddfe69f164eae70abc86f0f9cbed7e8-Abstract-Conference.html](https://papers.nips.cc/paper_files/paper/2024/hash/4ddfe69f164eae70abc86f0f9cbed7e8-Abstract-Conference.html)

**TLDR**: Aligns target-aware molecule diffusion models with exact energy optimization for improved structure-based drug design.

## Abstract

Generating ligand molecules for specific protein targets, known as structure-based drug design, is a fundamental problem in therapeutics development and biological discovery. Recently, target-aware generative models, especially diffusion models, have shown great promise in modeling protein-ligand interactions and generating candidate drugs. However, existing models primarily focus on learning the chemical distribution of all drug candidates, which lacks effective steerability on the chemical quality of model generations. In this paper, we propose a novel and general alignment framework to align pretrained target diffusion models with preferred functional properties, named AliDiff. AliDiff shifts the target-conditioned chemical distribution towards regions with higher binding affinity and structural rationality, specified by user-defined reward functions, via the preference optimization approach. To avoid the overfitting problem in common preference optimization objectives, we further develop an improved Exact Energy Preference Optimization method to yield an exact and efficient alignment of the diffusion models, and provide the closed-form expression for the converged distribution. Empirical studies on the CrossDocked2020 benchmark show that AliDiff can generate molecules with state-of-the-art binding energies with up to -7.07 Avg. Vina Score, while maintaining strong molecular properties. Code is available at https://github.com/MinkaiXu/AliDiff.