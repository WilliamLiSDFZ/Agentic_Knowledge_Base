---
title: "Continual Dialogue State Tracking via Reason-of-Select Distillation"
source: "https://aclanthology.org/2024.findings-acl.422/"
categories: ['continual-learning-for-nlp-tasks']
tags: ['dialogue-state-tracking', 'continual-learning', 'knowledge-distillation']
venue: "ACL 2024"
tldr: "Addresses continual dialogue state tracking by distilling reasoning via a reason-of-select approach to prevent forgetting."
---

# Continual Dialogue State Tracking via Reason-of-Select Distillation

**Source**: [https://aclanthology.org/2024.findings-acl.422/](https://aclanthology.org/2024.findings-acl.422/)

**TLDR**: Addresses continual dialogue state tracking by distilling reasoning via a reason-of-select approach to prevent forgetting.

## Abstract

AbstractAn ideal dialogue system requires continuous skill acquisition and adaptation to new tasks while retaining prior knowledge. Dialogue State Tracking (DST), vital in these systems, often involves learning new services, confronting catastrophic forgetting and a critical capability loss termed the “Value Selection Quandary”. To address these challenges, we introduce the Reason-of-Select (RoS) distillation method by enhancing smaller models with a novel “meta-reasoning” capability. Meta-reasoning, employing an enhanced multi-domain perspective, combines fragments of meta-knowledge from domain-specific dialogues during continual learning, transcending traditional single-perspective reasoning. This domain bootstrapping process enhances the model’s ability to dissect intricate dialogues from multiple possible values, and its domain-agnostic property aligns data distribution across different domains, effectively mitigating forgetting. Besides, two novel improvements, “multi-value resolution” strategy and Semantic Contrastive Reasoning Selection method, significantly enhance RoS by generating DST-specific selection chains and mitigating hallucinations in teachers’ reasoning, ensuring effective and reliable knowledge transfer. Extensive experiments validate the exceptional performance and robust generalization capabilities of our method.