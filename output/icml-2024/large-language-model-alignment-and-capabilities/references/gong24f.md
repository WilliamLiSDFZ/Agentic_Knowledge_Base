---
title: "Evaluation of LLMs on Syntax-Aware Code Fill-in-the-Middle Tasks"
source: "https://proceedings.mlr.press/v235/gong24f.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/gong24f/gong24f.pdf"
categories: ['large-language-model-alignment-and-capabilities', 'transformer-architecture-efficiency-and-scaling']
tags: ['code-completion', 'fill-in-the-middle', 'llm-benchmark']
venue: "ICML 2024"
tldr: "SAFIM is a new benchmark for evaluating LLMs on syntax-aware code fill-in-the-middle tasks across 17,720 examples."
---

# Evaluation of LLMs on Syntax-Aware Code Fill-in-the-Middle Tasks

**Source**: [https://proceedings.mlr.press/v235/gong24f.html](https://proceedings.mlr.press/v235/gong24f.html)

**TLDR**: SAFIM is a new benchmark for evaluating LLMs on syntax-aware code fill-in-the-middle tasks across 17,720 examples.

## Abstract

We introduce Syntax-Aware Fill-in-the-Middle (SAFIM), a new benchmark for evaluating Large Language Models (LLMs) on the code Fill-in-the-Middle (FIM) task. This benchmark focuses on syntax-aware completions of program structures such as code blocks and conditional expressions, and includes 17,720 examples from multiple programming languages, sourced from recent code submissions after April 2022 to minimize data contamination. SAFIM provides a robust framework with various prompt designs and novel syntax-aware post-processing techniques, facilitating accurate and fair comparisons across LLMs. Our comprehensive evaluation of 15 LLMs shows that FIM pretraining not only enhances FIM proficiency but also improves Left-to-Right (L2R) inference using LLMs. Our findings challenge conventional beliefs and suggest that pretraining methods and data quality have more impact than model size. SAFIM thus serves as a foundational platform for future research in effective pretraining strategies for code LLMs. The evaluation toolkit and dataset are available at https://github.com/gonglinyuan/safim, and the leaderboard is available at https://safimbenchmark.com.