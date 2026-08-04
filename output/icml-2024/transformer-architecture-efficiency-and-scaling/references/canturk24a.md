---
title: "Graph Positional and Structural Encoder"
source: "https://proceedings.mlr.press/v235/canturk24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/canturk24a/canturk24a.pdf"
categories: ['graph-neural-networks-and-topology', 'transformer-architecture-efficiency-and-scaling']
tags: ['positional-encoding', 'structural-encoding', 'graph-transformers', 'GNN']
venue: "ICML 2024"
tldr: "Introduces a learnable graph positional and structural encoder that adaptively combines multiple encodings for diverse graph prediction tasks."
---

# Graph Positional and Structural Encoder

**Source**: [https://proceedings.mlr.press/v235/canturk24a.html](https://proceedings.mlr.press/v235/canturk24a.html)

**TLDR**: Introduces a learnable graph positional and structural encoder that adaptively combines multiple encodings for diverse graph prediction tasks.

## Abstract

Positional and structural encodings (PSE) enable better identifiability of nodes within a graph, rendering them essential tools for empowering modern GNNs, and in particular graph Transformers. However, designing PSEs that work optimally for all graph prediction tasks is a challenging and unsolved problem. Here, we present the Graph Positional and Structural Encoder (GPSE), the first-ever graph encoder designed to capture rich PSE representations for augmenting any GNN. GPSE learns an efficient common latent representation for multiple PSEs, and is highly transferable: The encoder trained on a particular graph dataset can be used effectively on datasets drawn from markedly different distributions and modalities. We show that across a wide range of benchmarks, GPSE-enhanced models can significantly outperform those that employ explicitly computed PSEs, and at least match their performance in others. Our results pave the way for the development of foundational pre-trained graph encoders for extracting positional and structural information, and highlight their potential as a more powerful and efficient alternative to explicitly computed PSEs and existing self-supervised pre-training approaches. Our framework and pre-trained models are publicly available at https://github.com/G-Taxonomy-Workgroup/GPSE. For convenience, GPSE has also been integrated into the PyG library to facilitate downstream applications.