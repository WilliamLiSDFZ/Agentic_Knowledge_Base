---
title: "Compositional Image Decomposition with Diffusion Models"
source: "https://proceedings.mlr.press/v235/su24c.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/su24c/su24c.pdf"
categories: ['generative-models-and-variational-inference', '3d-vision-and-scene-understanding']
tags: ['image-decomposition', 'diffusion-models', 'compositional-generation', 'scene-understanding', 'components']
venue: "ICML 2024"
tldr: "A diffusion-model-based framework decomposes natural images into compositional components such as objects, lighting, and shadows for cross-image recombination."
---

# Compositional Image Decomposition with Diffusion Models

**Source**: [https://proceedings.mlr.press/v235/su24c.html](https://proceedings.mlr.press/v235/su24c.html)

**TLDR**: A diffusion-model-based framework decomposes natural images into compositional components such as objects, lighting, and shadows for cross-image recombination.

## Abstract

Given an image of a natural scene, we are able to quickly decompose it into a set of components such as objects, lighting, shadows, and foreground. We can then envision a scene where we combine certain components with those from other images, for instance a set of objects from our bedroom and animals from a zoo under the lighting conditions of a forest, even if we have never encountered such a scene before. In this paper, we present a method to decompose an image into such compositional components. Our approach, Decomp Diffusion, is an unsupervised method which, when given a single image, infers a set of different components in the image, each represented by a diffusion model. We demonstrate how components can capture different factors of the scene, ranging from global scene descriptors like shadows or facial expression to local scene descriptors like constituent objects. We further illustrate how inferred factors can be flexibly composed, even with factors inferred from other models, to generate a variety of scenes sharply different than those seen in training time. Code and visualizations are at https://energy-based-model.github.io/decomp-diffusion.