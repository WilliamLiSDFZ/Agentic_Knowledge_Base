---
title: "Towards Uncertainty-Aware Language Agent"
source: "https://aclanthology.org/2024.findings-acl.398/"
pdf_url: ""
categories: ['llm-agents-reasoning-and-planning']
tags: ['language-agents', 'uncertainty', 'planning']
venue: "ACL 2024"
tldr: "Presents an uncertainty-aware language agent framework that incorporates uncertainty estimation into dynamic LLM-based interactions with the world."
---

# Towards Uncertainty-Aware Language Agent

**Source**: [https://aclanthology.org/2024.findings-acl.398/](https://aclanthology.org/2024.findings-acl.398/)

**TLDR**: Presents an uncertainty-aware language agent framework that incorporates uncertainty estimation into dynamic LLM-based interactions with the world.

## Abstract

AbstractWhile Language Agents have achieved promising success by placing Large Language Models at the core of a more versatile design that dynamically interacts with the external world, the existing approaches neglect the notion of uncertainty during these interactions. We present the Uncertainty-Aware Language Agent (UALA), a framework that orchestrates the interaction between the agent and the external world using uncertainty quantification. Compared with other well-known counterparts like ReAct, our extensive experiments across 3 representative tasks (HotpotQA, StrategyQA, MMLU) and various LLM sizes demonstrate that UALA brings a significant improvement of performance, while having a substantially lower reliance on the external world (i.e., reduced number of tool calls and tokens). Our analyses provide various insights including the great potential of UALA compared with agent fine-tuning, and underscore the unreliability of verbalised confidence of LLMs as a proxy for uncertainty.