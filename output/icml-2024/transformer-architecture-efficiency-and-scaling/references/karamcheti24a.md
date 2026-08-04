---
title: "Prismatic VLMs: Investigating the Design Space of Visually-Conditioned Language Models"
source: "https://proceedings.mlr.press/v235/karamcheti24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/karamcheti24a/karamcheti24a.pdf"
categories: ['large-language-model-alignment-and-capabilities', 'transformer-architecture-efficiency-and-scaling']
tags: ['vision-language-models', 'design-space', 'visual-conditioning', 'LLaVA', 'multimodal']
venue: "ICML 2024"
tldr: "Systematically investigates the design space of visually-conditioned language models to identify best practices for building VLMs."
---

# Prismatic VLMs: Investigating the Design Space of Visually-Conditioned Language Models

**Source**: [https://proceedings.mlr.press/v235/karamcheti24a.html](https://proceedings.mlr.press/v235/karamcheti24a.html)

**TLDR**: Systematically investigates the design space of visually-conditioned language models to identify best practices for building VLMs.

## Abstract

Visually-conditioned language models (VLMs) have seen growing adoption in applications such as visual dialogue, scene understanding, and robotic task planning; adoption that has fueled a wealth of new models such as LLaVa, InstructBLIP, and PaLI-3. Despite the volume of new releases, key design decisions around image preprocessing, architecture, and optimization are under-explored, making it challenging to understand what factors account for model performance – a challenge further complicated by the lack of objective, consistent evaluations. To address these gaps, we first compile a suite of standardized evaluations spanning visual question answering, object localization, and challenge sets that probe properties such as hallucination; evaluations that provide fine-grained insight VLM capabilities. Second, we rigorously investigate VLMs along key design axes, including pretrained visual representations and training from base vs. instruct-tuned language models, amongst others. We couple our analysis with three resource contributions: (1) a unified framework for evaluating VLMs, (2) optimized, flexible training code, and (3) checkpoints for all models, including a family of VLMs at the 7-13B scale that strictly outperform InstructBLIP and LLaVa v1.5, the state-of-the-art in open VLMs.