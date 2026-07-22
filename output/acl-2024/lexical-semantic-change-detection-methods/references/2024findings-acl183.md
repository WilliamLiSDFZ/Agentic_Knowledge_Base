---
title: "Modeling Dynamic Topics in Chain-Free Fashion by Evolution-Tracking Contrastive Learning and Unassociated Word Exclusion"
source: "https://aclanthology.org/2024.findings-acl.183/"
categories: ['topic-modeling-and-essay-evaluation', 'lexical-semantic-change-detection-methods']
tags: ['dynamic-topic-models', 'contrastive-learning', 'evolution-tracking']
venue: "ACL 2024"
tldr: "Proposes evolution-tracking contrastive learning with unassociated word exclusion for better dynamic topic modeling."
---

# Modeling Dynamic Topics in Chain-Free Fashion by Evolution-Tracking Contrastive Learning and Unassociated Word Exclusion

**Source**: [https://aclanthology.org/2024.findings-acl.183/](https://aclanthology.org/2024.findings-acl.183/)

**TLDR**: Proposes evolution-tracking contrastive learning with unassociated word exclusion for better dynamic topic modeling.

## Abstract

AbstractDynamic topic models track the evolution of topics in sequential documents, which have derived various applications like trend analysis. However, existing models suffer from repetitive topic and unassociated topic issues, failing to reveal the evolution and hindering further applications. To address these issues, we break the tradition of simply chaining topics in existing work and propose a novel neural Chain-Free Dynamic Topic Model. We introduce a new evolution-tracking contrastive learning method that builds the similarity relations among dynamic topics. This not only tracks topic evolution but also maintains topic diversity, mitigating the repetitive topic issue. To avoid unassociated topics, we further present an unassociated word exclusion method that consistently excludes unassociated words from discovered topics. Extensive experiments demonstrate our model significantly outperforms state-of-the-art baselines, tracking topic evolution with high-quality topics, showing better performance on downstream tasks, and remaining robust to the hyperparameter for evolution intensities.