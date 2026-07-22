---
title: "Boosting LLM Agents with Recursive Contemplation for Effective Deception Handling"
source: "https://aclanthology.org/2024.findings-acl.591/"
pdf_url: ""
categories: ['llm-agents-reasoning-and-planning', 'llm-security-robustness-and-detection']
tags: ['LLM-agents', 'deception-handling', 'recursive-contemplation', 'adversarial-content', 'reasoning']
venue: "ACL 2024"
tldr: "Proposes a recursive contemplation framework to improve LLM agents' robustness against deceptive or misleading information."
---

# Boosting LLM Agents with Recursive Contemplation for Effective Deception Handling

**Source**: [https://aclanthology.org/2024.findings-acl.591/](https://aclanthology.org/2024.findings-acl.591/)

**TLDR**: Proposes a recursive contemplation framework to improve LLM agents' robustness against deceptive or misleading information.

## Abstract

AbstractRecent advances in large language models (LLMs) have led to significant success in using LLMs as agents. Nevertheless, a common assumption that LLMs always process honest information neglects the widespread deceptive or misleading content in human and AI-generated material. This oversight might expose LLMs to malicious manipulations. To enhance LLMs’ ability to identify and counteract deceptive information, in this paper, inspired by humans’ recursive thinking and perspective-taking, we introduce a novel cognitive framework, Recursive Contemplation (ReCon). ReCon combines formulation and refinement contemplation processes; formulation contemplation produces initial thoughts and speech, while refinement contemplation further polishes them. Additionally, we incorporate first-order and second-order perspective transitions into these processes respectively. Specifically, the first-order allows an LLM agent to infer others’ mental states, and the second-order involves understanding how others perceive the agent’s mental state. After integrating ReCon with various LLMs, extensive experiment results from the Avalon game and BigTom benchmark indicate ReCon’s efficacy in aiding LLMs to discern and maneuver around deceptive information without extra fine-tuning and data. Finally, we demonstrate ReCon’s scaling trend with model parameters, and explore the current limitations of LLMs in terms of safety and reasoning, potentially furnishing insights for subsequent research. Our project page can be found at https://shenzhi-wang.github.io/avalon_recon.