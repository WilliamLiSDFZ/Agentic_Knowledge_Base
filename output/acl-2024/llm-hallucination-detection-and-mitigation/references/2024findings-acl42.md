---
title: "BIDER: Bridging Knowledge Inconsistency for Efficient Retrieval-Augmented LLMs via Key Supporting Evidence"
source: "https://aclanthology.org/2024.findings-acl.42/"
pdf_url: ""
categories: ['llm-hallucination-detection-and-mitigation', 'llm-agents-reasoning-and-planning']
tags: ['retrieval-augmented-generation', 'knowledge-inconsistency', 'open-domain-qa', 'evidence-extraction', 'llm']
venue: "ACL 2024"
tldr: "BIDER bridges knowledge inconsistency in retrieval-augmented LLMs by extracting key supporting evidence to improve answer accuracy."
---

# BIDER: Bridging Knowledge Inconsistency for Efficient Retrieval-Augmented LLMs via Key Supporting Evidence

**Source**: [https://aclanthology.org/2024.findings-acl.42/](https://aclanthology.org/2024.findings-acl.42/)

**TLDR**: BIDER bridges knowledge inconsistency in retrieval-augmented LLMs by extracting key supporting evidence to improve answer accuracy.

## Abstract

AbstractRetrieval-augmented large language models (LLMs) have demonstrated efficacy in knowledge-intensive tasks such as open-domain QA, addressing inherent challenges in knowledge update and factual inadequacy.However, inconsistencies between retrieval knowledge and the necessary knowledge for LLMs, leading to a decline in LLM’s answer quality. This paper introduces BIDER, an approach that refines retrieval documents into Key Supporting Evidence (KSE) through knowledge synthesis, supervised fine-tuning (SFT), and preference alignment. We train BIDER by learning from crafting KSE, while maximizing its output to align with LLM’s information acquisition preferences through reinforcement learning. Evaluations across five datasets show BIDER boosts LLMs’ answer quality by 7% while reducing input content length in retrieval documents by 80%, outperforming existing methods. The proposed KSE simulation effectively equips LLMs with essential information for accurate question answering.