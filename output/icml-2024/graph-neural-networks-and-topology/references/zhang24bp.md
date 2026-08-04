---
title: "EquiPocket: an E(3)-Equivariant Geometric Graph Neural Network for Ligand Binding Site Prediction"
source: "https://proceedings.mlr.press/v235/zhang24bp.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/zhang24bp/zhang24bp.pdf"
categories: ['graph-neural-networks-and-topology', 'equivariant-neural-networks-and-symmetry-learning']
tags: ['equivariant-GNN', 'protein-binding-site', 'drug-discovery', 'geometric-deep-learning', 'E3-equivariance']
venue: "ICML 2024"
tldr: "Proposes EquiPocket, an E(3)-equivariant geometric graph neural network for accurate ligand binding site prediction on proteins."
---

# EquiPocket: an E(3)-Equivariant Geometric Graph Neural Network for Ligand Binding Site Prediction

**Source**: [https://proceedings.mlr.press/v235/zhang24bp.html](https://proceedings.mlr.press/v235/zhang24bp.html)

**TLDR**: Proposes EquiPocket, an E(3)-equivariant geometric graph neural network for accurate ligand binding site prediction on proteins.

## Abstract

Predicting the binding sites of target proteins plays a fundamental role in drug discovery. Most existing deep-learning methods consider a protein as a 3D image by spatially clustering its atoms into voxels and then feed the voxelized protein into a 3D CNN for prediction. However, the CNN-based methods encounter several critical issues: 1) defective in representing irregular protein structures; 2) sensitive to rotations; 3) insufficient to characterize the protein surface; 4) unaware of protein size shift. To address the above issues, this work proposes EquiPocket, an E(3)-equivariant Graph Neural Network (GNN) for binding site prediction, which comprises three modules: the first one to extract local geometric information for each surface atom, the second one to model both the chemical and spatial structure of protein and the last one to capture the geometry of the surface via equivariant message passing over the surface atoms. We further propose a dense attention output layer to alleviate the effect incurred by variable protein size. Extensive experiments on several representative benchmarks demonstrate the superiority of our framework to the state-of-the-art methods.