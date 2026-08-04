---
title: "MM-Vet: Evaluating Large Multimodal Models for Integrated Capabilities"
source: "https://proceedings.mlr.press/v235/yu24o.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/yu24o/yu24o.pdf"
categories: ['large-language-model-alignment-and-capabilities', 'ai-explainability-uncertainty-human-decision-making']
tags: ['multimodal-models', 'evaluation-benchmark', 'integrated-capabilities']
venue: "ICML 2024"
tldr: "MM-Vet is a benchmark for evaluating large multimodal models on complex tasks requiring integrated visual and language capabilities."
---

# MM-Vet: Evaluating Large Multimodal Models for Integrated Capabilities

**Source**: [https://proceedings.mlr.press/v235/yu24o.html](https://proceedings.mlr.press/v235/yu24o.html)

**TLDR**: MM-Vet is a benchmark for evaluating large multimodal models on complex tasks requiring integrated visual and language capabilities.

## Abstract

We propose MM-Vet, an evaluation benchmark that examines large multimodal models (LMMs) on complicated multimodal tasks. Recent LMMs have shown various intriguing abilities, such as solving math problems written on the blackboard, reasoning about events and celebrities in news images, and explaining visual jokes. Rapid model advancements pose challenges to evaluation benchmark development. Problems include: (1) How to systematically structure and evaluate the complicated multimodal tasks; (2) How to design evaluation metrics that work well across question and answer types; and (3) How to give model insights beyond a simple performance ranking. To this end, we present MM-Vet, designed based on the insight that the intriguing ability to solve complicated tasks is often achieved by a generalist model being able to integrate different core vision-language (VL) capabilities. MM-Vet defines 6 core VL capabilities and examines the 16 integrations of interest derived from the capability combination. For evaluation metrics, we propose an LLM-based evaluator for open-ended outputs. The evaluator enables the evaluation across different question types and answer styles, resulting in a unified scoring metric. We evaluate representative LMMs on MM-Vet, providing insights into the capabilities of different LMM system paradigms and models.