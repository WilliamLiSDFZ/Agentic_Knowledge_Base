---
title: "Agent-FLAN: Designing Data and Methods of Effective Agent Tuning for Large Language Models"
source: "https://aclanthology.org/2024.findings-acl.557/"
pdf_url: ""
categories: ['llm-agents-reasoning-and-planning', 'llm-training-alignment-and-evaluation']
tags: ['agent-tuning', 'llm', 'instruction-following']
venue: "ACL 2024"
tldr: "Agent-FLAN identifies key data and method design principles to effectively tune open-source LLMs for agentic task performance."
---

# Agent-FLAN: Designing Data and Methods of Effective Agent Tuning for Large Language Models

**Source**: [https://aclanthology.org/2024.findings-acl.557/](https://aclanthology.org/2024.findings-acl.557/)

**TLDR**: Agent-FLAN identifies key data and method design principles to effectively tune open-source LLMs for agentic task performance.

## Abstract

AbstractOpen-sourced Large Language Models (LLMs) have achieved great success in various NLP tasks, however, they are still far inferior to API-based models when acting as agents. How to integrate agent ability into general LLMs becomes a crucial and urgent problem.This paper first delivers three key observations: (1) the current agent training corpus is entangled with both formats following and agent reasoning, which significantly shifts from the distribution of its pre-training data; (2) LLMs exhibit different learning speeds on the capabilities required by agent tasks; and (3) current approaches have side-effects when improving agent abilities by introducing hallucinations. Based on the above findings, we propose Agent-FLAN to effectively Fine-tune LANguage models for Agents.Through careful decomposition and redesign of the training corpus, Agent-FLAN enables Llama2-7B to outperform prior best works by 3.5% across various agent evaluation datasets. With comprehensively constructed negative samples, Agent-FLAN greatly alleviates the hallucination issues based on our established evaluation benchmark. Besides, it consistently improves the agent capability of LLMs when scaling model sizes while slightly enhancing the general capability of LLMs. The code and models are available at https://github.com/InternLM/Agent-FLAN.