---
title: "CogMG: Collaborative Augmentation Between Large Language Model and Knowledge Graph"
source: "https://aclanthology.org/2024.acl-demos.35/"
categories: ['llm-reasoning-and-knowledge-graph-benchmarks', 'llm-hallucination-detection-and-mitigation']
tags: ['knowledge-graph', 'hallucination-reduction', 'collaborative-augmentation']
venue: "ACL 2024"
tldr: "CogMG collaboratively augments LLMs with knowledge graphs to reduce hallucinations in question-answering applications."
---

# CogMG: Collaborative Augmentation Between Large Language Model and Knowledge Graph

**Source**: [https://aclanthology.org/2024.acl-demos.35/](https://aclanthology.org/2024.acl-demos.35/)

**TLDR**: CogMG collaboratively augments LLMs with knowledge graphs to reduce hallucinations in question-answering applications.

## Abstract

AbstractLarge language models have become integral to question-answering applications despite their propensity for generating hallucinations and factually inaccurate content. Querying knowledge graphs to reduce hallucinations in LLM meets the challenge of incomplete knowledge coverage in knowledge graphs. On the other hand, updating knowledge graphs by information extraction and knowledge graph completion faces the knowledge update misalignment issue. In this work, we introduce a collaborative augmentation framework, CogMG, leveraging knowledge graphs to address the limitations of LLMs in QA scenarios, explicitly targeting the problems of incomplete knowledge coverage and knowledge update misalignment. The LLMs identify and decompose required knowledge triples that are not present in the KG, enriching them and aligning updates with real-world demands. We demonstrate the efficacy of this approach through a supervised fine-tuned LLM within an agent framework, showing significant improvements in reducing hallucinations and enhancing factual accuracy in QA responses. Our code and video are publicly available.