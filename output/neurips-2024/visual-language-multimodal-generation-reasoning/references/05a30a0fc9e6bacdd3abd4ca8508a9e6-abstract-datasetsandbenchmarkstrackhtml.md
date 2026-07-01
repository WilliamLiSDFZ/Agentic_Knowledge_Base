---
title: "UltraEdit: Instruction-based Fine-Grained Image Editing at Scale"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/05a30a0fc9e6bacdd3abd4ca8508a9e6-Abstract-Datasets_and_Benchmarks_Track.html"
categories: ['visual-language-multimodal-generation-reasoning', 'generative-models-for-visual-style-and-appearance']
tags: ['image-editing', 'instruction-based', 'large-scale-dataset']
venue: "NeurIPS 2024"
tldr: "UltraEdit is a large-scale automatically generated dataset of ~4M samples for fine-grained instruction-based image editing."
---

# UltraEdit: Instruction-based Fine-Grained Image Editing at Scale

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/05a30a0fc9e6bacdd3abd4ca8508a9e6-Abstract-Datasets_and_Benchmarks_Track.html](https://papers.nips.cc/paper_files/paper/2024/hash/05a30a0fc9e6bacdd3abd4ca8508a9e6-Abstract-Datasets_and_Benchmarks_Track.html)

**TLDR**: UltraEdit is a large-scale automatically generated dataset of ~4M samples for fine-grained instruction-based image editing.

## Abstract

This paper presents UltraEdit, a large-scale (~ 4M editing samples), automatically generated dataset for instruction-based image editing. Our key idea is to address the drawbacks in existing image editing datasets like InstructPix2Pix and MagicBrush, and provide a systematic approach to producing massive and high-quality image editing samples: 1) UltraEdit includes more diverse editing instructions by combining LLM creativity and in-context editing examples by human raters; 2) UltraEdit is anchored on real images (photographs or artworks), which offers more diversity and less biases than those purely synthesized by text-to-image models; 3) UltraEdit supports region-based editing with high-quality, automatically produced region annotations. Our experiments show that canonical diffusion-based editing baselines trained on UltraEdit set new records on challenging MagicBrush and Emu-Edit benchmarks, respectively. Our analysis further confirms the crucial role of real image anchors and region-based editing data. The dataset, code, and models will be made public.