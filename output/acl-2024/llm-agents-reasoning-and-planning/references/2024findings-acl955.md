---
title: "Chain-of-History Reasoning for Temporal Knowledge Graph Forecasting"
source: "https://aclanthology.org/2024.findings-acl.955/"
categories: ['llm-reasoning-and-knowledge-graph-benchmarks', 'llm-agents-reasoning-and-planning']
tags: ['temporal-knowledge-graph', 'forecasting', 'chain-of-thought']
venue: "ACL 2024"
tldr: "Proposes Chain-of-History reasoning to combine structural and semantic information from LLMs for improved temporal knowledge graph forecasting."
---

# Chain-of-History Reasoning for Temporal Knowledge Graph Forecasting

**Source**: [https://aclanthology.org/2024.findings-acl.955/](https://aclanthology.org/2024.findings-acl.955/)

**TLDR**: Proposes Chain-of-History reasoning to combine structural and semantic information from LLMs for improved temporal knowledge graph forecasting.

## Abstract

AbstractTemporal Knowledge Graph (TKG) forecasting aims to predict future facts based on given histories. Most recent graph-based models excel at capturing structural information within TKGs but lack semantic comprehension abilities. Nowadays, with the surge of LLMs, the LLM-based TKG prediction model has emerged. However, the existing LLM-based model exhibits three shortcomings: (1) It only focuses on the first-order history for prediction while ignoring high-order historical information, resulting in the provided information for LLMs being extremely limited. (2) LLMs struggle with optimal reasoning performance under heavy historical information loads. (3) For TKG prediction, the temporal reasoning capability of LLM alone is limited. To address the first two challenges, we propose Chain-of-History (CoH) reasoning which explores high-order histories step-by-step, achieving effective utilization of high-order historical information for LLMs on TKG prediction. To address the third issue, we design CoH as a plug-and-play module to enhance the performance of graph-based models for TKG prediction. Extensive experiments on three datasets and backbones demonstrate the effectiveness of CoH.