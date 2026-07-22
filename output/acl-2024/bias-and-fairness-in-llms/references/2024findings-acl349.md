---
title: "All Languages Matter: On the Multilingual Safety of LLMs"
source: "https://aclanthology.org/2024.findings-acl.349/"
categories: ['llm-security-robustness-and-detection', 'bias-and-fairness-in-llms']
tags: ['multilingual-safety', 'LLM-benchmark', 'harmful-content']
venue: "ACL 2024"
tldr: "Introduces the first multilingual safety benchmark to evaluate LLM safety across many languages beyond English."
---

# All Languages Matter: On the Multilingual Safety of LLMs

**Source**: [https://aclanthology.org/2024.findings-acl.349/](https://aclanthology.org/2024.findings-acl.349/)

**TLDR**: Introduces the first multilingual safety benchmark to evaluate LLM safety across many languages beyond English.

## Abstract

AbstractSafety lies at the core of developing and deploying large language models (LLMs). However, previous safety benchmarks only concern the safety in one language, e.g. the majority language in the pretraining data such as English. In this work, we build the first multilingual safety benchmark for LLMs, XSafety, in response to the global deployment of LLMs in practice. XSafety covers 14 kinds of commonly used safety issues across 10 languages that span several language families. We utilize XSafety to empirically study the multilingual safety for 4 widely-used LLMs, including both close-API and open-source models. Experimental results show that all LLMs produce significantly more unsafe responses for non-English queries than English ones, indicating the necessity of developing safety alignment for non-English languages. In addition, we propose a simple and effective prompting method to improve the multilingual safety of ChatGPT by enhancing cross-lingual generalization of safety alignment. Our prompting method can significantly reduce the ratio of unsafe responses by 42% for non-English queries. We will release all the data and results to facilitate future research on LLMs’ safety.