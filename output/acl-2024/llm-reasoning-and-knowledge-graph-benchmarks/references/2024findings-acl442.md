---
title: "ODA: Observation-Driven Agent for integrating LLMs and Knowledge Graphs"
source: "https://aclanthology.org/2024.findings-acl.442/"
categories: ['llm-reasoning-and-knowledge-graph-benchmarks', 'llm-agents-reasoning-and-planning']
tags: ['knowledge-graphs', 'LLM-agents', 'observation-driven', 'reasoning', 'NLP']
venue: "ACL 2024"
tldr: "ODA is an observation-driven agent framework that integrates LLMs with knowledge graphs for improved task-solving."
---

# ODA: Observation-Driven Agent for integrating LLMs and Knowledge Graphs

**Source**: [https://aclanthology.org/2024.findings-acl.442/](https://aclanthology.org/2024.findings-acl.442/)

**TLDR**: ODA is an observation-driven agent framework that integrates LLMs with knowledge graphs for improved task-solving.

## Abstract

AbstractThe integration of Large Language Models (LLMs) and knowledge graphs (KGs) has achieved remarkable success in various natural language processing tasks. However, existing methodologies that integrate LLMs and KGs often navigate the task-solving process solely based on the LLM’s analysis of the question, overlooking the rich cognitive potential inherent in the vast knowledge encapsulated in KGs. To address this, we introduce Observation-Driven Agent (ODA), a novel AI agent framework tailored for tasks involving KGs. ODA incorporates KG reasoning abilities via global observation, which enhances reasoning capabilities through a cyclical paradigm of observation, action, and reflection. Confronting the exponential explosion of knowledge during observation, we innovatively design a recursive observation mechanism. Subsequently, we integrate the observed knowledge into the action and reflection modules. Through extensive experiments, ODA demonstrates state-of-the-art performance on several datasets, notably achieving accuracy improvements of 12.87% and 8.9%.