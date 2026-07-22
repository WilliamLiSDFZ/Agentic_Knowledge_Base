---
title: "FUSE: Measure-Theoretic Compact Fuzzy Set Representation for Taxonomy Expansion"
source: "https://aclanthology.org/2024.findings-acl.158/"
pdf_url: ""
categories: ['concept-embedding-taxonomy-hierarchy-representation', 'language-model-representations-and-embedding-spaces']
tags: ['taxonomy-expansion', 'fuzzy-set-representation', 'concept-embedding']
venue: "ACL 2024"
tldr: "FUSE proposes a measure-theoretic fuzzy set representation for taxonomy expansion that models semantic concepts with uncertainty-aware embeddings."
---

# FUSE: Measure-Theoretic Compact Fuzzy Set Representation for Taxonomy Expansion

**Source**: [https://aclanthology.org/2024.findings-acl.158/](https://aclanthology.org/2024.findings-acl.158/)

**TLDR**: FUSE proposes a measure-theoretic fuzzy set representation for taxonomy expansion that models semantic concepts with uncertainty-aware embeddings.

## Abstract

AbstractTaxonomy Expansion, which relies on modeling concepts and concept relations, can be formulated as a set representation learning task. The generalization of set, fuzzy set, incorporates uncertainty and measures the information within a semantic concept, making it suitable for concept modeling. Existing works usually model sets as vectors or geometric objects such as boxes, which are not closed under set operations. In this work, we propose a sound and efficient formulation of set representation learning based on its volume approximation as a fuzzy set. The resulting embedding framework, Fuzzy Set Embedding, satisfies all set operations and compactly approximates the underlying fuzzy set, hence preserving information while being efficient to learn, relying on minimum neural architecture. We empirically demonstrate the power of FUSE on the task of taxonomy expansion, where FUSE achieves remarkable improvements up to 23% compared with existing baselines. Our work marks the first attempt to understand and efficiently compute the embeddings of fuzzy sets.