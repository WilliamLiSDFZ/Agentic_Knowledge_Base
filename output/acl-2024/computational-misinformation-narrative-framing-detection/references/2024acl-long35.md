---
title: "Leveraging Codebook Knowledge with NLI and ChatGPT for Zero-Shot Political Relation Classification"
source: "https://aclanthology.org/2024.acl-long.35/"
categories: ['computational-misinformation-narrative-framing-detection', 'natural-language-processing-information-extraction']
tags: ['zero-shot-learning', 'political-relations', 'NLI']
venue: "ACL 2024"
tldr: "Zero-shot methods using codebook knowledge and ChatGPT are evaluated for classifying political relations in event ontologies."
---

# Leveraging Codebook Knowledge with NLI and ChatGPT for Zero-Shot Political Relation Classification

**Source**: [https://aclanthology.org/2024.acl-long.35/](https://aclanthology.org/2024.acl-long.35/)

**TLDR**: Zero-shot methods using codebook knowledge and ChatGPT are evaluated for classifying political relations in event ontologies.

## Abstract

AbstractIs it possible accurately classify political relations within evolving event ontologies without extensive annotations? This study investigates zero-shot learning methods that use expert knowledge from existing annotation codebook, and evaluates the performance of advanced ChatGPT (GPT-3.5/4) and a natural language inference (NLI)-based model called ZSP. ChatGPT uses codebook’s labeled summaries as prompts, whereas ZSP breaks down the classification task into context, event mode, and class disambiguation to refine task-specific hypotheses. This decomposition enhances interpretability, efficiency, and adaptability to schema changes. The experiments reveal ChatGPT’s strengths and limitations, and crucially show ZSP’s outperformance of dictionary-based methods and its competitive edge over some supervised models. These findings affirm the value of ZSP for validating event records and advancing ontology development. Our study underscores the efficacy of leveraging transfer learning and existing domain expertise to enhance research efficiency and scalability.