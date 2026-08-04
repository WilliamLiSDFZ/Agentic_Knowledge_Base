---
title: "Completing Visual Objects via Bridging Generation and Segmentation"
source: "https://proceedings.mlr.press/v235/li24j.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/li24j/li24j.pdf"
categories: ['3d-vision-and-scene-understanding', 'generative-models-and-variational-inference']
tags: ['object-completion', 'segmentation', 'generation', 'iterative', 'partial-occlusion']
venue: "ICML 2024"
tldr: "Presents MaskComp, an iterative method that bridges generation and segmentation to reconstruct complete objects from partially visible inputs."
---

# Completing Visual Objects via Bridging Generation and Segmentation

**Source**: [https://proceedings.mlr.press/v235/li24j.html](https://proceedings.mlr.press/v235/li24j.html)

**TLDR**: Presents MaskComp, an iterative method that bridges generation and segmentation to reconstruct complete objects from partially visible inputs.

## Abstract

This paper presents a novel approach to object completion, with the primary goal of reconstructing a complete object from its partially visible components. Our method, named MaskComp, delineates the completion process through iterative stages of generation and segmentation. In each iteration, the object mask is provided as an additional condition to boost image generation, and, in return, the generated images can lead to a more accurate mask by fusing the segmentation of images. We demonstrate that the combination of one generation and one segmentation stage effectively functions as a mask denoiser. Through alternation between the generation and segmentation stages, the partial object mask is progressively refined, providing precise shape guidance and yielding superior object completion results. Our experiments demonstrate the superiority of MaskComp over existing approaches, e.g., ControlNet and Stable Diffusion, establishing it as an effective solution for object completion.