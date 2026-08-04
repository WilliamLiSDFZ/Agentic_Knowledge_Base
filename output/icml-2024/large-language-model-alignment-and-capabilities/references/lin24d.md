---
title: "Non-confusing Generation of Customized Concepts in Diffusion Models"
source: "https://proceedings.mlr.press/v235/lin24d.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/lin24d/lin24d.pdf"
categories: ['generative-models-and-variational-inference', 'large-language-model-alignment-and-capabilities']
tags: ['diffusion-models', 'concept-customization', 'compositional-generation']
venue: "ICML 2024"
tldr: "A method to reduce inter-concept visual confusion in compositional customized concept generation using text-guided diffusion models."
---

# Non-confusing Generation of Customized Concepts in Diffusion Models

**Source**: [https://proceedings.mlr.press/v235/lin24d.html](https://proceedings.mlr.press/v235/lin24d.html)

**TLDR**: A method to reduce inter-concept visual confusion in compositional customized concept generation using text-guided diffusion models.

## Abstract

We tackle the common challenge of inter-concept visual confusion in compositional concept generation using text-guided diffusion models (TGDMs). It becomes even more pronounced in the generation of customized concepts, due to the scarcity of user-provided concept visual examples. By revisiting the two major stages leading to the success of TGDMs—1) contrastive image-language pre-training (CLIP) for text encoder that encodes visual semantics, and 2) training TGDM that decodes the textual embeddings into pixels—we point that existing customized generation methods only focus on fine-tuning the second stage while overlooking the first one. To this end, we propose a simple yet effective solution called CLIF: contrastive image-language fine-tuning. Specifically, given a few samples of customized concepts, we obtain non-confusing textual embeddings of a concept by fine-tuning CLIP via contrasting a concept and the over-segmented visual regions of other concepts. Experimental results demonstrate the effectiveness of CLIF in preventing the confusion of multi-customized concept generation. Project page: https://clif-official.github.io/clif.