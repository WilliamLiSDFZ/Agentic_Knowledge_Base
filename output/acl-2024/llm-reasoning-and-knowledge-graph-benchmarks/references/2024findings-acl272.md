---
title: "Enhancing Hyperbolic Knowledge Graph Embeddings via Lorentz Transformations"
source: "https://aclanthology.org/2024.findings-acl.272/"
categories: ['llm-reasoning-and-knowledge-graph-benchmarks', 'concept-embedding-taxonomy-hierarchy-representation']
tags: ['knowledge-graph-embedding', 'hyperbolic-space', 'Lorentz-transformation', 'link-prediction', 'hierarchical']
venue: "ACL 2024"
tldr: "Enhances hyperbolic knowledge graph embeddings by incorporating Lorentz transformations to better capture relational hierarchies."
---

# Enhancing Hyperbolic Knowledge Graph Embeddings via Lorentz Transformations

**Source**: [https://aclanthology.org/2024.findings-acl.272/](https://aclanthology.org/2024.findings-acl.272/)

**TLDR**: Enhances hyperbolic knowledge graph embeddings by incorporating Lorentz transformations to better capture relational hierarchies.

## Abstract

AbstractKnowledge Graph Embedding (KGE) is a powerful technique for predicting missing links in Knowledge Graphs (KGs) by learning the entities and relations. Hyperbolic space has emerged as a promising embedding space for KGs due to its ability to represent hierarchical data. Nevertheless, most existing hyperbolic KGE methods rely on tangent approximation and are not fully hyperbolic, resulting in distortions and inaccuracies. To overcome this limitation, we propose LorentzKG, a fully hyperbolic KGE method that represents entities as points in the Lorentz model and represents relations as the intrinsic transformation—the Lorentz transformations between entities. We demonstrate that the Lorentz transformation, which can be decomposed into Lorentz rotation/reflection and Lorentz boost, captures various types of relations including hierarchical structures. Experimental results show that our LorentzKG achieves state-of-the-art performance.