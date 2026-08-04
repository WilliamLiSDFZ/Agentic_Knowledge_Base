---
title: "MLLM-as-a-Judge: Assessing Multimodal LLM-as-a-Judge with Vision-Language Benchmark"
source: "https://proceedings.mlr.press/v235/chen24h.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/chen24h/chen24h.pdf"
categories: ['large-language-model-alignment-and-capabilities', 'ai-explainability-uncertainty-human-decision-making']
tags: ['multimodal-LLMs', 'LLM-as-judge', 'vision-language-benchmark', 'evaluation']
venue: "ICML 2024"
tldr: "A benchmark for evaluating multimodal LLMs used as judges in vision-language tasks, revealing biases and limitations in their assessment capabilities."
---

# MLLM-as-a-Judge: Assessing Multimodal LLM-as-a-Judge with Vision-Language Benchmark

**Source**: [https://proceedings.mlr.press/v235/chen24h.html](https://proceedings.mlr.press/v235/chen24h.html)

**TLDR**: A benchmark for evaluating multimodal LLMs used as judges in vision-language tasks, revealing biases and limitations in their assessment capabilities.

## Abstract

Multimodal Large Language Models (MLLMs) have gained significant attention recently, showing remarkable potential in artificial general intelligence. However, assessing the utility of MLLMs presents considerable challenges, primarily due to the absence multimodal benchmarks that align with human preferences. Drawing inspiration from the concept of LLM-as-a-Judge within LLMs, this paper introduces a novel benchmark, termed MLLM-as-a-Judge, to assess the ability of MLLMs in assisting judges across diverse modalities, encompassing three distinct tasks: Scoring Evaluation, Pair Comparison, and Batch Ranking. Our study reveals that, while MLLMs demonstrate remarkable human-like discernment in Pair Comparisons, there is a significant divergence from human preferences in Scoring Evaluation and Batch Ranking tasks. Furthermore, a closer examination reveals persistent challenges in the evaluative capacities of LLMs, including diverse biases, hallucinatory responses, and inconsistencies in judgment, even in advanced models such as GPT-4V. These findings emphasize the pressing need for enhancements and further research efforts to be undertaken before regarding MLLMs as fully reliable evaluators. In light of this, we advocate for additional efforts dedicated to supporting the continuous development within the domain of MLLM functioning as judges. The code and dataset are publicly available at our project homepage: https://mllm-judge.github.io/.