---
title: "Thermometer: Towards Universal Calibration for Large Language Models"
source: "https://proceedings.mlr.press/v235/shen24c.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/shen24c/shen24c.pdf"
categories: ['uncertainty-calibration-and-distribution-shift-adaptation', 'large-language-model-alignment-and-capabilities']
tags: ['LLM-calibration', 'uncertainty-quantification', 'instruction-tuning']
venue: "ICML 2024"
tldr: "Thermometer is a universal calibration framework for large language models that addresses the unique challenges of miscalibration arising from instruction tuning."
---

# Thermometer: Towards Universal Calibration for Large Language Models

**Source**: [https://proceedings.mlr.press/v235/shen24c.html](https://proceedings.mlr.press/v235/shen24c.html)

**TLDR**: Thermometer is a universal calibration framework for large language models that addresses the unique challenges of miscalibration arising from instruction tuning.

## Abstract

We consider the issue of calibration in large language models (LLM). Recent studies have found that common interventions such as instruction tuning often result in poorly calibrated LLMs. Although calibration is well-explored in traditional applications, calibrating LLMs is uniquely challenging. These challenges stem as much from the severe computational requirements of LLMs as from their versatility, which allows them to be applied to diverse tasks. Addressing these challenges, we propose THERMOMETER, a calibration approach tailored to LLMs. THERMOMETER learns an auxiliary model, given data from multiple tasks, for calibrating a LLM. It is computationally efficient, preserves the accuracy of the LLM, and produces better-calibrated responses for new tasks. Extensive empirical evaluations across various benchmarks demonstrate the effectiveness of the proposed method.