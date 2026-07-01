---
title: "AdaSociety: An Adaptive Environment with Social Structures for Multi-Agent Decision-Making"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/3e4d8407cb468850f2f8f4a949e64bf0-Abstract-Datasets_and_Benchmarks_Track.html"
categories: ['reinforcement-learning-optimization-and-decision-making', 'llm-agent-communication-and-cooperation']
tags: ['multi-agent-systems', 'adaptive-environments', 'social-structures']
venue: "NeurIPS 2024"
tldr: "Introduces AdaSociety, an adaptive multi-agent environment with social structures that dynamically generates tasks to enhance agent intelligence."
---

# AdaSociety: An Adaptive Environment with Social Structures for Multi-Agent Decision-Making

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/3e4d8407cb468850f2f8f4a949e64bf0-Abstract-Datasets_and_Benchmarks_Track.html](https://papers.nips.cc/paper_files/paper/2024/hash/3e4d8407cb468850f2f8f4a949e64bf0-Abstract-Datasets_and_Benchmarks_Track.html)

**TLDR**: Introduces AdaSociety, an adaptive multi-agent environment with social structures that dynamically generates tasks to enhance agent intelligence.

## Abstract

Traditional interactive environments limit agents' intelligence growth with fixed tasks. Recently, single-agent environments address this by generating new tasks based on agent actions, enhancing task diversity. We consider the decision-making problem in multi-agent settings, where tasks are further influenced by social connections, affecting rewards and information access. However, existing multi-agent environments lack a combination of adaptive physical surroundings and social connections, hindering the learning of intelligent behaviors.To address this, we introduce AdaSociety, a customizable multi-agent environment featuring expanding state and action spaces, alongside explicit and alterable social structures.  As agents progress, the environment adaptively generates new tasks with social structures for agents to undertake. In AdaSociety, we develop three mini-games showcasing distinct social structures and tasks. Initial results demonstrate that specific social structures can promote both individual and collective benefits, though current reinforcement learning and LLM-based algorithms show limited effectiveness in leveraging social structures to enhance performance. Overall, AdaSociety serves as a valuable research platform for exploring intelligence in diverse physical and social settings. The code is available at https://github.com/bigai-ai/AdaSociety.