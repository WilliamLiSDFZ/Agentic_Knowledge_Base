---
title: "StatBot.Swiss: Bilingual Open Data Exploration in Natural Language"
source: "https://aclanthology.org/2024.findings-acl.326/"
pdf_url: ""
categories: ['text-to-sql-parsing-and-benchmarks', 'language-technology-cultural-linguistic-diversity']
tags: ['text-to-sql', 'bilingual', 'open-data']
venue: "ACL 2024"
tldr: "StatBot.Swiss is the first bilingual (German/French) Text-to-SQL dataset for exploring Swiss open statistical data in natural language."
---

# StatBot.Swiss: Bilingual Open Data Exploration in Natural Language

**Source**: [https://aclanthology.org/2024.findings-acl.326/](https://aclanthology.org/2024.findings-acl.326/)

**TLDR**: StatBot.Swiss is the first bilingual (German/French) Text-to-SQL dataset for exploring Swiss open statistical data in natural language.

## Abstract

AbstractThe potential for improvements brought by Large Language Models (LLMs) in Text-to-SQL systems is mostly assessed on monolingual English datasets. However, LLMs’ performance for other languages remains vastly unexplored. In this work, we release the StatBot.Swiss dataset, the first bilingual benchmark for evaluating Text-to-SQL systems based on real-world applications. The StatBot.Swiss dataset contains 455 natural language/SQL-pairs over 35 big databases with varying level of complexity for both English and German.We evaluate the performance of state-of-the-art LLMs such as GPT-3.5-Turbo and mixtral-8x7b-instruct for the Text-to-SQL translation task using an in-context learning approach. Our experimental analysis illustrates that current LLMs struggle to generalize well in generating SQL queries on our novel bilingual dataset.