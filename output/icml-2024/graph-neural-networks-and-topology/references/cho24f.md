---
title: "Neurodegenerative Brain Network Classification via Adaptive Diffusion with Temporal Regularization"
source: "https://proceedings.mlr.press/v235/cho24f.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/cho24f/cho24f.pdf"
categories: ['graph-neural-networks-and-topology', 'multi-region-brain-connectivity-modeling']
tags: ['brain-connectome', 'neurodegenerative-disease', 'graph-neural-networks']
venue: "ICML 2024"
tldr: "An adaptive diffusion GNN with temporal regularization is proposed for classifying neurodegenerative diseases from brain network data."
---

# Neurodegenerative Brain Network Classification via Adaptive Diffusion with Temporal Regularization

**Source**: [https://proceedings.mlr.press/v235/cho24f.html](https://proceedings.mlr.press/v235/cho24f.html)

**TLDR**: An adaptive diffusion GNN with temporal regularization is proposed for classifying neurodegenerative diseases from brain network data.

## Abstract

Analysis of neurodegenerative diseases on brain connectomes is important in facilitating early diagnosis and predicting its onset. However, investigation of the progressive and irreversible dynamics of these diseases remains underexplored in cross-sectional studies as its diagnostic groups are considered independent. Also, as in many real-world graphs, brain networks exhibit intricate structures with both homophily and heterophily. To address these challenges, we propose Adaptive Graph diffusion network with Temporal regularization (AGT). AGT introduces node-wise convolution to adaptively capture low (i.e., homophily) and high-frequency (i.e., heterophily) characteristics within an optimally tailored range for each node. Moreover, AGT captures sequential variations within progressive diagnostic groups with a novel temporal regularization, considering the relative feature distance between the groups in the latent space. As a result, our proposed model yields interpretable results at both node-level and group-level. The superiority of our method is validated on two neurodegenerative disease benchmarks for graph classification: Alzheimer’s Disease Neuroimaging Initiative (ADNI) and Parkinson’s Progression Markers Initiative (PPMI) datasets.