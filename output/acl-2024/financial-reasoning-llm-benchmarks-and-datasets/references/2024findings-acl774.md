---
title: "FinTral: A Family of GPT-4 Level Multimodal Financial Large Language Models"
source: "https://aclanthology.org/2024.findings-acl.774/"
categories: ['financial-reasoning-llm-benchmarks-and-datasets', 'multimodal-language-vision-learning-systems']
tags: ['financial-llm', 'multimodal', 'domain-specific-pretraining']
venue: "ACL 2024"
tldr: "Introduces FinTral, a family of multimodal LLMs built on Mistral-7b and specialized for financial analysis across text, tabular, and image data."
---

# FinTral: A Family of GPT-4 Level Multimodal Financial Large Language Models

**Source**: [https://aclanthology.org/2024.findings-acl.774/](https://aclanthology.org/2024.findings-acl.774/)

**TLDR**: Introduces FinTral, a family of multimodal LLMs built on Mistral-7b and specialized for financial analysis across text, tabular, and image data.

## Abstract

AbstractWe introduce FinTral, a suite of state-of-the-art multimodal large language models (LLMs) built upon the Mistral-7b model and tailored for financial analysis. FinTral integrates textual, numerical, tabular, and image data. We enhance FinTral with domain-specific pretraining, instruction fine-tuning, and RLAIF training by exploiting a large collection of textual and visual datasets we curate for this work. We also introduce an extensive benchmark featuring nine tasks and 25 datasets for evaluation, including hallucinations in the financial domain. Our FinTral model trained with direct preference optimization employing advanced Tools and Retrieval methods, dubbed FinTral-DPO-T&R, demonstrates an exceptional zero-shot performance. It outperforms ChatGPT-3.5 in all tasks and surpasses GPT-4 in five out of nine tasks, marking a significant advancement in AI-driven financial technology. We also demonstrate that FinTral has the potential to excel in real-time analysis and decision-making in diverse financial contexts.