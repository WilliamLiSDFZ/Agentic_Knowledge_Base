---
title: "Envisioning Outlier Exposure by Large Language Models for Out-of-Distribution Detection"
source: "https://proceedings.mlr.press/v235/cao24d.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/cao24d/cao24d.pdf"
categories: ['anomaly-and-out-of-distribution-detection', 'large-language-model-alignment-and-capabilities']
tags: ['out-of-distribution-detection', 'LLM', 'outlier-exposure', 'vision-language-models']
venue: "ICML 2024"
tldr: "Leverages large language models to synthesize virtual outlier descriptions for zero-shot out-of-distribution detection."
---

# Envisioning Outlier Exposure by Large Language Models for Out-of-Distribution Detection

**Source**: [https://proceedings.mlr.press/v235/cao24d.html](https://proceedings.mlr.press/v235/cao24d.html)

**TLDR**: Leverages large language models to synthesize virtual outlier descriptions for zero-shot out-of-distribution detection.

## Abstract

Detecting out-of-distribution (OOD) samples is essential when deploying machine learning models in open-world scenarios. Zero-shot OOD detection, requiring no training on in-distribution (ID) data, has been possible with the advent of vision-language models like CLIP. Existing methods build a text-based classifier with only closed-set labels. However, this largely restricts the inherent capability of CLIP to recognize samples from large and open label space. In this paper, we propose to tackle this constraint by leveraging the expert knowledge and reasoning capability of large language models (LLM) to Envision potential Outlier Exposure, termed EOE, without access to any actual OOD data. Owing to better adaptation to open-world scenarios, EOE can be generalized to different tasks, including far, near, and fine-grained OOD detection. Technically, we design (1) LLM prompts based on visual similarity to generate potential outlier class labels specialized for OOD detection, as well as (2) a new score function based on potential outlier penalty to distinguish hard OOD samples effectively. Empirically, EOE achieves state-of-the-art performance across different OOD tasks and can be effectively scaled to the ImageNet-1K dataset. The code is publicly available at: https://github.com/tmlr-group/EOE.