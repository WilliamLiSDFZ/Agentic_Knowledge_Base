---
title: "DynaSemble: Dynamic Ensembling of Textual and Structure-Based Models for Knowledge Graph Completion"
source: "https://aclanthology.org/2024.acl-short.20/"
categories: ['llm-reasoning-and-knowledge-graph-benchmarks', 'concept-embedding-taxonomy-hierarchy-representation']
tags: ['knowledge-graph-completion', 'dynamic-ensembling', 'textual-structural-models']
venue: "ACL 2024"
tldr: "Proposes DynaSemble, which dynamically ensembles textual and structure-based models for improved knowledge graph completion."
---

# DynaSemble: Dynamic Ensembling of Textual and Structure-Based Models for Knowledge Graph Completion

**Source**: [https://aclanthology.org/2024.acl-short.20/](https://aclanthology.org/2024.acl-short.20/)

**TLDR**: Proposes DynaSemble, which dynamically ensembles textual and structure-based models for improved knowledge graph completion.

## Abstract

AbstractWe consider two popular approaches to KnowledgeGraph Completion (KGC): textual modelsthat rely on textual entity descriptions, andstructure-based models that exploit the connectivitystructure of the Knowledge Graph(KG). Preliminary experiments show that theseapproaches have complementary strengths:structure-based models perform exceptionallywell when the gold answer is easily reachablefrom the query head in the KG, while textualmodels exploit descriptions to give goodperformance even when the gold answer isnot easily reachable. In response, we proposeDynaSemble, a novel method for learningquery-dependent ensemble weights to combinethese approaches by using the distributions ofscores assigned by the models in the ensembleto all candidate entities. DynaSemble achievesstate-of-the-art results on three standard KGCdatasets, with up to 6.8 pt MRR and 8.3 ptHits@1 gains over the best baseline model forthe WN18RR dataset.