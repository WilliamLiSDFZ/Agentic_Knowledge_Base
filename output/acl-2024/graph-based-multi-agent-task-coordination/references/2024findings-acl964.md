---
title: "VillagerAgent: A Graph-Based Multi-Agent Framework for Coordinating Complex Task Dependencies in Minecraft"
source: "https://aclanthology.org/2024.findings-acl.964/"
pdf_url: ""
categories: ['graph-based-multi-agent-task-coordination']
tags: ['multi-agent', 'graph-coordination', 'minecraft']
venue: "ACL 2024"
tldr: "Proposes VillagerAgent, a graph-based multi-agent framework for coordinating complex spatial, causal, and temporal task dependencies in Minecraft."
---

# VillagerAgent: A Graph-Based Multi-Agent Framework for Coordinating Complex Task Dependencies in Minecraft

**Source**: [https://aclanthology.org/2024.findings-acl.964/](https://aclanthology.org/2024.findings-acl.964/)

**TLDR**: Proposes VillagerAgent, a graph-based multi-agent framework for coordinating complex spatial, causal, and temporal task dependencies in Minecraft.

## Abstract

AbstractIn this paper, we aim to evaluate multi-agent systems against complex dependencies, including spatial, causal, and temporal constraints. First, we construct a new benchmark, named VillagerBench, within the Minecraft environment. VillagerBench comprises diverse tasks crafted to test various aspects of multi-agent collaboration, from workload distribution to dynamic adaptation and synchronized task execution. Second, we introduce a Directed Acyclic Graph Multi-Agent Framework (VillagerAgent) to resolve complex inter-agent dependencies and enhance collaborative efficiency. This solution incorporates a task decomposer that creates a directed acyclic graph (DAG) for structured task management, an agent controller for task distribution, and a state manager for tracking environmental and agent data.Our empirical evaluation on VillagerBench demonstrates that VillagerAgentoutperforms the existing AgentVerse model, reducing hallucinations and improving task decomposition efficacy. The results underscore VillagerAgent’s potential in advancing multi-agent collaboration, offering a scalable and generalizable solution in dynamic environments. Source code is open-source on GitHub.