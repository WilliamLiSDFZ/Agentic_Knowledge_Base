---
title: "MatPlotAgent: Method and Evaluation for LLM-Based Agentic Scientific Data Visualization"
source: "https://aclanthology.org/2024.findings-acl.701/"
pdf_url: ""
categories: ['llm-agents-for-scientific-data-tasks', 'code-llm-generation-and-evaluation']
tags: ['scientific-visualization', 'LLM-agents', 'code-generation']
venue: "ACL 2024"
tldr: "Proposes MatPlotAgent, an LLM-based agentic framework with benchmark for automated scientific data visualization."
---

# MatPlotAgent: Method and Evaluation for LLM-Based Agentic Scientific Data Visualization

**Source**: [https://aclanthology.org/2024.findings-acl.701/](https://aclanthology.org/2024.findings-acl.701/)

**TLDR**: Proposes MatPlotAgent, an LLM-based agentic framework with benchmark for automated scientific data visualization.

## Abstract

AbstractScientific data visualization plays a crucial role in research by enabling the direct display of complex information and assisting researchers in identifying implicit patterns. Despite its importance, the use of Large Language Models (LLMs) for scientific data visualization remains rather unexplored. In this study, we introduce MatPlotAgent, an efficient model-agnostic LLM agent framework designed to automate scientific data visualization tasks. Leveraging the capabilities of both code LLMs and multi-modal LLMs, MatPlotAgent consists of three core modules: query understanding, code generation with iterative debugging, and a visual feedback mechanism for error correction. To address the lack of benchmarks in this field, we present MatPlotBench, a high-quality benchmark consisting of 100 human-verified test cases. Additionally, we introduce a scoring approach that utilizes GPT-4V for automatic evaluation. Experimental results demonstrate that MatPlotAgent can improve the performance of various LLMs, including both commercial and open-source models. Furthermore, the proposed evaluation method shows a strong correlation with human-annotated scores.