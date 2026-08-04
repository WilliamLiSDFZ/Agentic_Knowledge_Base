---
title: "Surface-VQMAE: Vector-quantized Masked Auto-encoders on Molecular Surfaces"
source: "https://proceedings.mlr.press/v235/wu24o.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/wu24o/wu24o.pdf"
categories: ['generative-models-for-molecular-protein-design', 'generative-models-and-variational-inference']
tags: ['molecular-surfaces', 'protein-interaction', 'vector-quantization', 'masked-autoencoders', 'protein-representation']
venue: "ICML 2024"
tldr: "Introduces Surface-VQMAE, a vector-quantized masked autoencoder framework for learning protein surface representations to analyze biological functions."
---

# Surface-VQMAE: Vector-quantized Masked Auto-encoders on Molecular Surfaces

**Source**: [https://proceedings.mlr.press/v235/wu24o.html](https://proceedings.mlr.press/v235/wu24o.html)

**TLDR**: Introduces Surface-VQMAE, a vector-quantized masked autoencoder framework for learning protein surface representations to analyze biological functions.

## Abstract

Molecular surfaces imply fingerprints of interaction patterns between proteins. However, non-equivalent efforts have been paid to incorporating the abundant protein surface information for analyzing proteins’ biological functions in juxtaposition to amino acid sequences and 3D structures. We propose a novel surface-based unsupervised learning algorithm termed Surface-VQMAE to overcome this obstacle. In light of surface point clouds’ sparsity and disorder properties, we first partition them into patches and obtain the sequential arrangement via the Morton curve. Successively, a Transformer-based architecture named SurfFormer was introduced to integrate the surface geometry and capture patch-level relations. At last, we enhance the prevalent masked auto-encoder (MAE) with the vector quantization (VQ) technique, which establishes a surface pattern codebook to enforce a discrete posterior distribution of latent variables and achieve more condensed semantics. Our work is the foremost to implement pretraining purely on molecular surfaces and extensive experiments on diverse real-life scenarios including binding site scoring, binding affinity prediction, and mutant effect estimation demonstrate its effectiveness. The code is available at https://github.com/smiles724/VQMAE.