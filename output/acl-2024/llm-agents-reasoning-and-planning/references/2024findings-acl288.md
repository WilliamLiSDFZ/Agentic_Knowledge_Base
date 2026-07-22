---
title: "Unraveling and Mitigating Retriever Inconsistencies in Retrieval-Augmented Large Language Models"
source: "https://aclanthology.org/2024.findings-acl.288/"
categories: ['llm-hallucination-detection-and-mitigation', 'llm-agents-reasoning-and-planning']
tags: ['retrieval-augmented-generation', 'RAG', 'retriever-inconsistency', 'LLM', 'factuality']
venue: "ACL 2024"
tldr: "Investigates and mitigates example-level performance inconsistencies in retrieval-augmented LLMs caused by retriever unreliability."
---

# Unraveling and Mitigating Retriever Inconsistencies in Retrieval-Augmented Large Language Models

**Source**: [https://aclanthology.org/2024.findings-acl.288/](https://aclanthology.org/2024.findings-acl.288/)

**TLDR**: Investigates and mitigates example-level performance inconsistencies in retrieval-augmented LLMs caused by retriever unreliability.

## Abstract

AbstractAlthough Retrieval-Augmented Large Language Models (RALMs) demonstrate their superiority in terms of factuality, they do not consistently outperform the original retrieval-free Language Models (LMs). Our experiments reveal that this example-level performance inconsistency exists not only between retrieval-augmented and retrieval-free LM but also among different retrievers. To understand this phenomenon, we investigate the degeneration behavior of RALMs and theoretically decompose it into four categories. Further analysis based on our decomposition reveals that the innate difference in knowledge sources and the unpredictable degeneration of the reader model contribute most to the inconsistency. Drawing from our analysis, we introduce Ensemble of Retrievers (EoR), a trainable framework that can adaptively retrieve from different knowledge sources and effectively decrease unpredictable reader errors. Our experiments on Open Domain Question Answering show that EoR substantially improves performance over the RALM with a single retriever by considerably reducing inconsistent behaviors.