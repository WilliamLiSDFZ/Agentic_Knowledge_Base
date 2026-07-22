---
title: "Investigating the Impact of Data Contamination of Large Language Models in Text-to-SQL translation"
source: "https://aclanthology.org/2024.findings-acl.827/"
categories: ['text-to-sql-parsing-and-benchmarks', 'web-data-quality-and-llm-evaluation']
tags: ['text-to-sql', 'data-contamination', 'benchmark-leakage']
venue: "ACL 2024"
tldr: "Investigates how data contamination in training corpora affects LLM performance on Text-to-SQL benchmarks, questioning whether translation ability reflects true generalization."
---

# Investigating the Impact of Data Contamination of Large Language Models in Text-to-SQL translation

**Source**: [https://aclanthology.org/2024.findings-acl.827/](https://aclanthology.org/2024.findings-acl.827/)

**TLDR**: Investigates how data contamination in training corpora affects LLM performance on Text-to-SQL benchmarks, questioning whether translation ability reflects true generalization.

## Abstract

AbstractUnderstanding textual description to generate code seems to be an achieved capability of instruction-following Large Language Models (LLMs) in zero-shot scenario. However, there is a severe possibility that this translation ability may be influenced by having seen target textual descriptions and the related code. This effect is known as Data Contamination.In this study, we investigate the impact of Data Contamination on the performance of GPT-3.5 in the Text-to-SQL code-generating tasks. Hence, we introduce a novel method to detect Data Contamination in GPTs and examine GPT-3.5’s Text-to-SQL performances using the known Spider Dataset and our new unfamiliar dataset Termite. Furthermore, we analyze GPT-3.5’s efficacy on databases with modified information via an adversarial table disconnection (ATD) approach, complicating Text-to-SQL tasks by removing structural pieces of information from the database. Our results indicate a significant performance drop in GPT-3.5 on the unfamiliar Termite dataset, even with ATD modifications, highlighting the effect of Data Contamination on LLMs in Text-to-SQL translation tasks.