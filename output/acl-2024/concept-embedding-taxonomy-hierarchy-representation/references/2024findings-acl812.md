---
title: "A Unified Joint Approach with Topological Context Learning and Rule Augmentation for Knowledge Graph Completion"
source: "https://aclanthology.org/2024.findings-acl.812/"
pdf_url: ""
categories: ['llm-reasoning-and-knowledge-graph-benchmarks', 'concept-embedding-taxonomy-hierarchy-representation']
tags: ['knowledge-graph-completion', 'topological-context', 'rule-augmentation']
venue: "ACL 2024"
tldr: "A unified approach combining topological context learning and rule augmentation improves knowledge graph completion by enriching relational representations."
---

# A Unified Joint Approach with Topological Context Learning and Rule Augmentation for Knowledge Graph Completion

**Source**: [https://aclanthology.org/2024.findings-acl.812/](https://aclanthology.org/2024.findings-acl.812/)

**TLDR**: A unified approach combining topological context learning and rule augmentation improves knowledge graph completion by enriching relational representations.

## Abstract

AbstractKnowledge graph completion (KGC) task is to infer the missing knowledge in the knowledge graph based on known factual triples. However, present KGC approaches still face the following two challenges. Those methods perform simple linear update on relation representation, and only local neighborhood information is aggregated, which makes it difficult to capture logic semantic between relations and global topological context information. To tackle the above challenges, we propose a unified joint approach with Topological Context learning and Rule Augmentation (TCRA) for KGC. The TCRA framework consists of an entity topological context learning mechanism based on dual-branch hierarchical graph attention network, and a relation rule context learning mechanism based on Rule-Transformer and rule-to-relation aggregator. The former mechanism encodes the topological structure features of entities, aggregates the local neighborhood topological context information of entities on the three levels (entity, relation and triple), and build clusters of global head or tail entities related to the same relation. It can capture the local and global topological context information of entities related to the same relation. The latter mechanism introduces chain-like Horn rules as the context information of relations, and encodes the logical semantic of relations to enrich the relation representation. Experimental performances on three benchmark datasets FB15k-237, WN18RR and Kinship indicate the effectiveness and superiority of our proposed approach. The codes are publicly available.