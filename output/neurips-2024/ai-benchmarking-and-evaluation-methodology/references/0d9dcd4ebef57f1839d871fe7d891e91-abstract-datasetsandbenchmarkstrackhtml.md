---
title: "MLLMGuard: A Multi-dimensional Safety Evaluation Suite for Multimodal Large Language Models"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/0d9dcd4ebef57f1839d871fe7d891e91-Abstract-Datasets_and_Benchmarks_Track.html"
categories: ['llm-safety-robustness-and-privacy-defenses', 'ai-benchmarking-and-evaluation-methodology']
tags: ['multimodal-llm-safety', 'evaluation-suite', 'red-teaming', 'safety-benchmark', 'malicious-instructions']
venue: "NeurIPS 2024"
tldr: "MLLMGuard presents a multi-dimensional safety evaluation suite for assessing multimodal LLMs against malicious instructions."
---

# MLLMGuard: A Multi-dimensional Safety Evaluation Suite for Multimodal Large Language Models

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/0d9dcd4ebef57f1839d871fe7d891e91-Abstract-Datasets_and_Benchmarks_Track.html](https://papers.nips.cc/paper_files/paper/2024/hash/0d9dcd4ebef57f1839d871fe7d891e91-Abstract-Datasets_and_Benchmarks_Track.html)

**TLDR**: MLLMGuard presents a multi-dimensional safety evaluation suite for assessing multimodal LLMs against malicious instructions.

## Abstract

Powered by remarkable advancements in Large Language Models (LLMs), Multimodal Large Language Models (MLLMs) demonstrate impressive capabilities in manifold tasks.However, the practical application scenarios of MLLMs are intricate, exposing them to potential malicious instructions and thereby posing safety risks.While current benchmarks do incorporate certain safety considerations, they often lack comprehensive coverage and fail to exhibit the necessary rigor and robustness.For instance, the common practice of employing GPT-4V as both the evaluator and a model to be evaluated lacks credibility, as it tends to exhibit a bias toward its own responses.In this paper, we present MLLMGuard, a multi-dimensional safety evaluation suite for MLLMs, including a bilingual image-text evaluation dataset, inference utilities, and a lightweight evaluator.MLLMGuard's assessment comprehensively covers two languages (English and Chinese) and five important safety dimensions (Privacy, Bias, Toxicity, Truthfulness, and Legality), each with corresponding rich subtasks.Focusing on these dimensions, our evaluation dataset is primarily sourced from platforms such as social media, and it integrates text-based and image-based red teaming techniques with meticulous annotation by human experts.This can prevent inaccurate evaluation caused by data leakage when using open-source datasets and ensures the quality and challenging nature of our benchmark.Additionally, a fully automated lightweight evaluator termed GuardRank is developed, which achieves significantly higher evaluation accuracy than GPT-4.Our evaluation results across 13 advanced models indicate that MLLMs still have a substantial journey ahead before they can be considered safe and responsible.