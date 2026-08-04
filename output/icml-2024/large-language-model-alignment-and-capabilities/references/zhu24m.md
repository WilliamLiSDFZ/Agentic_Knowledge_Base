---
title: "Dynamic Evaluation of Large Language Models by Meta Probing Agents"
source: "https://proceedings.mlr.press/v235/zhu24m.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/zhu24m/zhu24m.pdf"
categories: ['large-language-model-alignment-and-capabilities', 'test-time-adaptation-methods-and-evaluation']
tags: ['LLM-evaluation', 'data-contamination', 'dynamic-evaluation', 'meta-probing', 'benchmark']
venue: "ICML 2024"
tldr: "This paper proposes dynamic evaluation of LLMs using meta probing agents to address data contamination in benchmarks."
---

# Dynamic Evaluation of Large Language Models by Meta Probing Agents

**Source**: [https://proceedings.mlr.press/v235/zhu24m.html](https://proceedings.mlr.press/v235/zhu24m.html)

**TLDR**: This paper proposes dynamic evaluation of LLMs using meta probing agents to address data contamination in benchmarks.

## Abstract

Evaluation of large language models (LLMs) has raised great concerns in the community due to the issue of data contamination. Existing work designed evaluation protocols using well-defined algorithms for specific tasks, which cannot be easily extended to diverse scenarios. Moreover, current evaluation benchmarks can only provide the overall benchmark results and cannot support a fine-grained and multifaceted analysis of LLMs’ abilities. In this paper, we propose meta probing agents (MPA), a general dynamic evaluation protocol inspired by psychometrics to evaluate LLMs. MPA designs the probing and judging agents to automatically transform an original evaluation problem into a new one following psychometric theory on three basic cognitive abilities: language understanding, problem solving, and domain knowledge. These basic abilities are also dynamically configurable, allowing multifaceted analysis. We conducted extensive evaluations using MPA and found that most LLMs achieve poorer performance, indicating room for improvement. Our multifaceted analysis demonstrated the strong correlation between the basic abilities and an implicit Mattew effect on model size, i.e., larger models possess stronger correlations of the abilities. MPA can also be used as a data augmentation approach to enhance LLMs. Code is available at: https://github.com/microsoft/promptbench.