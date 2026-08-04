---
title: "Q-Align: Teaching LMMs for Visual Scoring via Discrete Text-Defined Levels"
source: "https://proceedings.mlr.press/v235/wu24ah.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/wu24ah/wu24ah.pdf"
categories: ['image-quality-assessment-and-super-resolution', 'large-language-model-alignment-and-capabilities']
tags: ['image-quality-assessment', 'large-multimodal-models', 'visual-scoring', 'discrete-text-levels', 'LMM']
venue: "ICML 2024"
tldr: "Proposes Q-Align, training large multimodality models for visual scoring using discrete text-defined quality levels to accurately evaluate diverse visual content."
---

# Q-Align: Teaching LMMs for Visual Scoring via Discrete Text-Defined Levels

**Source**: [https://proceedings.mlr.press/v235/wu24ah.html](https://proceedings.mlr.press/v235/wu24ah.html)

**TLDR**: Proposes Q-Align, training large multimodality models for visual scoring using discrete text-defined quality levels to accurately evaluate diverse visual content.

## Abstract

The explosion of visual content available online underscores the requirement for an accurate machine assessor to robustly evaluate scores across diverse types of visual contents. While recent studies have demonstrated the exceptional potentials of large multi-modality models (LMMs) on a wide range of related fields, in this work, we explore how to teach them for visual rating aligning with human opinions. Observing that human raters only learn and judge discrete text-defined levels in subjective studies, we propose to emulate this subjective process and teach LMMs with text-defined rating levels instead of scores. The proposed Q-Align achieves state-of-the-art accuracy on image quality assessment (IQA), image aesthetic assessment (IAA), as well as video quality assessment (VQA) under the original LMM structure. With the syllabus, we further unify the three tasks into one model, termed the OneAlign. Our experiments demonstrate the advantage of discrete levels over direct scores on training, and that LMMs can learn beyond the discrete levels and provide effective finer-grained evaluations. Code and weights will be released.