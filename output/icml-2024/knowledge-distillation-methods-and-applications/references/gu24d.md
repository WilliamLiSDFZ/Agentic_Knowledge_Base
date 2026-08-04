---
title: "Data-free Distillation of Diffusion Models with Bootstrapping"
source: "https://proceedings.mlr.press/v235/gu24d.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/gu24d/gu24d.pdf"
categories: ['generative-models-and-variational-inference', 'knowledge-distillation-methods-and-applications']
tags: ['diffusion-distillation', 'data-free', 'bootstrapping']
venue: "ICML 2024"
tldr: "This paper proposes a data-free knowledge distillation method for diffusion models using bootstrapping to accelerate inference without requiring original training data."
---

# Data-free Distillation of Diffusion Models with Bootstrapping

**Source**: [https://proceedings.mlr.press/v235/gu24d.html](https://proceedings.mlr.press/v235/gu24d.html)

**TLDR**: This paper proposes a data-free knowledge distillation method for diffusion models using bootstrapping to accelerate inference without requiring original training data.

## Abstract

Diffusion models have demonstrated great potential for generating diverse images. However, their performance often suffers from slow generation due to iterative denoising. Knowledge distillation has been recently proposed as a remedy which can reduce the number of inference steps to one or a few, without significant quality degradation. However, existing distillation methods either require significant amounts of offline computation for generating synthetic training data from the teacher model, or need to perform expensive online learning with the help of real data. In this work, we present a novel technique called BOOT, that overcomes these limitations with an efficient data-free distillation algorithm. The core idea is to learn a time-conditioned model that predicts the output of a pre-trained diffusion model teacher given any time-step. Such a model can be efficiently trained based on bootstrapping from two consecutive sampled steps. Furthermore, our method can be easily adapted to large-scale text-to-image diffusion models, which are challenging for previous methods given the fact that the training sets are often large and difficult to access. We demonstrate the effectiveness of our approach on several benchmark datasets in the DDIM setting, achieving comparable generation quality while being orders of magnitude faster than the diffusion teacher. The text-to-image results show that the proposed approach is able to handle highly complex distributions, shedding light on more efficient generative modeling.