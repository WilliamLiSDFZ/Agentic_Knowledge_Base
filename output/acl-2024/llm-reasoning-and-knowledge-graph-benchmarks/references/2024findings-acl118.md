---
title: "Learning Low-dimensional Multi-domain Knowledge Graph Embedding via Dual Archimedean Spirals"
source: "https://aclanthology.org/2024.findings-acl.118/"
pdf_url: ""
categories: ['llm-reasoning-and-knowledge-graph-benchmarks', 'language-model-representations-and-embedding-spaces']
tags: ['knowledge-graph-embedding', 'multi-domain', 'low-dimensional']
venue: "ACL 2024"
tldr: "Dual Archimedean spiral embeddings improve multi-domain knowledge graph link prediction in low-dimensional spaces."
---

# Learning Low-dimensional Multi-domain Knowledge Graph Embedding via Dual Archimedean Spirals

**Source**: [https://aclanthology.org/2024.findings-acl.118/](https://aclanthology.org/2024.findings-acl.118/)

**TLDR**: Dual Archimedean spiral embeddings improve multi-domain knowledge graph link prediction in low-dimensional spaces.

## Abstract

AbstractKnowledge graph embedding (KGE) is extensively employed for link prediction by representing entities and relations as low-dimensional vectors. In real-world scenarios, knowledge graphs (KGs) usually encompass diverse domains, which poses challenges to KG representations. However, existing KGE methods rarely make domain constraints on the embedding distribution of multi-domain KGs, leading to the embedding overlapping of different domains and performance degradation of link prediction. To address this challenge, we propose Dual Archimedean Spiral Knowledge Graph Embedding (DuASE), a low-dimensional KGE model for multi-domain KGs. DuASE is inspired by our discovery that relation types can distinguish entities from different domains. Specifically, DuASE encodes entities with the same relation on the same Archimedean spiral, allowing it to differentiate the entities from different domains. To avoid embedding overlapping across domains, DuASE further makes the head and the tail spirals in the same triplet cluster to their respective domain space by a regularization function. Thus, DuASE can better capture the domain information and the dependencies between entities when modeling the multi-domain KGs, leading to improved KG representations. We validate the effectiveness of DuASE on the novel multi-domain dataset (n-MDKG) introduced in this study and three other benchmark datasets.