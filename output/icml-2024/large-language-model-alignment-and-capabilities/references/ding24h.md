---
title: "Quality Diversity through Human Feedback: Towards Open-Ended Diversity-Driven Optimization"
source: "https://proceedings.mlr.press/v235/ding24h.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/ding24h/ding24h.pdf"
categories: ['large-language-model-alignment-and-capabilities', 'generative-models-and-variational-inference']
tags: ['quality-diversity', 'RLHF', 'human-feedback', 'open-ended-optimization', 'diversity']
venue: "ICML 2024"
tldr: "Combines quality diversity optimization with human feedback to drive open-ended diverse generation beyond average-preference optimization in generative tasks."
---

# Quality Diversity through Human Feedback: Towards Open-Ended Diversity-Driven Optimization

**Source**: [https://proceedings.mlr.press/v235/ding24h.html](https://proceedings.mlr.press/v235/ding24h.html)

**TLDR**: Combines quality diversity optimization with human feedback to drive open-ended diverse generation beyond average-preference optimization in generative tasks.

## Abstract

Reinforcement Learning from Human Feedback (RLHF) has shown potential in qualitative tasks where easily defined performance measures are lacking. However, there are drawbacks when RLHF is commonly used to optimize for average human preferences, especially in generative tasks that demand diverse model responses. Meanwhile, Quality Diversity (QD) algorithms excel at identifying diverse and high-quality solutions but often rely on manually crafted diversity metrics. This paper introduces Quality Diversity through Human Feedback (QDHF), a novel approach that progressively infers diversity metrics from human judgments of similarity among solutions, thereby enhancing the applicability and effectiveness of QD algorithms in complex and open-ended domains. Empirical studies show that QDHF significantly outperforms state-of-the-art methods in automatic diversity discovery and matches the efficacy of QD with manually crafted diversity metrics on standard benchmarks in robotics and reinforcement learning. Notably, in open-ended generative tasks, QDHF substantially enhances the diversity of text-to-image generation from a diffusion model and is more favorably received in user studies. We conclude by analyzing QDHF’s scalability, robustness, and quality of derived diversity metrics, emphasizing its strength in open-ended optimization tasks. Code and tutorials are available at https://liding.info/qdhf.