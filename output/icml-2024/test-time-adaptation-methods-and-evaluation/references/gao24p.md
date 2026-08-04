---
title: "Fast-Slow Test-Time Adaptation for Online Vision-and-Language Navigation"
source: "https://proceedings.mlr.press/v235/gao24p.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/gao24p/gao24p.pdf"
categories: ['test-time-adaptation-methods-and-evaluation', 'large-language-model-alignment-and-capabilities']
tags: ['test-time-adaptation', 'vision-and-language-navigation', 'online-learning', 'embodied-AI']
venue: "ICML 2024"
tldr: "A fast-slow test-time adaptation method improves online vision-and-language navigation by leveraging unlabeled test observations during deployment."
---

# Fast-Slow Test-Time Adaptation for Online Vision-and-Language Navigation

**Source**: [https://proceedings.mlr.press/v235/gao24p.html](https://proceedings.mlr.press/v235/gao24p.html)

**TLDR**: A fast-slow test-time adaptation method improves online vision-and-language navigation by leveraging unlabeled test observations during deployment.

## Abstract

The ability to accurately comprehend natural language instructions and navigate to the target location is essential for an embodied agent. Such agents are typically required to execute user instructions in an online manner, leading us to explore the use of unlabeled test samples for effective online model adaptation. However, for online Vision-and-Language Navigation (VLN), due to the intrinsic nature of inter-sample online instruction execution and intra-sample multi-step action decision, frequent updates can result in drastic changes in model parameters, while occasional updates can make the model ill-equipped to handle dynamically changing environments. Therefore, we propose a Fast-Slow Test-Time Adaptation (FSTTA) approach for online VLN by performing joint decomposition-accumulation analysis for both gradients and parameters in a unified framework. Extensive experiments show that our method obtains impressive performance gains on four popular benchmarks. Code is available at https://github.com/Feliciaxyao/ICML2024-FSTTA.