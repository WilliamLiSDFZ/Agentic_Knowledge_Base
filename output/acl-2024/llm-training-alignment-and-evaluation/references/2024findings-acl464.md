---
title: "Teaching Small Language Models to Reason for Knowledge-Intensive Multi-Hop Question Answering"
source: "https://aclanthology.org/2024.findings-acl.464/"
pdf_url: ""
categories: ['llm-training-alignment-and-evaluation', 'llm-reasoning-and-knowledge-graph-benchmarks']
tags: ['knowledge-distillation', 'chain-of-thought', 'multi-hop-QA']
venue: "ACL 2024"
tldr: "Proposes distilling reasoning chains from large LLMs to small language models for knowledge-intensive multi-hop question answering."
---

# Teaching Small Language Models to Reason for Knowledge-Intensive Multi-Hop Question Answering

**Source**: [https://aclanthology.org/2024.findings-acl.464/](https://aclanthology.org/2024.findings-acl.464/)

**TLDR**: Proposes distilling reasoning chains from large LLMs to small language models for knowledge-intensive multi-hop question answering.

## Abstract

AbstractLarge Language Models (LLMs) can teach small language models (SLMs) to solve complex reasoning tasks (e.g., mathematical question answering) by Chain-of-thought Distillation (CoTD). Specifically, CoTD fine-tunes SLMs by utilizing rationales generated from LLMs such as ChatGPT. However, CoTD has certain limitations that make it unsuitable for knowledge-intensive multi-hop question answering: 1) SLMs have a very limited capacity in memorizing required knowledge compared to LLMs. 2) SLMs do not possess the same powerful integrated abilities in question understanding and knowledge reasoning as LLMs. To address the above limitations, we introduce Decompose-and-Response Distillation (D&R Distillation), which distills two student models, namely Decomposer and Responser separately. The two models solve a knowledge-intensive multi-hop question through an interactive process of asking and answering subquestions. Our method offers two advantages: 1) SLMs have the capability to access external knowledge to address subquestions, which provides more comprehensive knowledge for multi-hop questions. 2) By employing simpler subquestions instead of complex CoT reasoning, SLMs effectively mitigate task complexity and decrease data prerequisites. Experimental results on three knowledge-intensive multi-hop question answering datasets demonstrate that D&R Distillation can surpass previous CoTD methods, even with much less training data.