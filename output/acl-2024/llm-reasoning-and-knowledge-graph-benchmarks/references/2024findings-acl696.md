---
title: "MusTQ: A Temporal Knowledge Graph Question Answering Dataset for Multi-Step Temporal Reasoning"
source: "https://aclanthology.org/2024.findings-acl.696/"
pdf_url: ""
categories: ['llm-reasoning-and-knowledge-graph-benchmarks', 'llm-agents-reasoning-and-planning']
tags: ['temporal-knowledge-graph', 'question-answering', 'multi-step-reasoning']
venue: "ACL 2024"
tldr: "MusTQ introduces a TKGQA dataset requiring multi-step temporal reasoning over dynamic knowledge graphs."
---

# MusTQ: A Temporal Knowledge Graph Question Answering Dataset for Multi-Step Temporal Reasoning

**Source**: [https://aclanthology.org/2024.findings-acl.696/](https://aclanthology.org/2024.findings-acl.696/)

**TLDR**: MusTQ introduces a TKGQA dataset requiring multi-step temporal reasoning over dynamic knowledge graphs.

## Abstract

AbstractQuestion answering over temporal knowledge graphs (TKGQA) is an emerging topic, which has attracted increasing interest since it considers the dynamic knowledge in the world. Several datasets along with model developments are proposed in the TKGQA research field. However, existing studies generally focus on fact-centered reasoning, with limited attention to temporal reasoning. To tackle the intricate and comprehensive nature of temporal reasoning, we propose a new TKGQA dataset, MusTQ, which contains 666K multi-step temporal reasoning questions as well as a TKG. The multi-step temporal reasoning is established based on six basic temporal reasoning types derived from a well-established measure theory. Using MusTQ, we evaluate previous TKGQA methods and find that they typically fall short in multi-step temporal reasoning. Furthermore, we propose a TKGQA model, MusTKGQA, which enhances multi-step reasoning ability with entity-time attention mechanism and optimized temporal knowledge graph representation. Extensive experiments on MusTQ show that our model achieves state-of-the-art multi-step temporal reasoning performance.