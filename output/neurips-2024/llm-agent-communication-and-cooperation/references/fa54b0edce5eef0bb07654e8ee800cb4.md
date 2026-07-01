---
title: "Reflective Multi-Agent Collaboration based on Large Language Models"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/fa54b0edce5eef0bb07654e8ee800cb4-Abstract-Conference.html"
categories: ['llm-agent-communication-and-cooperation', 'reinforcement-learning-optimization-and-decision-making']
tags: ['multi-agent-LLM', 'reflection', 'collaboration', 'autonomous-agents', 'planning']
venue: "NeurIPS 2024"
tldr: "Proposes a reflective multi-agent collaboration framework based on LLMs to improve performance on complex downstream tasks."
---

# Reflective Multi-Agent Collaboration based on Large Language Models

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/fa54b0edce5eef0bb07654e8ee800cb4-Abstract-Conference.html](https://papers.nips.cc/paper_files/paper/2024/hash/fa54b0edce5eef0bb07654e8ee800cb4-Abstract-Conference.html)

**TLDR**: Proposes a reflective multi-agent collaboration framework based on LLMs to improve performance on complex downstream tasks.

## Abstract

Benefiting from the powerful language expression and planning capabilities of Large Language Models (LLMs), LLM-based autonomous agents have achieved promising performance in various downstream tasks. Recently, based on the development of single-agent systems, researchers propose to construct LLM-based multi-agent systems to tackle more complicated tasks. In this paper, we propose a novel framework, named COPPER, to enhance the collaborative capabilities of LLM-based agents with the self-reflection mechanism. To improve the quality of reflections, we propose to fine-tune a shared reflector, which automatically tunes the prompts of actor models using our counterfactual PPO mechanism. On the one hand, we propose counterfactual rewards to assess the contribution of a single agent’s reflection within the system, alleviating the credit assignment problem. On the other hand, we propose to train a shared reflector, which enables the reflector to generate personalized reflections according to agent roles, while reducing the computational resource requirements and improving training stability. We conduct experiments on three datasets to evaluate the performance of our model in multi-hop question answering, mathematics, and chess scenarios. Experimental results show that COPPER possesses stronger reflection capabilities and exhibits excellent generalization performance across different actor models.