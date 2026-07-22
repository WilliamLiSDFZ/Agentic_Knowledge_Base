---
title: "CodeInsight: A Curated Dataset of Practical Coding Solutions from Stack Overflow"
source: "https://aclanthology.org/2024.findings-acl.354/"
categories: ['code-llm-generation-and-evaluation', 'nlp-benchmark-design-and-interpretability']
tags: ['code-generation', 'Stack-Overflow-dataset', 'unit-tests']
venue: "ACL 2024"
tldr: "Introduces CodeInsight, a curated dataset of practical coding solutions from Stack Overflow with intent, code, and unit tests."
---

# CodeInsight: A Curated Dataset of Practical Coding Solutions from Stack Overflow

**Source**: [https://aclanthology.org/2024.findings-acl.354/](https://aclanthology.org/2024.findings-acl.354/)

**TLDR**: Introduces CodeInsight, a curated dataset of practical coding solutions from Stack Overflow with intent, code, and unit tests.

## Abstract

AbstractWe introduce a novel dataset tailored for code generation, aimed at aiding developers in common tasks. Our dataset provides examples that include a clarified intent, code snippets associated, and an average of three related unit tests. It encompasses a range of libraries such as Pandas, Numpy, and Regex, along with more than 70 standard libraries in Python code derived from Stack Overflow. Comprising 3,402 crafted examples by Python experts, our dataset is designed for both model finetuning and standalone evaluation. To complete unit tests evaluation, we categorize examples in order to get more fine grained analysis, enhancing the understanding of models’ strengths and weaknesses in specific coding tasks. The examples have been refined to reduce data contamination, a process confirmed by the performance of three leading models: Mistral 7B, CodeLLAMA 13B, and Starcoder 15B. We further investigate data-contamination testing GPT-4 performance on a part of our dataset. The benchmark can be accessed at anonymized address.