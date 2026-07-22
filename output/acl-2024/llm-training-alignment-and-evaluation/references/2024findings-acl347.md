---
title: "Mass-Editing Memory with Attention in Transformers: A cross-lingual exploration of knowledge"
source: "https://aclanthology.org/2024.findings-acl.347/"
categories: ['llm-reasoning-and-knowledge-graph-benchmarks', 'llm-training-alignment-and-evaluation']
tags: ['knowledge-editing', 'cross-lingual', 'transformers', 'multilingual', 'factual-knowledge']
venue: "ACL 2024"
tldr: "Explores cross-lingual effectiveness of attention-based knowledge editing methods in large language models beyond MLP blocks."
---

# Mass-Editing Memory with Attention in Transformers: A cross-lingual exploration of knowledge

**Source**: [https://aclanthology.org/2024.findings-acl.347/](https://aclanthology.org/2024.findings-acl.347/)

**TLDR**: Explores cross-lingual effectiveness of attention-based knowledge editing methods in large language models beyond MLP blocks.

## Abstract

AbstractRecent research has explored methods for updating and modifying factual knowledge in large language models, often focusing on specific multi-layer perceptron blocks. This study expands on this work by examining the effectiveness of existing knowledge editing methods across languages and delving into the role of attention mechanisms in this process. Drawing from the insights gained, we propose Mass-Editing Memory with Attention in Transformers (MEMAT), a method that achieves significant improvements in all metrics while requiring minimal parameter modifications. MEMAT delivers a remarkable 10% increase in magnitude metrics, benefits languages not included in the training data and also demonstrates a high degree of portability. Our code and data are at https://github.com/dtamayo-nlp/MEMAT.