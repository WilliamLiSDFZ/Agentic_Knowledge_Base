---
title: "Score identity Distillation: Exponentially Fast Distillation of Pretrained Diffusion Models for One-Step Generation"
source: "https://proceedings.mlr.press/v235/zhou24x.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/zhou24x/zhou24x.pdf"
categories: ['generative-models-and-variational-inference', 'knowledge-distillation-methods-and-applications']
tags: ['diffusion-distillation', 'one-step-generation', 'score-matching']
venue: "ICML 2024"
tldr: "Introduces Score identity Distillation (SiD), a data-free method that distills pretrained diffusion models into a single-step generator with exponentially fast FID reduction."
---

# Score identity Distillation: Exponentially Fast Distillation of Pretrained Diffusion Models for One-Step Generation

**Source**: [https://proceedings.mlr.press/v235/zhou24x.html](https://proceedings.mlr.press/v235/zhou24x.html)

**TLDR**: Introduces Score identity Distillation (SiD), a data-free method that distills pretrained diffusion models into a single-step generator with exponentially fast FID reduction.

## Abstract

We introduce Score identity Distillation (SiD), an innovative data-free method that distills the generative capabilities of pretrained diffusion models into a single-step generator. SiD not only facilitates an exponentially fast reduction in Fréchet inception distance (FID) during distillation but also approaches or even exceeds the FID performance of the original teacher diffusion models. By reformulating forward diffusion processes as semi-implicit distributions, we leverage three score-related identities to create an innovative loss mechanism. This mechanism achieves rapid FID reduction by training the generator using its own synthesized images, eliminating the need for real data or reverse-diffusion-based generation, all accomplished within significantly shortened generation time. Upon evaluation across four benchmark datasets, the SiD algorithm demonstrates high iteration efficiency during distillation and surpasses competing distillation approaches, whether they are one-step or few-step, data-free, or dependent on training data, in terms of generation quality. This achievement not only redefines the benchmarks for efficiency and effectiveness in diffusion distillation but also in the broader field of diffusion-based generation. The PyTorch implementation is available at https://github.com/mingyuanzhou/SiD.