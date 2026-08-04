---
title: "Leveraging VLM-Based Pipelines to Annotate 3D Objects"
source: "https://proceedings.mlr.press/v235/kabra24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/kabra24a/kabra24a.pdf"
categories: ['3d-vision-and-scene-understanding', 'large-language-model-alignment-and-capabilities']
tags: ['vision-language-models', '3D-objects', 'annotation', 'captioning']
venue: "ICML 2024"
tldr: "Leverages VLM-based pipelines with multi-view aggregation to automatically annotate 3D objects at scale without GPT-4."
---

# Leveraging VLM-Based Pipelines to Annotate 3D Objects

**Source**: [https://proceedings.mlr.press/v235/kabra24a.html](https://proceedings.mlr.press/v235/kabra24a.html)

**TLDR**: Leverages VLM-based pipelines with multi-view aggregation to automatically annotate 3D objects at scale without GPT-4.

## Abstract

Pretrained vision language models (VLMs) present an opportunity to caption unlabeled 3D objects at scale. The leading approach to summarize VLM descriptions from different views of an object (Luo et al., 2023) relies on a language model (GPT4) to produce the final output. This text-based aggregation is susceptible to hallucinations as it merges potentially contradictory descriptions. We propose an alternative algorithm to marginalize over factors such as the viewpoint that affect the VLM’s response. Instead of merging text-only responses, we utilize the VLM’s joint image-text likelihoods. We show our probabilistic aggregation is not only more reliable and efficient, but sets the SoTA on inferring object types with respect to human-verified labels. The aggregated annotations are also useful for conditional inference; they improve downstream predictions (e.g., of object material) when the object’s type is specified as an auxiliary text-based input. Such auxiliary inputs allow ablating the contribution of visual reasoning over visionless reasoning in an unsupervised setting. With these supervised and unsupervised evaluations, we show how a VLM-based pipeline can be leveraged to produce reliable annotations for 764K objects from the Objaverse dataset.