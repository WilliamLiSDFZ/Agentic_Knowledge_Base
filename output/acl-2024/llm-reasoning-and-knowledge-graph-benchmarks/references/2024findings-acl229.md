---
title: "KG-Adapter: Enabling Knowledge Graph Integration in Large Language Models through Parameter-Efficient Fine-Tuning"
source: "https://aclanthology.org/2024.findings-acl.229/"
pdf_url: ""
categories: ['llm-reasoning-and-knowledge-graph-benchmarks', 'llm-training-alignment-and-evaluation']
tags: ['knowledge-graph', 'parameter-efficient-fine-tuning', 'llm-integration']
venue: "ACL 2024"
tldr: "KG-Adapter enables efficient integration of knowledge graphs into LLMs via parameter-efficient fine-tuning adapters."
---

# KG-Adapter: Enabling Knowledge Graph Integration in Large Language Models through Parameter-Efficient Fine-Tuning

**Source**: [https://aclanthology.org/2024.findings-acl.229/](https://aclanthology.org/2024.findings-acl.229/)

**TLDR**: KG-Adapter enables efficient integration of knowledge graphs into LLMs via parameter-efficient fine-tuning adapters.

## Abstract

AbstractAlthough large language models (LLMs) show remarkable capabilities and generalizability across various tasks, they are criticized for lack of expertise. One promising solution is to combine knowledge graphs (KGs) with LLMs, and recent studies focus on integrating KGs into LLMs through prompt-based methods. However, these approaches fail to use the structural information of the KGs, suffer from the problem of knowledge conflict, and over-reliance on super LLMs. To address these challenges, we propose KG-Adapter, a parameter-level KG integration method based on parameter-efficient fine-tuning (PEFT). Specifically, we introduce a novel adapter structure designed for decoder-only LLMs, which can encode KGs from both node-centered and relation-centered perspectives, and then perform joint reasoning with LLMs to generate responses end-to-end. Experiments with diverse models on four datasets for two different tasks all demonstrate significant improvements. With only 28M parameters trained, we make the 7B-parameter LLM outperform the previous full-parameter fine-tuned state-of-the-art method and comparable to the prompt-based ChatGPT methods.