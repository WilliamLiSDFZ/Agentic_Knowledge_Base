---
title: "SurfPro: Functional Protein Design Based on Continuous Surface"
source: "https://proceedings.mlr.press/v235/song24c.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/song24c/song24c.pdf"
categories: ['generative-models-for-molecular-protein-design', 'equivariant-neural-networks-and-symmetry-learning']
tags: ['protein-design', 'molecular-surface', 'geometric-learning', 'biochemical-properties']
venue: "ICML 2024"
tldr: "SurfPro generates functional proteins conditioned on desired continuous molecular surfaces encoding both geometric and biochemical properties."
---

# SurfPro: Functional Protein Design Based on Continuous Surface

**Source**: [https://proceedings.mlr.press/v235/song24c.html](https://proceedings.mlr.press/v235/song24c.html)

**TLDR**: SurfPro generates functional proteins conditioned on desired continuous molecular surfaces encoding both geometric and biochemical properties.

## Abstract

How can we design proteins with desired functions? We are motivated by a chemical intuition that both geometric structure and biochemical properties are critical to a protein’s function. In this paper, we propose SurfPro, a new method to generate functional proteins given a desired surface and its associated biochemical properties. SurfPro comprises a hierarchical encoder that progressively models the geometric shape and biochemical features of a protein surface, and an autoregressive decoder to produce an amino acid sequence. We evaluate SurfPro on a standard inverse folding benchmark CATH 4.2 and two functional protein design tasks: protein binder design and enzyme design. Our SurfPro consistently surpasses previous state-of-the-art inverse folding methods, achieving a recovery rate of 57.78% on CATH 4.2 and higher success rates in terms of protein-protein binding and enzyme-substrate interaction scores