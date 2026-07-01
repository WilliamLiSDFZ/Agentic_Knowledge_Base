---
title: "StackEval: Benchmarking LLMs in Coding Assistance"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/4126a607bbe2836cb6ca0eb45b75618b-Abstract-Datasets_and_Benchmarks_Track.html"
categories: ['ai-benchmarking-and-evaluation-methodology', 'llm-training-and-optimization-techniques']
tags: ['llm-benchmarking', 'coding-assistance', 'software-engineering']
venue: "NeurIPS 2024"
tldr: "Two comprehensive benchmarks derived from Stack Overflow are introduced to evaluate LLMs on coding assistance tasks."
---

# StackEval: Benchmarking LLMs in Coding Assistance

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/4126a607bbe2836cb6ca0eb45b75618b-Abstract-Datasets_and_Benchmarks_Track.html](https://papers.nips.cc/paper_files/paper/2024/hash/4126a607bbe2836cb6ca0eb45b75618b-Abstract-Datasets_and_Benchmarks_Track.html)

**TLDR**: Two comprehensive benchmarks derived from Stack Overflow are introduced to evaluate LLMs on coding assistance tasks.

## Abstract

We present two comprehensive benchmarks to evaluate the performance of language models in coding assistance tasks, covering code writing, debugging, code review, and conceptual understanding. Our main contribution includes two curated datasets: StackEval, a large-scale benchmark derived from Stack Overflow questions, and StackUnseen, a dynamic benchmark featuring the most recent Stack Overflow content. These benchmarks offer novel insights into the capabilities and limitations of LLMs, particularly in handling new and emerging content. Additionally, we assess LLMs' proficiency as judges for coding tasks using a curated, human-annotated dataset, exploring their evaluation capabilities and potential biases, including whether they favor their own generated solutions. Our findings underscore the potential of these benchmarks to advance LLM development and application in coding assistance. To ensure reproducibility, we publicly share our datasets and evaluation code at https://github.com/ProsusAI/stack-eval.