---
title: "Learning Latent Space Hierarchical EBM Diffusion Models"
source: "https://proceedings.mlr.press/v235/cui24b.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/cui24b/cui24b.pdf"
categories: ['generative-models-and-variational-inference', 'probabilistic-generating-circuits-research']
tags: ['energy-based-models', 'hierarchical-generative-models', 'diffusion']
venue: "ICML 2024"
tldr: "Studies joint learning of energy-based prior models and multi-layer hierarchical generators via latent space EBM diffusion models."
---

# Learning Latent Space Hierarchical EBM Diffusion Models

**Source**: [https://proceedings.mlr.press/v235/cui24b.html](https://proceedings.mlr.press/v235/cui24b.html)

**TLDR**: Studies joint learning of energy-based prior models and multi-layer hierarchical generators via latent space EBM diffusion models.

## Abstract

This work studies the learning problem of the energy-based prior model and the multi-layer generator model. The multi-layer generator model, which contains multiple layers of latent variables organized in a top-down hierarchical structure, typically assumes the Gaussian prior model. Such a prior model can be limited in modelling expressivity, which results in a gap between the generator posterior and the prior model, known as the prior hole problem. Recent works have explored learning the energy-based (EBM) prior model as a second-stage, complementary model to bridge the gap. However, the EBM defined on a multi-layer latent space can be highly multi-modal, which makes sampling from such marginal EBM prior challenging in practice, resulting in ineffectively learned EBM. To tackle the challenge, we propose to leverage the diffusion probabilistic scheme to mitigate the burden of EBM sampling and thus facilitate EBM learning. Our extensive experiments demonstrate a superior performance of our diffusion-learned EBM prior on various challenging tasks.