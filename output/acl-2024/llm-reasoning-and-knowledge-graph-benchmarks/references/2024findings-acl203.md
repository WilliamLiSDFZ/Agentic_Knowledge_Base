---
title: "DARA: Decomposition-Alignment-Reasoning Autonomous Language Agent for Question Answering over Knowledge Graphs"
source: "https://aclanthology.org/2024.findings-acl.203/"
categories: ['llm-reasoning-and-knowledge-graph-benchmarks', 'llm-agents-reasoning-and-planning']
tags: ['knowledge-graph-qa', 'decomposition-alignment', 'language-agents']
venue: "ACL 2024"
tldr: "DARA is a decomposition-alignment-reasoning agent that improves LLM-based question answering over knowledge graphs via neural-symbolic reasoning."
---

# DARA: Decomposition-Alignment-Reasoning Autonomous Language Agent for Question Answering over Knowledge Graphs

**Source**: [https://aclanthology.org/2024.findings-acl.203/](https://aclanthology.org/2024.findings-acl.203/)

**TLDR**: DARA is a decomposition-alignment-reasoning agent that improves LLM-based question answering over knowledge graphs via neural-symbolic reasoning.

## Abstract

AbstractAnswering Questions over Knowledge Graphs (KGQA) is key to well-functioning autonomous language agents in various real-life applications. To improve the neural-symbolic reasoning capabilities of language agents powered by Large Language Models (LLMs) in KGQA, we propose the Decomposition-Alignment-Reasoning Agent (DARA) framework. DARA effectively parses questions into formal queries through a dual mechanism: high-level iterative task decomposition and low-level task grounding. Importantly, DARA can be efficiently trained with a small number of high-quality reasoning trajectories. Our experimental results demonstrate that DARA fine-tuned on LLMs (e.g. Llama-2-7B, Mistral) outperforms both in-context learning-based agents with GPT-4 and alternative fine-tuned agents, across different benchmarks, making such models more accessible for real-life applications. We also show that DARA attains performance comparable to state-of-the-art enumerating-and-ranking-based methods for KGQA.