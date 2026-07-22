---
title: "Discerning and Resolving Knowledge Conflicts through Adaptive Decoding with Contextual Information-Entropy Constraint"
source: "https://aclanthology.org/2024.findings-acl.234/"
categories: ['llm-hallucination-detection-and-mitigation']
tags: ['knowledge-conflicts', 'adaptive-decoding', 'contextual-information-entropy']
venue: "ACL 2024"
tldr: "Proposes adaptive decoding with contextual information-entropy constraints to resolve conflicts between parametric and contextual knowledge in LLMs."
---

# Discerning and Resolving Knowledge Conflicts through Adaptive Decoding with Contextual Information-Entropy Constraint

**Source**: [https://aclanthology.org/2024.findings-acl.234/](https://aclanthology.org/2024.findings-acl.234/)

**TLDR**: Proposes adaptive decoding with contextual information-entropy constraints to resolve conflicts between parametric and contextual knowledge in LLMs.

## Abstract

AbstractLarge language models (LLMs) internalize enormous parametric knowledge during pre-training. Concurrently, realistic applications necessitate external contextual knowledge to aid models on the underlying tasks. This raises a crucial dilemma known as knowledge conflicts, where the contextual knowledge clashes with the parametric knowledge. However, existing decoding works are specialized in resolving knowledge conflicts and could inadvertently deteriorate performance in absence of conflicts. In this paper, we propose an adaptive decoding method, termed as contextual information-entropy constraint decoding (COIECD), to discern whether the knowledge conflicts occur and resolve them. It can improve the model’s faithfulness to conflicting context, and simultaneously maintain high performance among non-conflicting context. Our experiments show that COIECD exhibits strong performance and robustness over knowledge conflicts in realistic datasets.