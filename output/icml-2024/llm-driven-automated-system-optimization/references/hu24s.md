---
title: "InfiAgent-DABench: Evaluating Agents on Data Analysis Tasks"
source: "https://proceedings.mlr.press/v235/hu24s.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/hu24s/hu24s.pdf"
categories: ['large-language-model-alignment-and-capabilities', 'llm-driven-automated-system-optimization']
tags: ['llm-agents', 'data-analysis', 'benchmark-evaluation']
venue: "ICML 2024"
tldr: "Introduces InfiAgent-DABench, the first benchmark for evaluating LLM-based agents on end-to-end data analysis tasks."
---

# InfiAgent-DABench: Evaluating Agents on Data Analysis Tasks

**Source**: [https://proceedings.mlr.press/v235/hu24s.html](https://proceedings.mlr.press/v235/hu24s.html)

**TLDR**: Introduces InfiAgent-DABench, the first benchmark for evaluating LLM-based agents on end-to-end data analysis tasks.

## Abstract

In this paper, we introduce InfiAgent-DABench, the first benchmark specifically designed to evaluate LLM-based agents on data analysis tasks. Agents need to solve these tasks end-to-end by interacting with an execution environment. This benchmark contains DAEval, a dataset consisting of 603 data analysis questions derived from 124 CSV files, and an agent framework which incorporates LLMs to serve as data analysis agents for both serving and evaluating. Since data analysis questions are often open-ended and hard to evaluate without human supervision, we adopt a format-prompting technique to convert each question into a closed-form format so that they can be automatically evaluated. Our extensive benchmarking of 34 LLMs uncovers the current challenges encountered in data analysis tasks. In addition, building upon our agent framework, we develop a specialized agent, DAAgent, which surpasses GPT-3.5 by 3.9% on DABench. Evaluation datasets and toolkits for InfiAgent-DABench are released at https://github.com/InfiAgent/InfiAgent.