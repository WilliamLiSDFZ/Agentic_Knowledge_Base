---
title: "Large Language Models Fall Short: Understanding Complex Relationships in Detective Narratives"
source: "https://aclanthology.org/2024.findings-acl.454/"
pdf_url: ""
categories: ['coreference-resolution-and-dialogue-understanding', 'llm-reasoning-and-knowledge-graph-benchmarks']
tags: ['narrative-understanding', 'relation-extraction', 'detective-fiction']
venue: "ACL 2024"
tldr: "Introduces Conan, a benchmark for extracting and analyzing complex character relationship graphs from detective narratives to test LLM understanding."
---

# Large Language Models Fall Short: Understanding Complex Relationships in Detective Narratives

**Source**: [https://aclanthology.org/2024.findings-acl.454/](https://aclanthology.org/2024.findings-acl.454/)

**TLDR**: Introduces Conan, a benchmark for extracting and analyzing complex character relationship graphs from detective narratives to test LLM understanding.

## Abstract

AbstractExisting datasets for narrative understanding often fail to represent the complexity and uncertainty of relationships in real-life social scenarios. To address this gap, we introduce a new benchmark, Conan, designed for extracting and analysing intricate character relation graphs from detective narratives. Specifically, we designed hierarchical relationship categories and manually extracted and annotated role-oriented relationships from the perspectives of various characters, incorporating both public relationships known to most characters and secret ones known to only a few. Our experiments with advanced Large Language Models (LLMs) like GPT-3.5, GPT-4, and Llama2 reveal their limitations in inferencing complex relationships and handling longer narratives. The combination of the Conan dataset and our pipeline strategy is geared towards understanding the ability of LLMs to comprehend nuanced relational dynamics in narrative contexts.