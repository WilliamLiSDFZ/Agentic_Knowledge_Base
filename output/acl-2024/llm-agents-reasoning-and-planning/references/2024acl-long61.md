---
title: "Tell Me More! Towards Implicit User Intention Understanding of Language Model Driven Agents"
source: "https://aclanthology.org/2024.acl-long.61/"
pdf_url: ""
categories: ['llm-agents-reasoning-and-planning', 'efficient-communication-principles-in-language']
tags: ['LLM-agents', 'user-intent', 'clarification', 'implicit-understanding']
venue: "ACL 2024"
tldr: "Proposes a framework for language model-driven agents to better understand implicit user intentions by seeking clarification when instructions are vague."
---

# Tell Me More! Towards Implicit User Intention Understanding of Language Model Driven Agents

**Source**: [https://aclanthology.org/2024.acl-long.61/](https://aclanthology.org/2024.acl-long.61/)

**TLDR**: Proposes a framework for language model-driven agents to better understand implicit user intentions by seeking clarification when instructions are vague.

## Abstract

AbstractCurrent language model-driven agents often lack mechanisms for effective user participation, which is crucial given the vagueness commonly found in user instructions. Although adept at devising strategies and performing tasks, these agents struggle with seeking clarification and grasping precise user intentions. To bridge this gap, we introduce Intention-in-Interaction (IN3), a novel benchmark designed to inspect users’ implicit intentions through explicit queries. Next, we propose the incorporation of model experts as the upstream in agent designs to enhance user-agent interaction. Employing IN3, we empirically train Mistral-Interact, a powerful model that proactively assesses task vagueness, inquires about user intentions, and refines them into actionable goals before starting downstream agent task execution. Integrating it into the XAgent framework, we comprehensively evaluate the enhanced agent system regarding user instruction understanding and execution, revealing that our approach notably excels at identifying vague user tasks, recovering and summarizing critical missing information, setting precise and necessary agent execution goals, and minimizing redundant tool usage, thus boosting overall efficiency.