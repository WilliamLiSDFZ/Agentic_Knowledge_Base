---
title: "DiMSUM: Diffusion Mamba - A Scalable and Unified Spatial-Frequency Method for Image Generation"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/39bc6e3cbf5a1991d33dc10ebff9a9cf-Abstract-Conference.html"
categories: ['diffusion-based-generative-modeling-and-inference', 'llm-training-and-optimization-techniques']
tags: ['diffusion-models', 'mamba', 'spatial-frequency']
venue: "NeurIPS 2024"
tldr: "DiMSUM is a state-space diffusion architecture that fuses spatial and frequency information using Mamba blocks to improve image generation with strong local feature inductive bias."
---

# DiMSUM: Diffusion Mamba - A Scalable and Unified Spatial-Frequency Method for Image Generation

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/39bc6e3cbf5a1991d33dc10ebff9a9cf-Abstract-Conference.html](https://papers.nips.cc/paper_files/paper/2024/hash/39bc6e3cbf5a1991d33dc10ebff9a9cf-Abstract-Conference.html)

**TLDR**: DiMSUM is a state-space diffusion architecture that fuses spatial and frequency information using Mamba blocks to improve image generation with strong local feature inductive bias.

## Abstract

We introduce a novel state-space architecture for diffusion models, effectively harnessing spatial and frequency information to enhance the inductive bias towards local features in input images for image generation tasks. While state-space networks, including Mamba, a revolutionary advancement in recurrent neural networks, typically scan input sequences from left to right, they face difficulties in designing effective scanning strategies, especially in the processing of image data. Our method demonstrates that integrating wavelet transformation into Mamba enhances the local structure awareness of visual inputs and better captures long-range relations of frequencies by disentangling them into wavelet subbands, representing both low- and high-frequency components. These wavelet-based outputs are then processed and seamlessly fused with the original Mamba outputs through a cross-attention fusion layer, combining both spatial and frequency information to optimize the order awareness of state-space models which is essential for the details and overall quality of image generation. Besides, we introduce a globally-shared transformer to supercharge the performance of Mamba, harnessing its exceptional power to capture global relationships. Through extensive experiments on standard benchmarks, our method demonstrates superior results compared to DiT and DIFFUSSM, achieving faster training convergence and delivering high-quality outputs. The codes and pretrained models are released at https://github.com/VinAIResearch/DiMSUM.git.