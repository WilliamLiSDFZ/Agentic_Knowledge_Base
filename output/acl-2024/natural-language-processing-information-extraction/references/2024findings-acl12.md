---
title: "Text2DB: Integration-Aware Information Extraction with Large Language Model Agents"
source: "https://aclanthology.org/2024.findings-acl.12/"
pdf_url: ""
categories: ['natural-language-processing-information-extraction', 'text-to-sql-parsing-and-benchmarks']
tags: ['information-extraction', 'llm-agents', 'database-integration']
venue: "ACL 2024"
tldr: "Text2DB reformulates information extraction as an integration-aware task using LLM agents to align extracted knowledge with downstream database needs."
---

# Text2DB: Integration-Aware Information Extraction with Large Language Model Agents

**Source**: [https://aclanthology.org/2024.findings-acl.12/](https://aclanthology.org/2024.findings-acl.12/)

**TLDR**: Text2DB reformulates information extraction as an integration-aware task using LLM agents to align extracted knowledge with downstream database needs.

## Abstract

AbstractThe task of information extraction (IE) is to extract structured knowledge from text. However, it is often not straightforward to utilize IE output due to the mismatch between the IE ontology and the downstream application needs. We propose a new formulation of IE, Text2DB, that emphasizes the integration of IE output and the target database (or knowledge base). Given a user instruction, a document set, and a database, our task requires the model to update the database with values from the document set to satisfy the user instruction. This task requires understanding user instructions for what to extract and adapting to the given DB/KB schema for how to extract on the fly. To evaluate this new task, we introduce a new benchmark featuring common demands such as data infilling, row population, and column addition. In addition, we propose an LLM agent framework OPAL (Observe-Plan-Analyze LLM) which includes an Observer component that interacts with the database, the Planner component that generates a code-based plan with calls to IE models, and the Analyzer component that provides feedback regarding code quality before execution. Experiments show that OPAL can successfully adapt to diverse database schemas by generating different code plans and calling the required IE models. We also highlight difficult cases such as dealing with large databases with complex dependencies and extraction hallucination, which we believe deserve further investigation.