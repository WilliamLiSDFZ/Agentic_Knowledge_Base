---
title: "Call Me When Necessary: LLMs can Efficiently and Faithfully Reason over Structured Environments"
source: "https://aclanthology.org/2024.findings-acl.254/"
categories: ['llm-agents-reasoning-and-planning', 'llm-reasoning-and-knowledge-graph-benchmarks']
tags: ['knowledge-graphs', 'structured-reasoning', 'LLM-efficiency']
venue: "ACL 2024"
tldr: "An LLM reasoning framework efficiently handles multi-hop structured environment queries by selectively invoking external calls."
---

# Call Me When Necessary: LLMs can Efficiently and Faithfully Reason over Structured Environments

**Source**: [https://aclanthology.org/2024.findings-acl.254/](https://aclanthology.org/2024.findings-acl.254/)

**TLDR**: An LLM reasoning framework efficiently handles multi-hop structured environment queries by selectively invoking external calls.

## Abstract

AbstractLarge Language Models (LLMs) have shown potential in reasoning over structured environments, e.g., knowledge graphs and tables. Such tasks typically require multi-hop reasoning, i.e., match natural language utterance with instances in the environment. Previous works adopt LLMs to incrementally build a reasoning path, where LLMs either invoke tools or pick up items by step-by-step interacting with the environment. We propose Reasoning-Path-Editing (Readi), a novel framework where LLMs can efficiently and faithfully reason over structured environments. In Readi, LLMs initially generate a reasoning path given a query, and edit the path only when necessary. We instantiate the path on structured environments and provide feedback to edit the path if anything goes wrong. Experimental results on three KGQA and two TableQA datasets show the effectiveness of Readi, significantly surpassing previous LLM-based methods (by 9.1% Hit@1 on WebQSP, 12.4% on MQA-3H and 9.5% on WTQ), comparable with state-of-the-art fine-tuned methods (67% on CWQ and 74.7% on WebQSP) and substantially boosting the vanilla LLMs (by 14.9% on CWQ). Our code will be available on https://aka.ms/readi.