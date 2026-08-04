---
title: "Counterfactual Image Editing"
source: "https://proceedings.mlr.press/v235/pan24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/pan24a/pan24a.pdf"
categories: ['causal-inference-and-discovery-methods']
tags: ['counterfactual-image-editing', 'causal-inference', 'generative-models', 'causal-features']
venue: "ICML 2024"
tldr: "Formalizes counterfactual image editing with causal relationships between features for more faithful image generation."
---

# Counterfactual Image Editing

**Source**: [https://proceedings.mlr.press/v235/pan24a.html](https://proceedings.mlr.press/v235/pan24a.html)

**TLDR**: Formalizes counterfactual image editing with causal relationships between features for more faithful image generation.

## Abstract

Counterfactual image editing is a challenging task within generative AI. The current literature on the topic focuses primarily on changing individual features while being silent about the causal relationships between features, which are present in the real world. In this paper, we first formalize this task through causal language, modeling the causal relationships between latent generative factors and images through a special type of causal model called augmented structural causal models (ASCMs). Second, we show two fundamental impossibility results: (1) counterfactual editing is impossible from i.i.d. image samples and their corresponding labels alone; (2) also, even when the causal relationships between latent generative factors and images are available, no guarantees regarding the output of the generative model can be provided. Third, we propose a relaxation over this hard problem aiming to approximate the non-identifiable target counterfactual distributions while still preserving features the users care about and that are causally consistent with the true generative model, which we call ctf-consistent estimators. Finally, we develop an efficient algorithm to generate counterfactual image samples leveraging neural causal models.