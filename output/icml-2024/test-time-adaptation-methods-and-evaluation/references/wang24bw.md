---
title: "Open-Vocabulary Calibration for Fine-tuned CLIP"
source: "https://proceedings.mlr.press/v235/wang24bw.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/wang24bw/wang24bw.pdf"
categories: ['uncertainty-calibration-and-distribution-shift-adaptation', 'test-time-adaptation-methods-and-evaluation']
tags: ['CLIP', 'calibration', 'vision-language-models', 'open-vocabulary', 'fine-tuning']
venue: "ICML 2024"
tldr: "Addresses miscalibration in fine-tuned CLIP models for open-vocabulary tasks, proposing methods to improve confidence calibration under distribution shift."
---

# Open-Vocabulary Calibration for Fine-tuned CLIP

**Source**: [https://proceedings.mlr.press/v235/wang24bw.html](https://proceedings.mlr.press/v235/wang24bw.html)

**TLDR**: Addresses miscalibration in fine-tuned CLIP models for open-vocabulary tasks, proposing methods to improve confidence calibration under distribution shift.

## Abstract

Vision-language models (VLMs) have emerged as formidable tools, showing their strong capability in handling various open-vocabulary tasks in image recognition, text-driven visual content generation, and visual chatbots, to name a few. In recent years, considerable efforts and resources have been devoted to adaptation methods for improving downstream performance of VLMs, particularly on parameter-efficient fine-tuning methods like prompt learning. However, a crucial aspect that has been largely overlooked is the confidence calibration problem in fine-tuned VLMs, which could greatly reduce reliability when deploying such models in the real world. This paper bridges the gap by systematically investigating the confidence calibration problem in the context of prompt learning and reveals that existing calibration methods are insufficient to address the problem, especially in the open-vocabulary setting. To solve the problem, we present a simple and effective approach called Distance-Aware Calibration (DAC), which is based on scaling the temperature using as guidance the distance between predicted text labels and base classes. The experiments with 7 distinct prompt learning methods applied across 11 diverse downstream datasets demonstrate the effectiveness of DAC, which achieves high efficacy without sacrificing the inference speed.