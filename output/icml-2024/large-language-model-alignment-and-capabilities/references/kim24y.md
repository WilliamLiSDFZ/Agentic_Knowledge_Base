---
title: "An LLM Compiler for Parallel Function Calling"
source: "https://proceedings.mlr.press/v235/kim24y.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/kim24y/kim24y.pdf"
categories: ['large-language-model-alignment-and-capabilities', 'llm-driven-automated-system-optimization']
tags: ['LLM', 'function-calling', 'parallel-execution']
venue: "ICML 2024"
tldr: "Presents an LLM compiler framework that enables efficient parallel function calling for large language models."
---

# An LLM Compiler for Parallel Function Calling

**Source**: [https://proceedings.mlr.press/v235/kim24y.html](https://proceedings.mlr.press/v235/kim24y.html)

**TLDR**: Presents an LLM compiler framework that enables efficient parallel function calling for large language models.

## Abstract

The reasoning capabilities of the recent LLMs enable them to execute external function calls to overcome their inherent limitations, such as knowledge cutoffs, poor arithmetic skills, or lack of access to private data. This development has allowed LLMs to select and coordinate multiple functions based on the context to tackle more complex problems. However, current methods for function calling often require sequential reasoning and acting for each function which can result in high latency, cost, and sometimes inaccurate behavior. To address this, we introduce LLMCompiler, which executes functions in parallel to efficiently orchestrate multiple function calls. Drawing inspiration from the principles of classical compilers, LLMCompiler enables parallel function calling with three components: (i) a Function Calling Planner, formulating execution plans for function calling; (ii) a Task Fetching Unit, dispatching function calling tasks; and (iii) an Executor, executing these tasks in parallel. LLMCompiler automatically generates an optimized orchestration for the function calls and can be used with both open-source and closed-source models. We have benchmarked LLMCompiler on a range of tasks with different patterns of function calling. We observe consistent latency speedup of up to $3.7 \times$, cost savings of up to $6.7 \times$, and accuracy improvement of up to $\sim 9 %$ compared to ReAct.Our code is available at https://github.com/SqueezeAILab/LLMCompiler.