---
title: "Bi-Directional Multi-Granularity Generation Framework for Knowledge Graph-to-Text with Large Language Model"
source: "https://aclanthology.org/2024.acl-short.14/"
pdf_url: ""
categories: ['llm-reasoning-and-knowledge-graph-benchmarks', 'natural-language-processing-information-extraction']
tags: ['knowledge-graph-to-text', 'multi-granularity', 'LLM', 'bidirectional-generation', 'KG-triples']
venue: "ACL 2024"
tldr: "Proposes a bi-directional multi-granularity generation framework for knowledge graph-to-text tasks using large language models."
---

# Bi-Directional Multi-Granularity Generation Framework for Knowledge Graph-to-Text with Large Language Model

**Source**: [https://aclanthology.org/2024.acl-short.14/](https://aclanthology.org/2024.acl-short.14/)

**TLDR**: Proposes a bi-directional multi-granularity generation framework for knowledge graph-to-text tasks using large language models.

## Abstract

AbstractThe knowledge graph-to-text (KG-to-text) generation task aims to synthesize coherent and engaging sentences that accurately convey the complex information derived from an input knowledge graph. Existing methods generate the whole target text based on all KG triples at once and may incorporate incorrect KG triples for each sentence. To this end, we propose the bi-directional multi-granularity generation framework. Instead of generating the whole text at a time, we construct the sentence level generation based on the corresponding triples and generate the graph-level text as a result. Moreover, we design a backward relation extraction task to enhance the correctness of relational information. Our method achieves the new state-of-the-art in benchmark dataset WebNLG and further analysis shows the efficiency of different modules.