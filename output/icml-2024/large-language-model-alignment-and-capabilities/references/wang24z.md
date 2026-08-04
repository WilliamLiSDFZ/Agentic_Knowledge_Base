---
title: "SciBench: Evaluating College-Level Scientific Problem-Solving Abilities of Large Language Models"
source: "https://proceedings.mlr.press/v235/wang24z.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/wang24z/wang24z.pdf"
categories: ['large-language-model-alignment-and-capabilities', 'position-papers-on-ml-research-directions']
tags: ['LLM-benchmarking', 'scientific-reasoning', 'college-level-problems', 'evaluation']
venue: "ICML 2024"
tldr: "SciBench introduces a benchmark for evaluating LLMs on complex college-level scientific problem solving beyond elementary algebra."
---

# SciBench: Evaluating College-Level Scientific Problem-Solving Abilities of Large Language Models

**Source**: [https://proceedings.mlr.press/v235/wang24z.html](https://proceedings.mlr.press/v235/wang24z.html)

**TLDR**: SciBench introduces a benchmark for evaluating LLMs on complex college-level scientific problem solving beyond elementary algebra.

## Abstract

Most existing Large Language Model (LLM) benchmarks on scientific problem reasoning focus on problems grounded in high-school subjects and are confined to elementary algebraic operations. To systematically examine the reasoning capabilities required for solving complex scientific problems, we introduce an expansive benchmark suite SciBench for LLMs. SciBench contains a carefully curated dataset featuring a range of collegiate-level scientific problems from mathematics, chemistry, and physics domains. Based on the dataset, we conduct an in-depth benchmarking study of representative open-source and proprietary LLMs with various prompting strategies. The results reveal that current LLMs fall short of delivering satisfactory performance, with the best overall score of merely 43.22%. Furthermore, through a detailed user study, we categorize the errors made by LLMs into ten problem-solving abilities. Our analysis indicates that no single prompting strategy significantly outperforms the others and some strategies that demonstrate improvements in certain problem-solving skills could result in declines in other skills. We envision that SciBench will catalyze further developments in the reasoning abilities of LLMs, thereby ultimately contributing to scientific research and discovery.