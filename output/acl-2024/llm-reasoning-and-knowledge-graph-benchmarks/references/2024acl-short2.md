---
title: "FanOutQA: A Multi-Hop, Multi-Document Question Answering Benchmark for Large Language Models"
source: "https://aclanthology.org/2024.acl-short.2/"
pdf_url: ""
categories: ['llm-reasoning-and-knowledge-graph-benchmarks', 'llm-training-alignment-and-evaluation']
tags: ['multi-hop-qa', 'benchmark', 'fan-out-questions']
venue: "ACL 2024"
tldr: "Introduces FanOutQA, a benchmark requiring LLMs to answer complex multi-hop questions spanning many entities across multiple documents."
---

# FanOutQA: A Multi-Hop, Multi-Document Question Answering Benchmark for Large Language Models

**Source**: [https://aclanthology.org/2024.acl-short.2/](https://aclanthology.org/2024.acl-short.2/)

**TLDR**: Introduces FanOutQA, a benchmark requiring LLMs to answer complex multi-hop questions spanning many entities across multiple documents.

## Abstract

AbstractOne type of question that is commonly found in day-to-day scenarios is “fan-out” questions, complex multi-hop, multi-document reasoning questions that require finding information about a large number of entities. However, there exist few resources to evaluate this type of question-answering capability among large language models. To evaluate complex reasoning in LLMs more fully, we present FanOutQA, a high-quality dataset of fan-out question-answer pairs and human-annotated decompositions with English Wikipedia as the knowledge base. We formulate three benchmark settings across our dataset and benchmark 7 LLMs, including GPT-4, LLaMA 2, Claude-2.1, and Mixtral-8x7B, finding that contemporary models still have room to improve reasoning over inter-document dependencies in a long context. We provide our dataset, along with open-source tools to run models to encourage evaluation.