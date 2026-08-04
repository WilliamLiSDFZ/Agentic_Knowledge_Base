---
title: "Diffuse, Sample, Project: Plug-And-Play Controllable Graph Generation"
source: "https://proceedings.mlr.press/v235/sharma24b.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/sharma24b/sharma24b.pdf"
categories: ['generative-models-and-variational-inference', 'graph-neural-networks-and-topology']
tags: ['graph-generation', 'diffusion-models', 'hard-constraints']
venue: "ICML 2024"
tldr: "A plug-and-play framework called Diffuse-Sample-Project is introduced for controllable graph generation that handles hard constraints via projection during diffusion sampling."
---

# Diffuse, Sample, Project: Plug-And-Play Controllable Graph Generation

**Source**: [https://proceedings.mlr.press/v235/sharma24b.html](https://proceedings.mlr.press/v235/sharma24b.html)

**TLDR**: A plug-and-play framework called Diffuse-Sample-Project is introduced for controllable graph generation that handles hard constraints via projection during diffusion sampling.

## Abstract

Diffusion models lend transformative capabilities to the graph generation task, yet controlling the properties of the generated graphs remains challenging. Recent approaches augment support for controlling soft, differentiable properties but they fail to handle user-specified hard constraints that are non-differentiable. This often results in vague control, unsuitable for applications like drug discovery that demand satisfaction of precise constraints, e.g., the maximum number of bonds. To address this, we formalize the problem of controlled graph generation and introduce PRODIGY (PROjected DIffusion for controlled Graph Generation), an innovative plug-and-play approach enabling the generation of graphs with precise control, from any pre-trained diffusion model. PRODIGY employs a novel operator to project the samples at each diffusion step onto the specified constrained space. For a large class of practical constraints and a variety of graphs, our extensive experiments demonstrate that PRODIGY empowers state-of-the-art continuous and discrete diffusion models to produce graphs meeting specific, hard constraints. Our approach achieves up to 100% constraint satisfaction for non-attributed and molecular graphs, under a variety of constraints, marking a significant step forward in precise, interpretable graph generation. Code is provided on the project webpage: https://prodigy-diffusion.github.io/.