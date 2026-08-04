---
title: "Swallowing the Bitter Pill: Simplified Scalable Conformer Generation"
source: "https://proceedings.mlr.press/v235/wang24q.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/wang24q/wang24q.pdf"
categories: ['generative-models-for-molecular-protein-design', 'generative-models-and-variational-inference']
tags: ['molecular-conformer-generation', 'diffusion-models', '3D-molecular-geometry', 'scalable', 'generative-models']
venue: "ICML 2024"
tldr: "A simplified diffusion model trained directly on 3D atomic positions achieves state-of-the-art molecular conformer generation through scale."
---

# Swallowing the Bitter Pill: Simplified Scalable Conformer Generation

**Source**: [https://proceedings.mlr.press/v235/wang24q.html](https://proceedings.mlr.press/v235/wang24q.html)

**TLDR**: A simplified diffusion model trained directly on 3D atomic positions achieves state-of-the-art molecular conformer generation through scale.

## Abstract

We present a novel way to predict molecular conformers through a simple formulation that sidesteps many of the heuristics of prior works and achieves state of the art results by using the advantages of scale. By training a diffusion generative model directly on 3D atomic positions without making assumptions about the explicit structure of molecules (e.g. modeling torsional angles) we are able to radically simplify structure learning, and make it trivial to scale up the model sizes. This model, called Molecular Conformer Fields (MCF), works by parameterizing conformer structures as functions that map elements from a molecular graph directly to their 3D location in space. This formulation allows us to boil down the essence of structure prediction to learning a distribution over functions. Experimental results show that scaling up the model capacity leads to large gains in generalization performance without enforcing inductive biases like rotational equivariance. MCF represents an advance in extending diffusion models to handle complex scientific problems in a conceptually simple, scalable and effective manner.