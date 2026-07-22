---
title: "Towards Objectively Benchmarking Social Intelligence of Language Agents at the Action Level"
source: "https://aclanthology.org/2024.findings-acl.526/"
pdf_url: ""
categories: ['social-ai-temporal-dynamics-evaluation', 'llm-agents-reasoning-and-planning']
tags: ['social-intelligence', 'agent-evaluation', 'action-level']
venue: "ACL 2024"
tldr: "A benchmark for objectively evaluating the social intelligence of language agents at the level of concrete actions."
---

# Towards Objectively Benchmarking Social Intelligence of Language Agents at the Action Level

**Source**: [https://aclanthology.org/2024.findings-acl.526/](https://aclanthology.org/2024.findings-acl.526/)

**TLDR**: A benchmark for objectively evaluating the social intelligence of language agents at the level of concrete actions.

## Abstract

AbstractProminent large language models have exhibited human-level performance in many domains, even enabling the derived agents to simulate human and social interactions. While practical works have substantiated the practicability of grounding language agents in sandbox simulation or embodied simulators, current social intelligence benchmarks either stay at the language level or use subjective metrics. In pursuit of a more realistic and objective evaluation, we introduce the Social Tasks in Sandbox Simulation (STSS) benchmark, which assesses language agents objectively at the action level by scrutinizing the goal achievements within the multi-agent simulation.Additionally, we sample conversation scenarios to build a language-level benchmark to provide an economically prudent preliminary evaluation and align with prevailing benchmarks. To gauge the significance of agent architecture, we implement a target-driven planning (TDP) module as an adjunct to the existing agent. Our evaluative findings highlight that the STSS benchmark is challenging for state-of-the-art language agents. Furthermore, it effectively discriminates between distinct language agents, suggesting its usefulness as a benchmark for evaluating both language models and agent architectures. Our code is available at https://github.com/wcx21/Social-Tasks-in-Sandbox-Simulation.