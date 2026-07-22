---
title: "Knowledge-to-SQL: Enhancing SQL Generation with Data Expert LLM"
source: "https://aclanthology.org/2024.findings-acl.653/"
categories: ['text-to-sql-parsing-and-benchmarks']
tags: ['text-to-SQL', 'knowledge-augmentation', 'database']
venue: "ACL 2024"
tldr: "Knowledge-to-SQL enhances SQL generation by incorporating a data expert LLM to supply domain-specific knowledge missing from schemas."
---

# Knowledge-to-SQL: Enhancing SQL Generation with Data Expert LLM

**Source**: [https://aclanthology.org/2024.findings-acl.653/](https://aclanthology.org/2024.findings-acl.653/)

**TLDR**: Knowledge-to-SQL enhances SQL generation by incorporating a data expert LLM to supply domain-specific knowledge missing from schemas.

## Abstract

AbstractGenerating accurate SQL queries for user questions (text-to-SQL) has been a long-standing challenge since it requires a deep understanding of both the user’s question and the corresponding database schema in order to retrieve the desired content accurately. Existing methods rely on the comprehensive capability of large language models (LLMs) to generate the SQL. However, some necessary knowledge is not explicitly included in the database schema and user question or has been learned by LLMs. Thus, the generated SQL of the knowledge-insufficient questions may be inaccurate, negatively influencing the text-to-SQL models’ performance and robustness. To address this challenge, we propose the Knowledge-to-SQL framework, which employs tailored Data Expert LLM (DELLM) to provide helpful knowledge for all text-to-SQL models. Specifically, we introduce the detailed implementation of DELLM regarding table reading and the basic fine-tuning process. We further propose a Preference Learning via Database Feedback (PLDBF) strategy, refining the DELLM to generate more helpful knowledge for LLMs. Extensive experiments verify that DELLM can enhance the state-of-the-art approaches for text-to-SQL tasks. The corresponding code of DELLM is released for further research.