---
title: "AnyTool: Self-Reflective, Hierarchical Agents for Large-Scale API Calls"
source: "https://proceedings.mlr.press/v235/du24h.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/du24h/du24h.pdf"
categories: ['large-language-model-alignment-and-capabilities', 'llm-driven-automated-system-optimization']
tags: ['LLM-agents', 'API-calls', 'tool-use', 'hierarchical-agents']
venue: "ICML 2024"
tldr: "AnyTool is a hierarchical self-reflective LLM agent that efficiently selects and uses relevant APIs from a pool of over 16,000 to answer user queries."
---

# AnyTool: Self-Reflective, Hierarchical Agents for Large-Scale API Calls

**Source**: [https://proceedings.mlr.press/v235/du24h.html](https://proceedings.mlr.press/v235/du24h.html)

**TLDR**: AnyTool is a hierarchical self-reflective LLM agent that efficiently selects and uses relevant APIs from a pool of over 16,000 to answer user queries.

## Abstract

We introduce AnyTool, a large language model agent designed to revolutionize the utilization of a vast array of tools in addressing user queries. We utilize over 16,000 APIs from Rapid API, operating under the assumption that a subset of these APIs could potentially resolve the queries. AnyTool primarily incorporates three elements: an API retriever with a hierarchical structure, a solver aimed at resolving user queries using a selected set of API candidates, and a self-reflection mechanism, which re-activates AnyTool if the initial solution proves impracticable. AnyTool is powered by the function calling feature of GPT-4, eliminating the need for training external modules. We also revisit the evaluation protocol introduced by previous works and identify a limitation in this protocol that leads to an artificially high pass rate. By revising the evaluation protocol to better reflect practical application scenarios, we introduce an additional benchmark, termed AnyToolBench. Experiments across various datasets demonstrate the superiority of our AnyTool over strong baselines such as ToolLLM and a GPT-4 variant tailored for tool utilization. For instance, AnyTool outperforms ToolLLM by +35.5% in terms of average pass rate on ToolBench.