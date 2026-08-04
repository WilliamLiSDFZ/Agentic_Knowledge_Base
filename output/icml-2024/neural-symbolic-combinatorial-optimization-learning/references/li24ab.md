---
title: "VisionGraph: Leveraging Large Multimodal Models for Graph Theory Problems in Visual Context"
source: "https://proceedings.mlr.press/v235/li24ab.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/li24ab/li24ab.pdf"
categories: ['large-language-model-alignment-and-capabilities', 'neural-symbolic-combinatorial-optimization-learning']
tags: ['large-multimodal-models', 'graph-theory', 'visual-reasoning', 'LMM']
venue: "ICML 2024"
tldr: "VisionGraph leverages large multimodal models to solve graph theory problems presented in visual contexts."
---

# VisionGraph: Leveraging Large Multimodal Models for Graph Theory Problems in Visual Context

**Source**: [https://proceedings.mlr.press/v235/li24ab.html](https://proceedings.mlr.press/v235/li24ab.html)

**TLDR**: VisionGraph leverages large multimodal models to solve graph theory problems presented in visual contexts.

## Abstract

Large Multimodal Models (LMMs) have achieved impressive success in visual reasoning, particularly in visual mathematics. However, problem-solving capabilities in graph theory remain less explored for LMMs, despite being a crucial aspect of mathematical reasoning that requires an accurate understanding of graphical structures and multi-step reasoning on visual graphs. To step forward in this direction, we are the first to design a benchmark named VisionGraph, used to explore the capabilities of advanced LMMs in solving multimodal graph theory problems. It encompasses eight complex graph problem tasks, from connectivity to shortest path problems. Subsequently, we present a Description-Program-Reasoning (DPR) chain to enhance the logical accuracy of reasoning processes through graphical structure description generation and algorithm-aware multi-step reasoning. Our extensive study shows that 1) GPT-4V outperforms Gemini Pro in multi-step graph reasoning; 2) All LMMs exhibit inferior perception accuracy for graphical structures, whether in zero/few-shot settings or with supervised fine-tuning (SFT), which further affects problem-solving performance; 3) DPR significantly improves the multi-step graph reasoning capabilities of LMMs and the GPT-4V (DPR) agent achieves SOTA performance.