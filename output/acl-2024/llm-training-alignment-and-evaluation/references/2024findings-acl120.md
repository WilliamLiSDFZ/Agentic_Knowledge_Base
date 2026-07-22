---
title: "Enhancing Text-to-SQL Parsing through Question Rewriting and Execution-Guided Refinement"
source: "https://aclanthology.org/2024.findings-acl.120/"
categories: ['text-to-sql-parsing-and-benchmarks', 'llm-training-alignment-and-evaluation']
tags: ['text-to-sql', 'question-rewriting', 'execution-feedback']
venue: "ACL 2024"
tldr: "DART-SQL enhances LLM-based text-to-SQL by rewriting ambiguous questions and refining SQL queries using execution feedback."
---

# Enhancing Text-to-SQL Parsing through Question Rewriting and Execution-Guided Refinement

**Source**: [https://aclanthology.org/2024.findings-acl.120/](https://aclanthology.org/2024.findings-acl.120/)

**TLDR**: DART-SQL enhances LLM-based text-to-SQL by rewriting ambiguous questions and refining SQL queries using execution feedback.

## Abstract

AbstractLarge Language Model (LLM)-based approach has become the mainstream for Text-to-SQL task and achieves remarkable performance. In this paper, we augment the existing prompt engineering methods by exploiting the database content and execution feedback. Specifically, we introduce DART-SQL, which comprises two key components: (1) Question Rewriting: DART-SQL rewrites natural language questions by leveraging database content information to eliminate ambiguity. (2) Execution-Guided Refinement: DART-SQL incorporates database content information and utilizes the execution results of the generated SQL to iteratively refine the SQL. We apply this framework to the two LLM-based approaches (DAIL-SQL and C3) and test it on four widely used benchmarks (Spider-dev, Spider-test, Realistic and DK). Experiments show that our framework for DAIL-SQL and C3 achieves an average improvement of 12.41% and 5.38%, respectively, in terms of execution accuracy(EX) metric.