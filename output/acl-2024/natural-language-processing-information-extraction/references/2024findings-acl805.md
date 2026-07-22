---
title: "GRADUAL: Granularity-aware Dual Prototype Learning for Better Few-Shot Relation Extraction"
source: "https://aclanthology.org/2024.findings-acl.805/"
pdf_url: ""
categories: ['natural-language-processing-information-extraction']
tags: ['few-shot-learning', 'relation-extraction', 'prototype-learning']
venue: "ACL 2024"
tldr: "GRADUAL introduces granularity-aware dual prototype learning to address inconsistent representations in few-shot relation extraction tasks."
---

# GRADUAL: Granularity-aware Dual Prototype Learning for Better Few-Shot Relation Extraction

**Source**: [https://aclanthology.org/2024.findings-acl.805/](https://aclanthology.org/2024.findings-acl.805/)

**TLDR**: GRADUAL introduces granularity-aware dual prototype learning to address inconsistent representations in few-shot relation extraction tasks.

## Abstract

AbstractRecent studies have shown that fusing text labels and context sentences is an effective method for learning prototype representations in few-shot relation extraction. However, the **inconsistency of prototype representations** across different few-shot tasks persists due to different context sentences for the same relation, even with the integration of text labels into prototype representations. Conversely, the text label for each relation is unique and consistent, 1)which prompts us to propose a **dual prototype learning method**. Unlike previous methods that only construct support-based prototypes, we additionally construct label-based prototypes. Furthermore, we introduce a graph-based prototype adjustment module to construct topological information between support-based and label-based prototypes, thereby generating a more effective similarity measure through a simple linear combination. In addition, relations of different granularities have different distribution widths in the same semantic space, the **imbalanced distribution in the semantic space** leads to a lack of comparability among relations. To create a more discriminative semantic space, 2)we propose a **granularity-aware prototype learning method** that unifies the distribution width of relations, making relations of different granularities have similar distribution widths. Experimental results on two public benchmark datasets show that our proposed methods achieve state-of-the-art performance in few-shot relation classification.