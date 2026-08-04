---
title: "Generative Enzyme Design Guided by Functionally Important Sites and Small-Molecule Substrates"
source: "https://proceedings.mlr.press/v235/song24k.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/song24k/song24k.pdf"
categories: ['generative-models-for-molecular-protein-design', 'generative-models-and-variational-inference']
tags: ['enzyme-design', 'generative-models', 'functional-sites', 'small-molecule-substrates']
venue: "ICML 2024"
tldr: "EnzyGen is a unified generative model for designing functional enzymes conditioned on functionally important sites and small-molecule substrates."
---

# Generative Enzyme Design Guided by Functionally Important Sites and Small-Molecule Substrates

**Source**: [https://proceedings.mlr.press/v235/song24k.html](https://proceedings.mlr.press/v235/song24k.html)

**TLDR**: EnzyGen is a unified generative model for designing functional enzymes conditioned on functionally important sites and small-molecule substrates.

## Abstract

Enzymes are genetically encoded biocatalysts capable of accelerating chemical reactions. How can we automatically design functional enzymes? In this paper, we propose EnzyGen, an approach to learn a unified model to design enzymes across all functional families. Our key idea is to generate an enzyme’s amino acid sequence and their three-dimensional (3D) coordinates based on functionally important sites and substrates corresponding to a desired catalytic function. These sites are automatically mined from enzyme databases. EnzyGen consists of a novel interleaving network of attention and neighborhood equivariant layers, which captures both long-range correlation in an entire protein sequence and local influence from nearest amino acids in 3D space. To learn the generative model, we devise a joint training objective, including a sequence generation loss, a position prediction loss and an enzyme-substrate interaction loss. We further construct EnzyBench, a dataset with 3157 enzyme families, covering all available enzymes within the protein data bank (PDB). Experimental results show that our EnzyGen consistently achieves the best performance across all 323 testing families, surpassing the best baseline by 10.79% in terms of substrate binding affinity. These findings demonstrate EnzyGen’s superior capability in designing well-folded and effective enzymes binding to specific substrates with high affinities. Our code, model and dataset are provided at https://github.com/LeiLiLab/EnzyGen.