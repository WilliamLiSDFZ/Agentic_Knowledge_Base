---
title: "Easing Concept Bleeding in Diffusion via Entity Localization and Anchoring"
source: "https://proceedings.mlr.press/v235/zhang24s.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/zhang24s/zhang24s.pdf"
categories: ['generative-models-and-variational-inference', 'audio-and-music-generation-diffusion-models']
tags: ['diffusion-models', 'concept-bleeding', 'entity-localization']
venue: "ICML 2024"
tldr: "A method to reduce concept bleeding in text-to-image diffusion models via entity localization and anchoring during multi-entity generation."
---

# Easing Concept Bleeding in Diffusion via Entity Localization and Anchoring

**Source**: [https://proceedings.mlr.press/v235/zhang24s.html](https://proceedings.mlr.press/v235/zhang24s.html)

**TLDR**: A method to reduce concept bleeding in text-to-image diffusion models via entity localization and anchoring during multi-entity generation.

## Abstract

Recent diffusion models have manifested extraordinary capabilities in generating high-quality, diverse, and innovative images guided by textual prompts. Nevertheless, these state-of-the-art models may encounter the challenge of concept bleeding when generating images with multiple entities or attributes in the prompt, leading to the unanticipated merging or overlapping of distinct objects in the synthesized result. The current work exploits auxiliary networks to produce mask-constrained regions for entities, necessitating the training of an object detection network. In this paper, we investigate the bleeding reason and find that the cross-attention map associated with a specific entity or attribute tends to extend beyond its intended focus, encompassing the background or other unrelated objects and thereby acting as the primary source of concept bleeding. Motivated by this, we propose Entity Localization and Anchoring (ELA) to drive the entity to concentrate on the expected region accurately during inference, eliminating the necessity for training. Specifically, we initially identify the region corresponding to each entity and subsequently employ a tailored loss function to anchor entities within their designated positioning areas. Extensive experiments demonstrate its superior capability in precisely generating multiple objects as specified in the textual prompts.