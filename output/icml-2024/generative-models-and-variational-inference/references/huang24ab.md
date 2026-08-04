---
title: "Interaction-based Retrieval-augmented Diffusion Models for Protein-specific 3D Molecule Generation"
source: "https://proceedings.mlr.press/v235/huang24ab.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/huang24ab/huang24ab.pdf"
categories: ['generative-models-for-molecular-protein-design', 'generative-models-and-variational-inference']
tags: ['drug-design', 'protein-ligand', 'retrieval-augmented', 'diffusion-model', '3d-molecule-generation']
venue: "ICML 2024"
tldr: "Proposes a retrieval-augmented diffusion model leveraging protein-ligand interaction templates for more effective 3D molecule generation."
---

# Interaction-based Retrieval-augmented Diffusion Models for Protein-specific 3D Molecule Generation

**Source**: [https://proceedings.mlr.press/v235/huang24ab.html](https://proceedings.mlr.press/v235/huang24ab.html)

**TLDR**: Proposes a retrieval-augmented diffusion model leveraging protein-ligand interaction templates for more effective 3D molecule generation.

## Abstract

Generating ligand molecules that bind to specific protein targets via generative models holds substantial promise for advancing structure-based drug design. Existing methods generate molecules from scratch without reference or template ligands, which poses challenges in model optimization and may yield suboptimal outcomes. To address this problem, we propose an innovative interaction-based retrieval-augmented diffusion model named IRDiff to facilitate target-aware molecule generation. IRDiff leverages a curated set of ligand references, i.e., those with desired properties such as high binding affinity, to steer the diffusion model towards synthesizing ligands that satisfy design criteria. Specifically, we utilize a protein-molecule interaction network (PMINet), which is pretrained with binding affinity signals to: (i) retrieve target-aware ligand molecules with high binding affinity to serve as references, and (ii) incorporate essential protein-ligand binding structures for steering molecular diffusion generation with two effective augmentation mechanisms, i.e., retrieval augmentation and self augmentation. Empirical studies on CrossDocked2020 dataset show IRDiff can generate molecules with more realistic 3D structures and achieve state-of-the-art binding affinities towards the protein targets, while maintaining proper molecular properties. The codes and models are available at https://github.com/YangLing0818/IRDiff