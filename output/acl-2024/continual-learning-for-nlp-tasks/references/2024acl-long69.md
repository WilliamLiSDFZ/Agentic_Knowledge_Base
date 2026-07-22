---
title: "TaSL: Continual Dialog State Tracking via Task Skill Localization and Consolidation"
source: "https://aclanthology.org/2024.acl-long.69/"
categories: ['continual-learning-for-nlp-tasks']
tags: ['continual-learning', 'dialogue-state-tracking', 'catastrophic-forgetting']
venue: "ACL 2024"
tldr: "Presents TaSL, a continual dialogue state tracking method using task skill localization to mitigate catastrophic forgetting."
---

# TaSL: Continual Dialog State Tracking via Task Skill Localization and Consolidation

**Source**: [https://aclanthology.org/2024.acl-long.69/](https://aclanthology.org/2024.acl-long.69/)

**TLDR**: Presents TaSL, a continual dialogue state tracking method using task skill localization to mitigate catastrophic forgetting.

## Abstract

AbstractA practical dialogue system requires the capacity for ongoing skill acquisition and adaptability to new tasks while preserving prior knowledge. However, current methods for Continual Dialogue State Tracking (DST), a crucial function of dialogue systems, struggle with the catastrophic forgetting issue and knowledge transfer between tasks. We present TaSL, a novel framework for task skill localization and consolidation that enables effective knowledge transfer without relying on memory replay. TaSL uses a novel group-wise technique to pinpoint task-specific and task-shared areas. Additionally, a fine-grained skill consolidation strategy protects task-specific knowledge from being forgotten while updating shared knowledge for bi-directional knowledge transfer. As a result, TaSL strikes a balance between preserving previous knowledge and excelling at new tasks. Comprehensive experiments on various backbones highlight the significant performance improvements of TaSL, with a 7.6% absolute increase in Avg. JGA and an 11% absolute rise in BWT metrics over existing state-of-the-art methods. The source code is provided for reproducibility.