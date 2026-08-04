---
title: "HyperFields: Towards Zero-Shot Generation of NeRFs from Text"
source: "https://proceedings.mlr.press/v235/babu24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/babu24a/babu24a.pdf"
categories: ['generative-models-and-variational-inference', '3d-vision-and-scene-understanding']
tags: ['NeRF', 'text-to-3D', 'hypernetwork', 'zero-shot-generation', 'neural-radiance-fields']
venue: "ICML 2024"
tldr: "Introduces HyperFields, a dynamic hypernetwork enabling zero-shot text-conditioned NeRF generation via a single forward pass."
---

# HyperFields: Towards Zero-Shot Generation of NeRFs from Text

**Source**: [https://proceedings.mlr.press/v235/babu24a.html](https://proceedings.mlr.press/v235/babu24a.html)

**TLDR**: Introduces HyperFields, a dynamic hypernetwork enabling zero-shot text-conditioned NeRF generation via a single forward pass.

## Abstract

We introduce HyperFields, a method for generating text-conditioned Neural Radiance Fields (NeRFs) with a single forward pass and (optionally) some fine-tuning. Key to our approach are: (i) a dynamic hypernetwork, which learns a smooth mapping from text token embeddings to the space of NeRFs; (ii) NeRF distillation training, which distills scenes encoded in individual NeRFs into one dynamic hypernetwork. These techniques enable a single network to fit over a hundred unique scenes. We further demonstrate that HyperFields learns a more general map between text and NeRFs, and consequently is capable of predicting novel in-distribution and out-of-distribution scenes — either zero-shot or with a few finetuning steps. Finetuning HyperFields benefits from accelerated convergence thanks to the learned general map, and is capable of synthesizing novel scenes 5 to 10 times faster than existing neural optimization-based methods. Our ablation experiments show that both the dynamic architecture and NeRF distillation are critical to the expressivity of HyperFields.