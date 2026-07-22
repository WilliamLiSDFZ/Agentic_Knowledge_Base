---
title: "Uncovering Limitations of Large Language Models in Information Seeking from Tables"
source: "https://aclanthology.org/2024.findings-acl.82/"
categories: ['llm-reasoning-and-knowledge-graph-benchmarks', 'document-understanding-and-information-extraction']
tags: ['table-question-answering', 'llm-limitations', 'information-seeking']
venue: "ACL 2024"
tldr: "Uncovers and analyzes key limitations of LLMs when seeking information from structured tables in knowledge-based QA settings."
---

# Uncovering Limitations of Large Language Models in Information Seeking from Tables

**Source**: [https://aclanthology.org/2024.findings-acl.82/](https://aclanthology.org/2024.findings-acl.82/)

**TLDR**: Uncovers and analyzes key limitations of LLMs when seeking information from structured tables in knowledge-based QA settings.

## Abstract

AbstractTables are recognized for their high information density and widespread usage, serving as essential sources of information. Seeking information from tables (TIS) is a crucial capability for Large Language Models (LLMs), serving as the foundation of knowledge-based Q&A systems. However, this field presently suffers from an absence of thorough and reliable evaluation. This paper introduces a more reliable benchmark for Table Information Seeking (TabIS). To avoid the unreliable evaluation caused by text similarity-based metrics, TabIS adopts a single-choice question format (with two options per question) instead of a text generation format. We establish an effective pipeline for generating options, ensuring their difficulty and quality. Experiments conducted on 12 LLMs reveal that while the performance of GPT-4-turbo is marginally satisfactory, both other proprietary and open-source models perform inadequately. Further analysis shows that LLMs exhibit a poor understanding of table structures, and struggle to balance between TIS performance and robustness against pseudo-relevant tables (common in retrieval-augmented systems). These findings uncover the limitations and potential challenges of LLMs in seeking information from tables. We release our data and code to facilitate further research in this field.