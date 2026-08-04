---
title: "Evaluating and Analyzing Relationship Hallucinations in Large Vision-Language Models"
source: "https://proceedings.mlr.press/v235/wu24l.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/wu24l/wu24l.pdf"
categories: ['large-language-model-alignment-and-capabilities', 'ai-explainability-uncertainty-human-decision-making']
tags: ['hallucination', 'vision-language-models', 'relationship-detection', 'evaluation', 'multimodal']
venue: "ICML 2024"
tldr: "Investigates relationship hallucinations in large vision-language models beyond object-level hallucinations, providing evaluation and analysis of inter-object relationship errors."
---

# Evaluating and Analyzing Relationship Hallucinations in Large Vision-Language Models

**Source**: [https://proceedings.mlr.press/v235/wu24l.html](https://proceedings.mlr.press/v235/wu24l.html)

**TLDR**: Investigates relationship hallucinations in large vision-language models beyond object-level hallucinations, providing evaluation and analysis of inter-object relationship errors.

## Abstract

The issue of hallucinations is a prevalent concern in existing Large Vision-Language Models (LVLMs). Previous efforts have primarily focused on investigating object hallucinations, which can be easily alleviated by introducing object detectors. However, these efforts neglect hallucinations in inter-object relationships, which is essential for visual comprehension. In this work, we introduce R-Bench, a novel benchmark for evaluating Vision Relationship Hallucination. R-Bench features image-level questions that focus on the existence of relationships and instance-level questions that assess local visual comprehension. We identify three types of relationship co-occurrences that lead to hallucinations: relationship-relationship, subject-relationship, and relationship-object. The visual instruction tuning dataset’s long-tail distribution significantly impacts LVLMs’ understanding of visual relationships. Additionally, our analysis reveals that current LVLMs tend to overlook visual content, overly rely on the common sense knowledge of Large Language Models (LLMs), and struggle with spatial relationship reasoning based on contextual information.