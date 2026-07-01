---
title: "RoleAgent: Building, Interacting, and Benchmarking High-quality Role-Playing Agents from Scripts"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/5875aca1ef70285a35940afbbce0f9fb-Abstract-Datasets_and_Benchmarks_Track.html"
categories: ['llm-agent-communication-and-cooperation', 'ai-benchmarking-and-evaluation-methodology']
tags: ['role-playing-agents', 'llm-simulation', 'benchmarking']
venue: "NeurIPS 2024"
tldr: "Introduces RoleAgent, a framework for building, interacting with, and benchmarking high-quality role-playing agents from scripts using LLMs."
---

# RoleAgent: Building, Interacting, and Benchmarking High-quality Role-Playing Agents from Scripts

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/5875aca1ef70285a35940afbbce0f9fb-Abstract-Datasets_and_Benchmarks_Track.html](https://papers.nips.cc/paper_files/paper/2024/hash/5875aca1ef70285a35940afbbce0f9fb-Abstract-Datasets_and_Benchmarks_Track.html)

**TLDR**: Introduces RoleAgent, a framework for building, interacting with, and benchmarking high-quality role-playing agents from scripts using LLMs.

## Abstract

Believable agents can empower interactive applications ranging from immersive environments to rehearsal spaces for interpersonal communication. Recently, generative agents have been proposed to simulate believable human behavior by using Large Language Models. However, the existing method heavily relies on human-annotated agent profiles (e.g., name, age, personality, relationships with others, and so on) for the initialization of each agent, which cannot be scaled up easily. In this paper, we propose a scalable RoleAgent framework to generate high-quality role-playing agents from raw scripts, which includes building and interacting stages. Specifically, in the building stage, we use a hierarchical memory system to extract and summarize the structure and high-level information of each agent for the raw script. In the interacting stage, we propose a novel innovative mechanism with four steps to achieve a high-quality interaction between agents. Finally, we introduce a systematic and comprehensive evaluation benchmark called RoleAgentBench to evaluate the effectiveness of our RoleAgent, which includes 100 and 28 roles for 20 English and 5 Chinese scripts, respectively. Extensive experimental results on RoleAgentBench demonstrate the effectiveness of RoleAgent.