---
title: "Cache & Distil: Optimising API Calls to Large Language Models"
source: "https://aclanthology.org/2024.findings-acl.704/"
categories: ['collaborative-llm-deployment-and-inference-optimization', 'llm-training-alignment-and-evaluation']
tags: ['API-optimization', 'knowledge-distillation', 'caching']
venue: "ACL 2024"
tldr: "Proposes Cache & Distil, combining caching and distillation to reduce costly LLM API calls by routing queries to a smaller local model when possible."
---

# Cache & Distil: Optimising API Calls to Large Language Models

**Source**: [https://aclanthology.org/2024.findings-acl.704/](https://aclanthology.org/2024.findings-acl.704/)

**TLDR**: Proposes Cache & Distil, combining caching and distillation to reduce costly LLM API calls by routing queries to a smaller local model when possible.

## Abstract

AbstractLarge-scale deployment of generative AI tools often depends on costly API calls to a Large Language Model (LLM) to fulfil user queries, a process that also exposes the request stream to external providers. To curtail the frequency of these calls, one can employ a local smaller language model -a student- which is continuously trained on the responses of the LLM. This student gradually gains proficiency in independently handling an increasing number of user requests, a process we term neural caching. The crucial element in neural caching is a policy that decides which requests should be processed by the student alone and which should be redirected to the LLM, subsequently aiding the student’s learning. In this study, we focus on classification tasks, and we consider a range of classic Active Learning-based selection criteria as the policy. Our experiments suggest that Margin Sampling and Query by Committee bring consistent benefits over other policies and baselines across tasks and budgets.