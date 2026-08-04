---
title: "CarbonNovo: Joint Design of Protein Structure and Sequence Using a Unified Energy-based Model"
source: "https://proceedings.mlr.press/v235/ren24e.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/ren24e/ren24e.pdf"
categories: ['generative-models-for-molecular-protein-design', 'generative-models-and-variational-inference']
tags: ['protein-design', 'de-novo', 'energy-based-model', 'joint-structure-sequence', 'unified-model']
venue: "ICML 2024"
tldr: "CarbonNovo jointly designs protein structure and sequence using a unified energy-based model, avoiding the limitations of separate two-stage approaches."
---

# CarbonNovo: Joint Design of Protein Structure and Sequence Using a Unified Energy-based Model

**Source**: [https://proceedings.mlr.press/v235/ren24e.html](https://proceedings.mlr.press/v235/ren24e.html)

**TLDR**: CarbonNovo jointly designs protein structure and sequence using a unified energy-based model, avoiding the limitations of separate two-stage approaches.

## Abstract

De novo protein design aims to create novel protein structures and sequences unseen in nature. Recent structure-oriented design methods typically employ a two-stage strategy, where structure design and sequence design modules are trained separately, and the backbone structures and sequences are generated sequentially in inference. While diffusion-based generative models like RFdiffusion show great promise in structure design, they face inherent limitations within the two-stage framework. First, the sequence design module risks overfitting, as the accuracy of the generated structures may not align with that of the crystal structures used for training. Second, the sequence design module lacks interaction with the structure design module to further optimize the generated structures. To address these challenges, we propose CarbonNovo, a unified energy-based model for jointly generating protein structure and sequence. Specifically, we leverage a score-based generative model and Markov Random Fields for describing the energy landscape of protein structure and sequence. In CarbonNovo, the structure and sequence design module communicates at each diffusion step, encouraging the generation of more coherent structure-sequence pairs. Moreover, the unified framework allows for incorporating the protein language models as evolutionary constraints for generated proteins. The rigorous evaluation demonstrates that CarbonNovo outperforms two-stage methods across various metrics, including designability, novelty, sequence plausibility, and Rosetta Energy.