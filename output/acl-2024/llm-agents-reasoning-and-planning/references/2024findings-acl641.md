---
title: "Decomposition for Enhancing Attention: Improving LLM-based Text-to-SQL through Workflow Paradigm"
source: "https://aclanthology.org/2024.findings-acl.641/"
pdf_url: ""
categories: ['text-to-sql-parsing-and-benchmarks', 'llm-agents-reasoning-and-planning']
tags: ['text-to-SQL', 'LLM', 'in-context-learning', 'workflow', 'attention-decomposition']
venue: "ACL 2024"
tldr: "Introduces a workflow-based decomposition paradigm to reduce attention diffusion in LLM-driven text-to-SQL parsing."
---

# Decomposition for Enhancing Attention: Improving LLM-based Text-to-SQL through Workflow Paradigm

**Source**: [https://aclanthology.org/2024.findings-acl.641/](https://aclanthology.org/2024.findings-acl.641/)

**TLDR**: Introduces a workflow-based decomposition paradigm to reduce attention diffusion in LLM-driven text-to-SQL parsing.

## Abstract

AbstractIn-context learning of large-language models (LLMs) has achieved remarkable success in the field of natural language processing, while extensive case studies reveal that the single-step chain-of-thought prompting approach faces challenges such as attention diffusion and inadequate performance in complex tasks like text-to-SQL. To improve the contextual learning capabilities of LLMs in text-to-SQL, a workflow paradigm method is proposed, aiming to enhance the attention and problem-solving scope of LLMs through decomposition. Specifically, the information determination module for eliminating redundant information and the brand-new prompt structure based on problem classification greatly enhance the model’s attention. Additionally, the inclusion of self-correction and active learning modules greatly expands the problem-solving scope of LLMs, hence improving the upper limit of LLM-based approaches. Extensive experiments conducted on three datasets demonstrate that our approach outperforms other methods by a significant margin. About 2-3 percentage point improvements compared to the existing baseline on the Spider Dev, Spider-Realistic, and Bird Dev datasets and new SOTA results on the Spider Test dataset are achieved. Our code is available on GitHub: https://github.com/FlyingFeather/DEA-SQL.