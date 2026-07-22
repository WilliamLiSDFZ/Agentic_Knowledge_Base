---
title: "Encoding Hierarchical Schema via Concept Flow for Multifaceted Ideology Detection"
source: "https://aclanthology.org/2024.findings-acl.172/"
pdf_url: ""
categories: ['hierarchical-text-classification-methods']
tags: ['ideology-detection', 'concept-flow', 'hierarchical-schema']
venue: "ACL 2024"
tldr: "Encodes hierarchical schema via concept flow to detect ideological leanings across multiple facets."
---

# Encoding Hierarchical Schema via Concept Flow for Multifaceted Ideology Detection

**Source**: [https://aclanthology.org/2024.findings-acl.172/](https://aclanthology.org/2024.findings-acl.172/)

**TLDR**: Encodes hierarchical schema via concept flow to detect ideological leanings across multiple facets.

## Abstract

AbstractMultifaceted ideology detection (MID) aims to detect the ideological leanings of texts towards multiple facets. Previous studies on ideology detection mainly focus on one generic facet and ignore label semantics and explanatory descriptions of ideologies, which are a kind of instructive information and reveal the specific concepts of ideologies. In this paper, we develop a novel concept semantics-enhanced framework for the MID task. Specifically, we propose a bidirectional iterative concept flow (BICo) method to encode multifaceted ideologies. BICo enables the concepts to flow across levels of the schema tree and enriches concept representations with multi-granularity semantics. Furthermore, we explore concept attentive matching and concept-guided contrastive learning strategies to guide the model to capture ideology features with the learned concept semantics. Extensive experiments on the benchmark dataset show that our approach achieves state-of-the-art performance in MID, including in the cross-topic scenario.