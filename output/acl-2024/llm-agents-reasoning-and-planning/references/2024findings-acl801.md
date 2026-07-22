---
title: "InstructGraph: Boosting Large Language Models via Graph-centric Instruction Tuning and Preference Alignment"
source: "https://aclanthology.org/2024.findings-acl.801/"
categories: ['llm-reasoning-and-knowledge-graph-benchmarks', 'llm-agents-reasoning-and-planning']
tags: ['knowledge-graphs', 'instruction-tuning', 'graph-reasoning', 'LLM', 'preference-alignment']
venue: "ACL 2024"
tldr: "InstructGraph enhances LLMs for graph reasoning and generation tasks via graph-centric instruction tuning and preference alignment."
---

# InstructGraph: Boosting Large Language Models via Graph-centric Instruction Tuning and Preference Alignment

**Source**: [https://aclanthology.org/2024.findings-acl.801/](https://aclanthology.org/2024.findings-acl.801/)

**TLDR**: InstructGraph enhances LLMs for graph reasoning and generation tasks via graph-centric instruction tuning and preference alignment.

## Abstract

AbstractDo current large language models (LLMs) better solve graph reasoning and generation tasks with parameter updates? In this paper, we propose InstructGraph, a framework that empowers LLMs with the abilities of graph reasoning and generation by instruction tuning and preference alignment. Specifically, we first propose a structured format verbalizer to unify all graph data into a universal code-like format, which can simply represent the graph without any external graph-specific encoders. Furthermore, a graph instruction tuning stage is introduced to guide LLMs in solving graph reasoning and generation tasks. Finally, we identify potential hallucination problems in graph tasks and sample negative instances for preference alignment, the target of which is to enhance the output’s reliability of the model. Extensive experiments across multiple graph-centric tasks exhibit that InstructGraph can achieve the best performance and outperform GPT-4 and LLaMA2 by more than 13% and 38%, respectively.