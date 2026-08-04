---
title: "Editing Partially Observable Networks via Graph Diffusion Models"
source: "https://proceedings.mlr.press/v235/trivedi24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/trivedi24a/trivedi24a.pdf"
categories: ['graph-neural-networks-and-topology', 'generative-models-and-variational-inference']
tags: ['graph-diffusion', 'network-completion', 'graph-generation']
venue: "ICML 2024"
tldr: "Uses graph diffusion models to edit and refine partially observable networks by correcting corruptions and inferring unobserved regions."
---

# Editing Partially Observable Networks via Graph Diffusion Models

**Source**: [https://proceedings.mlr.press/v235/trivedi24a.html](https://proceedings.mlr.press/v235/trivedi24a.html)

**TLDR**: Uses graph diffusion models to edit and refine partially observable networks by correcting corruptions and inferring unobserved regions.

## Abstract

Most real-world networks are noisy and incomplete samples from an unknown target distribution. Refining them by correcting corruptions or inferring unobserved regions typically improves downstream performance. Inspired by the impressive generative capabilities that have been used to correct corruptions in images, and the similarities between "in-painting" and filling in missing nodes and edges conditioned on the observed graph, we propose a novel graph generative framework, SGDM, which is based on subgraph diffusion. Our framework not only improves the scalability and fidelity of graph diffusion models, but also leverages the reverse process to perform novel, conditional generation tasks. In particular, through extensive empirical analysis and a set of novel metrics, we demonstrate that our proposed model effectively supports the following refinement tasks for partially observable networks: (T1) denoising extraneous subgraphs, (T2) expanding existing subgraphs and (T3) performing “style" transfer by regenerating a particular subgraph to match the characteristics of a different node or subgraph.