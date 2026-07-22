---
title: "AgentTuning: Enabling Generalized Agent Abilities for LLMs"
source: "https://aclanthology.org/2024.findings-acl.181/"
categories: ['llm-agents-reasoning-and-planning', 'llm-training-alignment-and-evaluation']
tags: ['LLM-agents', 'instruction-tuning', 'generalization']
venue: "ACL 2024"
tldr: "AgentTuning improves open LLMs' agent capabilities via generalized instruction tuning on diverse agent tasks."
---

# AgentTuning: Enabling Generalized Agent Abilities for LLMs

**Source**: [https://aclanthology.org/2024.findings-acl.181/](https://aclanthology.org/2024.findings-acl.181/)

**TLDR**: AgentTuning improves open LLMs' agent capabilities via generalized instruction tuning on diverse agent tasks.

## Abstract

AbstractOpen large language models (LLMs) with great performance in various tasks have significantly advanced the development of LLMs. However, they are far inferior to commercial models such as ChatGPT and GPT-4 when acting as agents to tackle complex tasks in the real world. These agent tasks employ LLMs as the central controller responsible for planning, memorization, and tool utilization, necessitating both fine-grained prompting methods and robust LLMs to achieve satisfactory performance. Though many prompting methods have been proposed to complete particular agent tasks, there is lack of research focusing on improving the agent capabilities of LLMs themselves without compromising their general abilities. In this work, we present AgentTuning, a simple and general method to enhance the agent abilities of LLMs while maintaining their general LLM capabilities. We construct AgentInstruct, a lightweight instruction-tuning dataset containing high-quality interaction trajectories. We employ a hybrid instruction-tuning strategy by combining AgentInstruct with open-source instructions from general domains. AgentTuning is used to instruction-tune the Llama 2 series, resulting in AgentLM. Our evaluations show that AgentTuning enables LLMs’ agent capabilities without compromising general abilities. The AgentLM-70B is comparable to GPT-3.5-turbo on unseen agent tasks, demonstrating generalized agent capabilities. We open source the AgentInstruct and AgentLM-7B, 13B, and 70B models at https://anonymous.4open.science/r/AgentTuning, serving open and powerful alternatives to commercial LLMs for agent tasks.