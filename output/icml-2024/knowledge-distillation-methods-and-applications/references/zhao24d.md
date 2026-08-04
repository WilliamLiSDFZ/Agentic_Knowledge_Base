---
title: "Image Fusion via Vision-Language Model"
source: "https://proceedings.mlr.press/v235/zhao24d.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/zhao24d/zhao24d.pdf"
categories: ['generative-models-and-variational-inference', 'knowledge-distillation-methods-and-applications']
tags: ['image-fusion', 'vision-language-model', 'semantic-features']
venue: "ICML 2024"
tldr: "Leverages vision-language models to incorporate text-level semantics into image fusion for enhanced quality."
---

# Image Fusion via Vision-Language Model

**Source**: [https://proceedings.mlr.press/v235/zhao24d.html](https://proceedings.mlr.press/v235/zhao24d.html)

**TLDR**: Leverages vision-language models to incorporate text-level semantics into image fusion for enhanced quality.

## Abstract

Image fusion integrates essential information from multiple images into a single composite, enhancing structures, textures, and refining imperfections. Existing methods predominantly focus on pixel-level and semantic visual features for recognition, but often overlook the deeper text-level semantic information beyond vision. Therefore, we introduce a novel fusion paradigm named image Fusion via vIsion-Language Model (FILM), for the first time, utilizing explicit textual information from source images to guide the fusion process. Specifically, FILM generates semantic prompts from images and inputs them into ChatGPT for comprehensive textual descriptions. These descriptions are fused within the textual domain and guide the visual information fusion, enhancing feature extraction and contextual understanding, directed by textual semantic information via cross-attention. FILM has shown promising results in four image fusion tasks: infrared-visible, medical, multi-exposure, and multi-focus image fusion. We also propose a vision-language dataset containing ChatGPT-generated paragraph descriptions for the eight image fusion datasets across four fusion tasks, facilitating future research in vision-language model-based image fusion. Code and dataset are available at https://github.com/Zhaozixiang1228/IF-FILM.