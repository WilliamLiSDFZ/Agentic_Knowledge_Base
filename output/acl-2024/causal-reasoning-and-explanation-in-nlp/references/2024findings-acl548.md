---
title: "Are LLMs Capable of Data-based Statistical and Causal Reasoning? Benchmarking Advanced Quantitative Reasoning with Data"
source: "https://aclanthology.org/2024.findings-acl.548/"
pdf_url: ""
categories: ['causal-reasoning-and-explanation-in-nlp', 'llm-reasoning-and-knowledge-graph-benchmarks']
tags: ['quantitative-reasoning', 'causal-reasoning', 'statistical-reasoning', 'LLM-benchmark', 'data-analysis']
venue: "ACL 2024"
tldr: "Introduces QRData benchmark to evaluate LLMs' statistical and causal reasoning capabilities over real datasets."
---

# Are LLMs Capable of Data-based Statistical and Causal Reasoning? Benchmarking Advanced Quantitative Reasoning with Data

**Source**: [https://aclanthology.org/2024.findings-acl.548/](https://aclanthology.org/2024.findings-acl.548/)

**TLDR**: Introduces QRData benchmark to evaluate LLMs' statistical and causal reasoning capabilities over real datasets.

## Abstract

AbstractQuantitative reasoning is a critical skill to analyze data, yet the assessment of such ability remains limited. To address this gap, we introduce the Quantitative Reasoning with Data (QRData) benchmark, aiming to evaluate Large Language Models’ capability in statistical and causal reasoning with real-world data. The benchmark comprises a carefully constructed dataset of 411 questions accompanied by data sheets from textbooks, online learning materials, and academic papers. To compare models’ quantitative reasoning abilities on data and text, we enrich the benchmark with an auxiliary set of 290 text-only questions, namely QRText. We evaluate natural language reasoning, program-based reasoning, and agent reasoning methods including Chain-of-Thought, Program-of-Thoughts, ReAct, and code interpreter assistants on diverse models. The strongest model GPT-4 achieves an accuracy of 58%, which has much room for improvement. Among open-source models, Deepseek-coder-instruct, a code LLM pretrained on 2T tokens, gets the highest accuracy of 37%. Analysis reveals that models encounter difficulties in data analysis and causal reasoning, and struggle in using causal knowledge and provided data simultaneously. Code and data are in https://github.com/xxxiaol/QRData.