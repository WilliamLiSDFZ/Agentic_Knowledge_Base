---
title: "GameTraversalBenchmark: Evaluating Planning Abilities Of Large Language Models Through Traversing 2D Game Maps"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/3852c8254bc6d904c09db9921157f59b-Abstract-Datasets_and_Benchmarks_Track.html"
categories: ['ai-benchmarking-and-evaluation-methodology', 'reinforcement-learning-optimization-and-decision-making']
tags: ['llm-planning', 'spatial-reasoning', 'game-traversal']
venue: "NeurIPS 2024"
tldr: "A benchmark is introduced to evaluate the planning abilities of large language models through traversal of 2D game maps."
---

# GameTraversalBenchmark: Evaluating Planning Abilities Of Large Language Models Through Traversing 2D Game Maps

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/3852c8254bc6d904c09db9921157f59b-Abstract-Datasets_and_Benchmarks_Track.html](https://papers.nips.cc/paper_files/paper/2024/hash/3852c8254bc6d904c09db9921157f59b-Abstract-Datasets_and_Benchmarks_Track.html)

**TLDR**: A benchmark is introduced to evaluate the planning abilities of large language models through traversal of 2D game maps.

## Abstract

Large language models (LLMs) have recently demonstrated great success in generating and understanding natural language.  While they have also shown potential beyond the domain of natural language, it remains an open question as to what extent and in which way these LLMs can plan. We investigate their planning capabilities by proposing \texttt{GameTraversalBenchmark (GTB)}, a benchmark consisting of diverse 2D grid-based game maps. An LLM succeeds if it can traverse through given objectives, with a minimum number of steps and a minimum number of generation errors. We evaluate a number of LLMs on \texttt{GTB} and found that GPT-4-Turbo achieved the highest score of $44.97\%$ on \texttt{GTB\_Score} (GTBS), a composite score that combines the three above criteria. Furthermore, we preliminarily test large reasoning models, namely o1, which scores $67.84\%$ on GTBS, indicating that the benchmark remains challenging for current models. Code, data, and documentation are available at \url{https://github.com/umair-nasir14/Game-Traversal-Benchmark}.