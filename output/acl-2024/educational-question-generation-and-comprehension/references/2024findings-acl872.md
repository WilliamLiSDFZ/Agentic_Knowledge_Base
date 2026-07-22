---
title: "Measuring Retrieval Complexity in Question Answering Systems"
source: "https://aclanthology.org/2024.findings-acl.872/"
pdf_url: ""
categories: ['llm-reasoning-and-knowledge-graph-benchmarks', 'educational-question-generation-and-comprehension']
tags: ['retrieval-complexity', 'question-answering', 'retrieval-difficulty', 'evaluation-metric']
venue: "ACL 2024"
tldr: "This paper proposes retrieval complexity, a novel metric to measure the difficulty of answering questions based on the completeness of retrieved documents."
---

# Measuring Retrieval Complexity in Question Answering Systems

**Source**: [https://aclanthology.org/2024.findings-acl.872/](https://aclanthology.org/2024.findings-acl.872/)

**TLDR**: This paper proposes retrieval complexity, a novel metric to measure the difficulty of answering questions based on the completeness of retrieved documents.

## Abstract

AbstractIn this paper, we investigate which questions are challenging for retrieval-based Question Answering (QA). We (i) propose retrieval complexity (RC), a novel metric conditioned on the completeness of retrieved documents, which measures the difficulty of answering questions, and (ii) propose an unsupervised pipeline to measure RC given an arbitrary retrieval system.Our proposed pipeline measures RC more accurately than alternative estimators, including LLMs, on six challenging QA benchmarks. Further investigation reveals that RC scores strongly correlate with both QA performance and expert judgment across five of the six studied benchmarks, indicating that RC is an effective measure of question difficulty.Subsequent categorization of high-RC questions shows that they span a broad set of question shapes, including multi-hop, compositional, and temporal QA, indicating that RC scores can categorize a new subset of complex questions. Our system can also have a major impact on retrieval-based systems by helping to identify more challenging questions on existing datasets.