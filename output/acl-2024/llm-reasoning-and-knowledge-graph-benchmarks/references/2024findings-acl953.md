---
title: "MATTER: Memory-Augmented Transformer Using Heterogeneous Knowledge Sources"
source: "https://aclanthology.org/2024.findings-acl.953/"
pdf_url: ""
categories: ['llm-reasoning-and-knowledge-graph-benchmarks', 'state-memory-replay-sequence-modeling']
tags: ['memory-augmented', 'knowledge-retrieval', 'heterogeneous-sources']
venue: "ACL 2024"
tldr: "MATTER augments transformers with heterogeneous external knowledge sources for improved knowledge-intensive QA tasks."
---

# MATTER: Memory-Augmented Transformer Using Heterogeneous Knowledge Sources

**Source**: [https://aclanthology.org/2024.findings-acl.953/](https://aclanthology.org/2024.findings-acl.953/)

**TLDR**: MATTER augments transformers with heterogeneous external knowledge sources for improved knowledge-intensive QA tasks.

## Abstract

AbstractLeveraging external knowledge is crucial for achieving high performance in knowledge-intensive tasks, such as question answering. The retrieve-and-read approach is widely adopted for integrating external knowledge into a language model. However, this approach suffers from increased computational cost and latency due to the long context length, which grows proportionally with the number of retrieved knowledge. Furthermore, existing retrieval-augmented models typically retrieve information from a single type of knowledge source, limiting their scalability to diverse knowledge sources with varying structures. In this work, we introduce an efficient memory-augmented transformer called MATTER, designed to retrieve relevant knowledge from multiple heterogeneous knowledge sources. Specifically, our model retrieves and reads from both unstructured sources (paragraphs) and semi-structured sources (QA pairs) in the form of fixed-length neural memories. We demonstrate that our model outperforms existing efficient retrieval-augmented models on popular QA benchmarks in terms of both accuracy and speed. Furthermore, MATTER achieves competitive results compared to conventional read-and-retrieve models while having 100x throughput during inference.