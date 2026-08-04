---
title: "CRUXEval: A Benchmark for Code Reasoning, Understanding and Execution"
source: "https://proceedings.mlr.press/v235/gu24c.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/gu24c/gu24c.pdf"
categories: ['large-language-model-alignment-and-capabilities', 'neural-network-learning-dynamics-theory']
tags: ['code-reasoning', 'benchmark', 'llm-evaluation']
venue: "ICML 2024"
tldr: "CRUXEval introduces a benchmark of 800 Python functions to evaluate LLM capabilities in code reasoning, understanding, and execution prediction."
---

# CRUXEval: A Benchmark for Code Reasoning, Understanding and Execution

**Source**: [https://proceedings.mlr.press/v235/gu24c.html](https://proceedings.mlr.press/v235/gu24c.html)

**TLDR**: CRUXEval introduces a benchmark of 800 Python functions to evaluate LLM capabilities in code reasoning, understanding, and execution prediction.

## Abstract

We present Code Reasoning, Understanding, and eXecution Evaluation, a benchmark consisting of 800 Python functions (3-13 lines). Each function comes with an input-output pair, leading to two natural tasks: input prediction and output prediction. First, we propose a general recipe for generating our execution benchmark by sampling from a model, which can be used for more challenging versions of the benchmark if needed. Second, we evaluate twenty code models on our benchmark and discover that many recent high-scoring models on HumanEval show no improvements on our benchmark. Third, we show that simple CoT and fine-tuning schemes can improve performance on our benchmark but remain far from solving it. The best setup, GPT-4 with chain of thought (CoT), achieves a pass@1 of 75% and 81% on input and output prediction, respectively. In contrast, Code Llama 34B achieves a pass@1 of 50% and 46% on input and output prediction. When it comes to reasoning about code, GPT-4 has a huge edge over other models but still fails consistently on some surprisingly simple Python programs.