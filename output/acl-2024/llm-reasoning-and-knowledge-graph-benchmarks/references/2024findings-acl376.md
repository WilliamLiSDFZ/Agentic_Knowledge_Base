---
title: "Knowledge Graph-Enhanced Large Language Models via Path Selection"
source: "https://aclanthology.org/2024.findings-acl.376/"
categories: ['llm-reasoning-and-knowledge-graph-benchmarks']
tags: ['knowledge-graph', 'hallucination-mitigation', 'path-selection']
venue: "ACL 2024"
tldr: "Enhances LLM factual accuracy by selecting relevant knowledge graph paths to augment generation."
---

# Knowledge Graph-Enhanced Large Language Models via Path Selection

**Source**: [https://aclanthology.org/2024.findings-acl.376/](https://aclanthology.org/2024.findings-acl.376/)

**TLDR**: Enhances LLM factual accuracy by selecting relevant knowledge graph paths to augment generation.

## Abstract

AbstractLarge Language Models (LLMs) have shown unprecedented performance in various real-world applications. However, they are known to generate factually inaccurate outputs, a.k.a. the hallucination problem. In recent years, incorporating external knowledge extracted from Knowledge Graphs (KGs) has become a promising strategy to improve the factual accuracy of LLM-generated outputs. Nevertheless, most existing explorations rely on LLMs themselves to perform KG knowledge extraction, which is highly inflexible as LLMs can only provide binary judgment on whether a certain knowledge (e.g., a knowledge path in KG) should be used. In addition, LLMs tend to pick only knowledge with direct semantic relationship with the input text, while potentially useful knowledge with indirect semantics can be ignored. In this work, we propose a principled framework KELP with three stages to handle the above problems. Specifically, KELP is able to achieve finer granularity of flexible knowledge extraction by generating scores for knowledge paths with input texts via latent semantic matching. Meanwhile, knowledge paths with indirect semantic relationships with the input text can also be considered via trained encoding between the selected paths in KG and the input text. Experiments on real-world datasets validate the effectiveness of KELP.