---
title: "Disentangled 3D Scene Generation with Layout Learning"
source: "https://proceedings.mlr.press/v235/epstein24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/epstein24a/epstein24a.pdf"
categories: ['3d-vision-and-scene-understanding', 'generative-models-and-variational-inference']
tags: ['3d-scene-generation', 'disentanglement', 'text-to-image', 'object-discovery', 'scene-decomposition']
venue: "ICML 2024"
tldr: "Proposes an unsupervised method to generate 3D scenes disentangled into component objects by leveraging a pretrained text-to-image model."
---

# Disentangled 3D Scene Generation with Layout Learning

**Source**: [https://proceedings.mlr.press/v235/epstein24a.html](https://proceedings.mlr.press/v235/epstein24a.html)

**TLDR**: Proposes an unsupervised method to generate 3D scenes disentangled into component objects by leveraging a pretrained text-to-image model.

## Abstract

We introduce a method to generate 3D scenes that are disentangled into their component objects. This disentanglement is unsupervised, relying only on the knowledge of a large pretrained text-to-image model. Our key insight is that objects can be discovered by finding parts of a 3D scene that, when rearranged spatially, still produce valid configurations of the same scene. Concretely, our method jointly optimizes multiple NeRFs—each representing its own object—along with a set of layouts that composite these objects into scenes. We then encourage these composited scenes to be in-distribution according to the image generator. We show that despite its simplicity, our approach successfully generates 3D scenes decomposed into individual objects, enabling new capabilities in text-to-3D content creation.