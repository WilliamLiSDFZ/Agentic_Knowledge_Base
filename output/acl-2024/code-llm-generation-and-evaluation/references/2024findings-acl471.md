---
title: "NaturalCodeBench: Examining Coding Performance Mismatch on HumanEval and Natural User Queries"
source: "https://aclanthology.org/2024.findings-acl.471/"
pdf_url: ""
categories: ['code-llm-generation-and-evaluation']
tags: ['code-generation', 'benchmark', 'llm-evaluation']
venue: "ACL 2024"
tldr: "NaturalCodeBench reveals a performance mismatch between LLMs on standard coding benchmarks and real-world natural user coding queries."
---

# NaturalCodeBench: Examining Coding Performance Mismatch on HumanEval and Natural User Queries

**Source**: [https://aclanthology.org/2024.findings-acl.471/](https://aclanthology.org/2024.findings-acl.471/)

**TLDR**: NaturalCodeBench reveals a performance mismatch between LLMs on standard coding benchmarks and real-world natural user coding queries.

## Abstract

AbstractLarge language models (LLMs) have manifested strong ability to generate codes for productive activities. However, current benchmarks for code synthesis, such as HumanEval, MBPP, and DS-1000, are predominantly oriented towards introductory tasks on algorithm and data science, insufficiently satisfying challenging requirements prevalent in real-world coding. To fill this gap, we propose NaturalCodeBench (NCB), a challenging code benchmark designed to mirror the complexity and variety of scenarios in real coding tasks. NCB comprises 402 high-quality problems in Python and Java, meticulously selected from natural user queries from online coding services, covering 6 different domains. Noting the extraordinary difficulty in creating testing cases for real-world queries, we also introduce a semi-automated pipeline to enhance the efficiency of test case construction. Comparing with manual solutions, it achieves an efficiency increase of more than 4 times. Our systematic experiments on 39 LLMs find that performance gaps on NCB between models with close HumanEval scores could still be significant, indicating a lack of focus on practical code synthesis scenarios or over-specified optimization on HumanEval. On the other hand, even the best-performing GPT-4 is still far from satisfying on NCB. The evaluation toolkit and development set are available at https://github.com/THUDM/NaturalCodeBench.