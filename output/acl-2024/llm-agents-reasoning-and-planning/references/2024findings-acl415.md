---
title: "RetrievalQA: Assessing Adaptive Retrieval-Augmented Generation for Short-form Open-Domain Question Answering"
source: "https://aclanthology.org/2024.findings-acl.415/"
pdf_url: ""
categories: ['llm-agents-reasoning-and-planning', 'llm-reasoning-and-knowledge-graph-benchmarks']
tags: ['retrieval-augmented-generation', 'adaptive-retrieval', 'open-domain-qa']
venue: "ACL 2024"
tldr: "Introduces RetrievalQA benchmark to evaluate adaptive retrieval-augmented generation systems on short-form open-domain question answering."
---

# RetrievalQA: Assessing Adaptive Retrieval-Augmented Generation for Short-form Open-Domain Question Answering

**Source**: [https://aclanthology.org/2024.findings-acl.415/](https://aclanthology.org/2024.findings-acl.415/)

**TLDR**: Introduces RetrievalQA benchmark to evaluate adaptive retrieval-augmented generation systems on short-form open-domain question answering.

## Abstract

AbstractAdaptive retrieval-augmented generation (ARAG) aims to dynamically determine the necessity of retrieval for queries instead of retrieving indiscriminately to enhance the efficiency and relevance of the sourced information. However, previous works largely overlook the evaluation of ARAG approaches, leading to their effectiveness being understudied. This work presents a benchmark, RetrievalQA, comprising 1,271 short-form questions covering new world and long-tail knowledge. The knowledge necessary to answer the questions is absent from LLMs; therefore, external information must be retrieved to answer correctly. This makes RetrievalQA a suitable testbed to evaluate existing ARAG methods. We observe that calibration-based methods heavily rely on threshold tuning, while vanilla prompting is inadequate for guiding LLMs to make reliable retrieval decisions. Based on our findings, we propose Time-Aware Adaptive Retrieval (TA-ARE), a simple yet effective method that helps LLMs assess the necessity of retrieval without calibration or additional training.