---
title: "Graph Generation with Diffusion Mixture"
source: "https://proceedings.mlr.press/v235/jo24b.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/jo24b/jo24b.pdf"
categories: ['generative-models-and-variational-inference', 'graph-neural-networks-and-topology']
tags: ['graph-generation', 'diffusion-models', 'topological-properties', 'mixture']
venue: "ICML 2024"
tldr: "Graph generation via diffusion mixture explicitly models topological properties of graphs by combining multiple diffusion processes tailored to graph structure."
---

# Graph Generation with Diffusion Mixture

**Source**: [https://proceedings.mlr.press/v235/jo24b.html](https://proceedings.mlr.press/v235/jo24b.html)

**TLDR**: Graph generation via diffusion mixture explicitly models topological properties of graphs by combining multiple diffusion processes tailored to graph structure.

## Abstract

Generation of graphs is a major challenge for real-world tasks that require understanding the complex nature of their non-Euclidean structures. Although diffusion models have achieved notable success in graph generation recently, they are ill-suited for modeling the topological properties of graphs since learning to denoise the noisy samples does not explicitly learn the graph structures to be generated. To tackle this limitation, we propose a generative framework that models the topology of graphs by explicitly learning the final graph structures of the diffusion process. Specifically, we design the generative process as a mixture of endpoint-conditioned diffusion processes which is driven toward the predicted graph that results in rapid convergence. We further introduce a simple parameterization of the mixture process and develop an objective for learning the final graph structure, which enables maximum likelihood training. Through extensive experimental validation on general graph and 2D/3D molecule generation tasks, we show that our method outperforms previous generative models, generating graphs with correct topology with both continuous (e.g. 3D coordinates) and discrete (e.g. atom types) features. Our code is available at https://github.com/harryjo97/GruM.