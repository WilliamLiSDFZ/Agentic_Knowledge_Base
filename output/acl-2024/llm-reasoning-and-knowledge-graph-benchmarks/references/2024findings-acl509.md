---
title: "Knowledge Context Modeling with Pre-trained Language Models for Contrastive Knowledge Graph Completion"
source: "https://aclanthology.org/2024.findings-acl.509/"
categories: ['llm-reasoning-and-knowledge-graph-benchmarks', 'language-model-representations-and-embedding-spaces']
tags: ['knowledge-graph-completion', 'contrastive-learning', 'PLMs']
venue: "ACL 2024"
tldr: "Knowledge context modeling with pre-trained language models improves contrastive knowledge graph completion."
---

# Knowledge Context Modeling with Pre-trained Language Models for Contrastive Knowledge Graph Completion

**Source**: [https://aclanthology.org/2024.findings-acl.509/](https://aclanthology.org/2024.findings-acl.509/)

**TLDR**: Knowledge context modeling with pre-trained language models improves contrastive knowledge graph completion.

## Abstract

AbstractText-based knowledge graph completion (KGC) methods utilize pre-trained language models for triple encoding and further fine-tune the model to achieve completion. Despite their excellent performance, they neglect the knowledge context in inferring process. Intuitively, knowledge contexts, which refer to the neighboring triples around the target triples, are important information for triple inferring, since they provide additional detailed information about the entities. To this end, we propose a novel framework named KnowC, which models the knowledge context as additional prompts with pre-trained language models for knowledge graph completion. Given the substantial number of neighbors typically associated with entities, along with the constrained input token capacity of language models, we further devise several strategies to sample the neighbors. We conduct extensive experiments on common datasets FB15k-237, WN18RR and Wikidata5M, experiments show that KnowC achieves state-of-the-art performance.