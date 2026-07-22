---
title: "Before Generation, Align it! A Novel and Effective Strategy for Mitigating Hallucinations in Text-to-SQL Generation"
source: "https://aclanthology.org/2024.findings-acl.324/"
pdf_url: ""
categories: ['text-to-sql-parsing-and-benchmarks', 'llm-hallucination-detection-and-mitigation']
tags: ['text-to-sql', 'hallucination-mitigation', 'in-context-learning']
venue: "ACL 2024"
tldr: "A pre-generation alignment strategy reduces hallucinations in LLM-driven text-to-SQL generation via schema-aware prompting."
---

# Before Generation, Align it! A Novel and Effective Strategy for Mitigating Hallucinations in Text-to-SQL Generation

**Source**: [https://aclanthology.org/2024.findings-acl.324/](https://aclanthology.org/2024.findings-acl.324/)

**TLDR**: A pre-generation alignment strategy reduces hallucinations in LLM-driven text-to-SQL generation via schema-aware prompting.

## Abstract

AbstractLarge Language Models (LLMs) driven by In-Context Learning (ICL) have significantly improved the performance of text-to-SQL. Previous methods generally employ a two-stage reasoning framework, namely 1) schema linking and 2) logical synthesis, making the framework not only effective but also interpretable. Despite these advancements, the inherent bad nature of the generalization of LLMs often results in hallucinations, which limits the full potential of LLMs. In this work, we first identify and categorize the common types of hallucinations at each stage in text-to-SQL. We then introduce a novel strategy, Task Alignment (TA), designed to mitigate hallucinations at each stage. TA encourages LLMs to take advantage of experiences from similar tasks rather than starting the tasks from scratch. This can help LLMs reduce the burden of generalization, thereby mitigating hallucinations effectively. We further propose TA-SQL, a text-to-SQL framework based on this strategy. The experimental results and comprehensive analysis demonstrate the effectiveness and robustness of our framework. Specifically, it enhances the performance of the GPT-4 baseline by 21.23% relatively on BIRD dev and it yields significant improvements across six models and four mainstream, complex text-to-SQL benchmarks.