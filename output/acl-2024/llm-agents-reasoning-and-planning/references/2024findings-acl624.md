---
title: "InjecAgent: Benchmarking Indirect Prompt Injections in Tool-Integrated Large Language Model Agents"
source: "https://aclanthology.org/2024.findings-acl.624/"
categories: ['llm-security-robustness-and-detection', 'llm-agents-reasoning-and-planning']
tags: ['prompt-injection', 'LLM-agents', 'security']
venue: "ACL 2024"
tldr: "InjecAgent is a benchmark for evaluating indirect prompt injection attacks on tool-integrated LLM agents."
---

# InjecAgent: Benchmarking Indirect Prompt Injections in Tool-Integrated Large Language Model Agents

**Source**: [https://aclanthology.org/2024.findings-acl.624/](https://aclanthology.org/2024.findings-acl.624/)

**TLDR**: InjecAgent is a benchmark for evaluating indirect prompt injection attacks on tool-integrated LLM agents.

## Abstract

AbstractRecent work has embodied LLMs as agents, allowing them to access tools, perform actions, and interact with external content (e.g., emails or websites). However, external content introduces the risk of indirect prompt injection (IPI) attacks, where malicious instructions are embedded within the content processed by LLMs, aiming to manipulate these agents into executing detrimental actions against users. Given the potentially severe consequences of such attacks, establishing benchmarks to assess and mitigate these risks is imperative.In this work, we introduce InjecAgent, a benchmark designed to assess the vulnerability of tool-integrated LLM agents to IPI attacks. InjecAgent comprises 1,054 test cases covering 17 different user tools and 62 attacker tools. We categorize attack intentions into two primary types: direct harm to users and exfiltration of private data. We conduct a comprehensive evaluation of 30 different LLM agents and show that agents are vulnerable to IPI attacks, with ReAct-prompted GPT-4 vulnerable to attacks 24% of the time. Further investigation into an enhanced setting, where the attacker instructions are reinforced with a hacking prompt, shows additional increases in success rates. Our findings raise questions about the widespread deployment of LLM Agents.