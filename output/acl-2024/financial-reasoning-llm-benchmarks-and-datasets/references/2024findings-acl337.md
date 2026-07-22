---
title: "Benchmarking Large Language Models on CFLUE - A Chinese Financial Language Understanding Evaluation Dataset"
source: "https://aclanthology.org/2024.findings-acl.337/"
pdf_url: ""
categories: ['financial-reasoning-llm-benchmarks-and-datasets']
tags: ['chinese-finance', 'llm-benchmark', 'financial-language-understanding']
venue: "ACL 2024"
tldr: "CFLUE is a new Chinese financial language understanding benchmark for evaluating LLMs on domain-specific financial NLP tasks."
---

# Benchmarking Large Language Models on CFLUE - A Chinese Financial Language Understanding Evaluation Dataset

**Source**: [https://aclanthology.org/2024.findings-acl.337/](https://aclanthology.org/2024.findings-acl.337/)

**TLDR**: CFLUE is a new Chinese financial language understanding benchmark for evaluating LLMs on domain-specific financial NLP tasks.

## Abstract

AbstractIn light of recent breakthroughs in large language models (LLMs) that have revolutionized natural language processing (NLP), there is an urgent need for new benchmarks to keep pace with the fast development of LLMs. In this paper, we propose CFLUE, the Chinese Financial Language Understanding Evaluation benchmark, designed to assess the capability of LLMs across various dimensions. Specifically, CFLUE provides datasets tailored for both knowledge assessment and application assessment. In knowledge assessment, it consists of 38K+ multiple-choice questions with associated solution explanations. These questions serve dual purposes: answer prediction and question reasoning. In application assessment, CFLUE features 16K+ test instances across distinct groups of NLP tasks such as text classification, machine translation, relation extraction, reading comprehension, and text generation. Upon CFLUE, we conduct a thorough evaluation of representative LLMs. The results reveal that only Qwen-72B, GPT-4, and GPT-4-turbo achieve an accuracy exceeding 60% in answer prediction for knowledge assessment, suggesting that there is still substantial room for improvement in current LLMs. In application assessment, while GPT-4 and GPT-4-turbo rank as the top two performers on average, their significant advantage over open-source LLMs is noticeably diminished, given that Qwen-72B achieves the best performance in 2 out of 5 tasks. The datasets and scripts associated with CFLUE are openly accessible at https://github.com/aliyun/cflue.