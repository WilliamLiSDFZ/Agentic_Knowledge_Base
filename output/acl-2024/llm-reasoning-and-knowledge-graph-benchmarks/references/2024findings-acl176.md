---
title: "Efficient Knowledge Infusion via KG-LLM Alignment"
source: "https://aclanthology.org/2024.findings-acl.176/"
categories: ['llm-reasoning-and-knowledge-graph-benchmarks', 'llms-for-biomedical-and-clinical-nlp']
tags: ['knowledge-graph', 'llm-alignment', 'domain-knowledge-infusion']
venue: "ACL 2024"
tldr: "Proposes a KG-LLM alignment method to efficiently infuse domain-specific knowledge into LLMs by bridging knowledge graph and language model representations."
---

# Efficient Knowledge Infusion via KG-LLM Alignment

**Source**: [https://aclanthology.org/2024.findings-acl.176/](https://aclanthology.org/2024.findings-acl.176/)

**TLDR**: Proposes a KG-LLM alignment method to efficiently infuse domain-specific knowledge into LLMs by bridging knowledge graph and language model representations.

## Abstract

AbstractTo tackle the problem of domain-specific knowledge scarcity within large language models (LLMs), knowledge graph-retrievalaugmented method has been proven to be an effective and efficient technique for knowledge infusion. However, existing approaches face two primary challenges: knowledge mismatch between public available knowledge graphs and the specific domain of the task at hand, and poor information compliance of LLMs with knowledge graphs. In this paper, we leverage a small set of labeled samples and a large-scale corpus to efficiently construct domain-specific knowledge graphs by an LLM, addressing the issue of knowledge mismatch. Additionally, we propose a three-stage KG-LLM alignment strategy to enhance the LLM’s capability to utilize information from knowledge graphs. We conduct experiments with a limited-sample setting on two biomedical question-answering datasets, and the results demonstrate that our approach outperforms existing baselines.