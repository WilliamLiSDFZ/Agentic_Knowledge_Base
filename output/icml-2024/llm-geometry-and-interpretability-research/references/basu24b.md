---
title: "On Mechanistic Knowledge Localization in Text-to-Image Generative Models"
source: "https://proceedings.mlr.press/v235/basu24b.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/basu24b/basu24b.pdf"
categories: ['llm-geometry-and-interpretability-research', 'generative-models-and-variational-inference']
tags: ['text-to-image', 'knowledge-localization', 'causal-tracing', 'model-editing', 'diffusion-models']
venue: "ICML 2024"
tldr: "Investigates mechanistic knowledge localization in text-to-image generative models to enable efficient model editing via causal tracing."
---

# On Mechanistic Knowledge Localization in Text-to-Image Generative Models

**Source**: [https://proceedings.mlr.press/v235/basu24b.html](https://proceedings.mlr.press/v235/basu24b.html)

**TLDR**: Investigates mechanistic knowledge localization in text-to-image generative models to enable efficient model editing via causal tracing.

## Abstract

Identifying layers within text-to-image models which control visual attributes can facilitate efficient model editing through closed-form updates. Recent work, leveraging causal tracing show that early Stable-Diffusion variants confine knowledge primarily to the first layer of the CLIP text-encoder, while it diffuses throughout the UNet. Extending this framework, we observe that for recent models (e.g., SD-XL, DeepFloyd), causal tracing fails in pinpointing localized knowledge, highlighting challenges in model editing. To address this issue, we introduce the concept of mechanistic localization in text-to-image models, where knowledge about various visual attributes (e.g., "style", "objects", "facts") can be mechanistically localized to a small fraction of layers in the UNet, thus facilitating efficient model editing. We localize knowledge using our method LocoGen which measures the direct effect of intermediate layers to output generation by performing interventions in the cross-attention layers of the UNet. We then employ LocoEdit, a fast closed-form editing method across popular open-source text-to-image models (including the latest SD-XL) and explore the possibilities of neuron-level model editing. Using mechanistic localization, our work offers a better view of successes and failures in localization-based text-to-image model editing.