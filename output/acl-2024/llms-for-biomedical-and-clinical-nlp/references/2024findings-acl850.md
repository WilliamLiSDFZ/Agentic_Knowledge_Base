---
title: "Evaluating Large Language Models for Health-related Queries with Presuppositions"
source: "https://aclanthology.org/2024.findings-acl.850/"
categories: ['llm-hallucination-detection-and-mitigation', 'llms-for-biomedical-and-clinical-nlp']
tags: ['health-misinformation', 'presuppositions', 'LLM-evaluation', 'factuality', 'robustness']
venue: "ACL 2024"
tldr: "UPHILL benchmarks LLMs on health-related queries with presuppositions to evaluate factual robustness against misinformation."
---

# Evaluating Large Language Models for Health-related Queries with Presuppositions

**Source**: [https://aclanthology.org/2024.findings-acl.850/](https://aclanthology.org/2024.findings-acl.850/)

**TLDR**: UPHILL benchmarks LLMs on health-related queries with presuppositions to evaluate factual robustness against misinformation.

## Abstract

AbstractAs corporations rush to integrate large language models (LLMs) it is critical that they provide factually accurate information, that is robust to any presuppositions that a user may express. In this work, we introduce UPHILL, a dataset consisting of health-related queries with varying degrees of presuppositions. Using UPHILL, we evaluate the factual accuracy and consistency of InstructGPT, ChatGPT, GPT-4 and Bing Copilot models. We find that while model responses rarely contradict true health claims (posed as questions), all investigated models fail to challenge false claims. Alarmingly, responses from these models agree with 23-32% of the existing false claims, and 49-55% with novel fabricated claims. As we increase the extent of presupposition in input queries, responses from all models except Bing Copilot agree with the claim considerably more often, regardless of its veracity. Given the moderate factual accuracy, and the inability of models to challenge false assumptions, our work calls for a careful assessment of current LLMs for use in high-stakes scenarios.