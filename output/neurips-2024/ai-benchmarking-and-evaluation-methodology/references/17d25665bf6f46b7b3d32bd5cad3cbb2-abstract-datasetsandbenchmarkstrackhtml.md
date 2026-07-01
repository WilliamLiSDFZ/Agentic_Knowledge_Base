---
title: "BLURD: Benchmarking and Learning using a Unified Rendering and Diffusion Model"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/17d25665bf6f46b7b3d32bd5cad3cbb2-Abstract-Datasets_and_Benchmarks_Track.html"
categories: ['ai-benchmarking-and-evaluation-methodology', 'diffusion-based-generative-modeling-and-inference']
tags: ['benchmarking', 'diffusion-models', 'vision-evaluation']
venue: "NeurIPS 2024"
tldr: "A unified rendering and diffusion-based framework for benchmarking pre-trained vision models across diverse factors of variation."
---

# BLURD: Benchmarking and Learning using a Unified Rendering and Diffusion Model

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/17d25665bf6f46b7b3d32bd5cad3cbb2-Abstract-Datasets_and_Benchmarks_Track.html](https://papers.nips.cc/paper_files/paper/2024/hash/17d25665bf6f46b7b3d32bd5cad3cbb2-Abstract-Datasets_and_Benchmarks_Track.html)

**TLDR**: A unified rendering and diffusion-based framework for benchmarking pre-trained vision models across diverse factors of variation.

## Abstract

Recent advancements in pre-trained vision models have made them pivotal in computer vision, emphasizing the need for their thorough evaluation and benchmarking. This evaluation needs to consider various factors of variation, their potential biases, shortcuts, and inaccuracies that ultimately lead to disparate performance in models. Such evaluations are conventionally done using either synthetic data from 2D or 3D rendering software or real-world images in controlled settings. Synthetic methods offer full control and flexibility, while real-world methods are limited by high costs and less adaptability. Moreover, 3D rendering can't yet fully replicate real photography, creating a realism gap.In this paper, we introduce BLURD--Benchmarking and Learning using a Unified Rendering and Diffusion Model--a novel method combining 3D rendering and Stable Diffusion to bridge this gap in representation learning. With BLURD we create a new family of datasets that allow for the creation of both 3D rendered and photo-realistic images with identical factors. BLURD, therefore, provides deeper insights into the representations learned by various CLIP backbones. The source code for creating the BLURD datasets is available at https://github.com/squaringTheCircle/BLURD