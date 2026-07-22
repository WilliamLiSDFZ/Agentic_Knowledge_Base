---
title: "Cutting Off the Head Ends the Conflict: A Mechanism for Interpreting and Mitigating Knowledge Conflicts in Language Models"
source: "https://aclanthology.org/2024.findings-acl.70/"
pdf_url: ""
categories: ['llm-hallucination-detection-and-mitigation']
tags: ['knowledge-conflicts', 'retrieval-augmentation', 'attention-heads']
venue: "ACL 2024"
tldr: "This paper identifies a mechanism by which specific attention heads cause knowledge conflicts between internal memory and external context in LLMs and proposes a mitigation strategy."
---

# Cutting Off the Head Ends the Conflict: A Mechanism for Interpreting and Mitigating Knowledge Conflicts in Language Models

**Source**: [https://aclanthology.org/2024.findings-acl.70/](https://aclanthology.org/2024.findings-acl.70/)

**TLDR**: This paper identifies a mechanism by which specific attention heads cause knowledge conflicts between internal memory and external context in LLMs and proposes a mitigation strategy.

## Abstract

AbstractRecently, retrieval augmentation and tool augmentation have demonstrated a remarkable capability to expand the internal memory boundaries of language models (LMs) by providing external context. However, internal memory and external context inevitably clash, leading to knowledge conflicts within LMs. In this paper, we aim to interpret the mechanism of knowledge conflicts through the lens of information flow, and then mitigate conflicts by precise interventions at the pivotal point. We find there are some attention heads with opposite effects in the later layers, where memory heads can recall knowledge from internal memory, and context heads can retrieve knowledge from external context. Moreover, we reveal that the pivotal point at which knowledge conflicts emerge in LMs is the integration of inconsistent information flows by memory heads and context heads. Inspired by the insights, we propose a novel method called Pruning Head via PatH PatcHing (PH3), which can efficiently mitigate knowledge conflicts by pruning conflicting attention heads without updating model parameters. PH3 can flexibly control eight LMs to use internal memory (↑ 44.0%) or external context (↑ 38.5%). Moreover, PH3 can also improve the performance of LMs on open-domain QA tasks. We also conduct extensive experiments to demonstrate the cross-model, cross-relation, and cross-format generalization of our method. Our code is publicly available at https://github.com/jinzhuoran/MConflict/.