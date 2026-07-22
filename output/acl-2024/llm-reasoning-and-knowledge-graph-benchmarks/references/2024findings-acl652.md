---
title: "Developing PUGG for Polish: A Modern Approach to KBQA, MRC, and IR Dataset Construction"
source: "https://aclanthology.org/2024.findings-acl.652/"
pdf_url: ""
categories: ['llm-reasoning-and-knowledge-graph-benchmarks', 'nlp-for-asian-languages']
tags: ['polish-nlp', 'knowledge-base-qa', 'dataset-construction']
venue: "ACL 2024"
tldr: "PUGG introduces modern Polish datasets for KBQA, machine reading comprehension, and information retrieval using knowledge graphs."
---

# Developing PUGG for Polish: A Modern Approach to KBQA, MRC, and IR Dataset Construction

**Source**: [https://aclanthology.org/2024.findings-acl.652/](https://aclanthology.org/2024.findings-acl.652/)

**TLDR**: PUGG introduces modern Polish datasets for KBQA, machine reading comprehension, and information retrieval using knowledge graphs.

## Abstract

AbstractAdvancements in AI and natural language processing have revolutionized machine-human language interactions, with question answering (QA) systems playing a pivotal role. The knowledge base question answering (KBQA) task, utilizing structured knowledge graphs (KG), allows for handling extensive knowledge-intensive questions. However, a significant gap exists in KBQA datasets, especially for low-resource languages. Many existing construction pipelines for these datasets are outdated and inefficient in human labor, and modern assisting tools like Large Language Models (LLM) are not utilized to reduce the workload. To address this, we have designed and implemented a modern, semi-automated approach for creating datasets, encompassing tasks such as KBQA, Machine Reading Comprehension (MRC), and Information Retrieval (IR), tailored explicitly for low-resource environments. We executed this pipeline and introduced the PUGG dataset, the first Polish KBQA dataset, and novel datasets for MRC and IR. Additionally, we provide a comprehensive implementation, insightful findings, detailed statistics, and evaluation of baseline models.