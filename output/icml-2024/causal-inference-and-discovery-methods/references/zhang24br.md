---
title: "Causal Representation Learning from Multiple Distributions: A General Setting"
source: "https://proceedings.mlr.press/v235/zhang24br.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/zhang24br/zhang24br.pdf"
categories: ['causal-inference-and-discovery-methods', 'generative-models-and-variational-inference']
tags: ['causal-representation-learning', 'latent-variables', 'distribution-shift', 'identifiability', 'multiple-distributions']
venue: "ICML 2024"
tldr: "Establishes a general framework for causal representation learning from multiple distributions with latent causal variables."
---

# Causal Representation Learning from Multiple Distributions: A General Setting

**Source**: [https://proceedings.mlr.press/v235/zhang24br.html](https://proceedings.mlr.press/v235/zhang24br.html)

**TLDR**: Establishes a general framework for causal representation learning from multiple distributions with latent causal variables.

## Abstract

In many problems, the measured variables (e.g., image pixels) are just mathematical functions of the latent causal variables (e.g., the underlying concepts or objects). For the purpose of making predictions in changing environments or making proper changes to the system, it is helpful to recover the latent causal variables $Z_i$ and their causal relations represented by graph $\mathcal{G}_Z$. This problem has recently been known as causal representation learning. This paper is concerned with a general, completely nonparametric setting of causal representation learning from multiple distributions (arising from heterogeneous data or nonstationary time series), without assuming hard interventions behind distribution changes. We aim to develop general solutions in this fundamental case; as a by product, this helps see the unique benefit offered by other assumptions such as parametric causal models or hard interventions. We show that under the sparsity constraint on the recovered graph over the latent variables and suitable sufficient change conditions on the causal influences, interestingly, one can recover the moralized graph of the underlying directed acyclic graph, and the recovered latent variables and their relations are related to the underlying causal model in a specific, nontrivial way. In some cases, most latent variables can even be recovered up to component-wise transformations. Experimental results verify our theoretical claims.