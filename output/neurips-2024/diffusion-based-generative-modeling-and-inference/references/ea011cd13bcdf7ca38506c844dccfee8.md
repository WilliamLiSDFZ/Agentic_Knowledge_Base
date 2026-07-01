---
title: "$\textit{Bifr\'ost}$: 3D-Aware Image Compositing with Language Instructions"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/ea011cd13bcdf7ca38506c844dccfee8-Abstract-Conference.html"
categories: ['diffusion-based-generative-modeling-and-inference', 'visual-language-multimodal-generation-reasoning']
tags: ['image-compositing', '3D-aware', 'diffusion-models', 'language-instructions', 'spatial-reasoning']
venue: "NeurIPS 2024"
tldr: "Bifröst is a 3D-aware diffusion-based framework for instruction-guided image compositing that handles complex spatial relationships."
---

# $\textit{Bifr\"ost}$: 3D-Aware Image Compositing with Language Instructions

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/ea011cd13bcdf7ca38506c844dccfee8-Abstract-Conference.html](https://papers.nips.cc/paper_files/paper/2024/hash/ea011cd13bcdf7ca38506c844dccfee8-Abstract-Conference.html)

**TLDR**: Bifröst is a 3D-aware diffusion-based framework for instruction-guided image compositing that handles complex spatial relationships.

## Abstract

This paper introduces $\textit{Bifröst}$, a novel 3D-aware framework that is built upon diffusion models to perform instruction-based image composition. Previous methods concentrate on image compositing at the 2D level, which fall short in handling complex spatial relationships ($\textit{e.g.}$, occlusion). $\textit{Bifröst}$ addresses these issues by training MLLM as a 2.5D location predictor and integrating depth maps as an extra condition during the generation process to bridge the gap between 2D and 3D, which enhances spatial comprehension and supports sophisticated spatial interactions. Our method begins by fine-tuning MLLM with a custom counterfactual dataset to predict 2.5D object locations in complex backgrounds from language instructions. Then, the image-compositing model is uniquely designed to process multiple types of input features, enabling it to perform high-fidelity image compositions that consider occlusion, depth blur, and image harmonization. Extensive qualitative and quantitative evaluations demonstrate that $\textit{Bifröst}$ significantly outperforms existing methods, providing a robust solution for generating realistically composited images in scenarios demanding intricate spatial understanding. This work not only pushes the boundaries of generative image compositing but also reduces reliance on expensive annotated datasets by effectively utilizing existing resources in innovative ways.