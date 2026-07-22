---
title: "RoleLLM: Benchmarking, Eliciting, and Enhancing Role-Playing Abilities of Large Language Models"
source: "https://aclanthology.org/2024.findings-acl.878/"
categories: ['llm-training-alignment-and-evaluation', 'llm-driven-interactive-narrative-and-games']
tags: ['role-playing', 'LLM-benchmark', 'character-imitation']
venue: "ACL 2024"
tldr: "RoleLLM provides a benchmark and pipeline for eliciting and evaluating role-playing capabilities in large language models."
---

# RoleLLM: Benchmarking, Eliciting, and Enhancing Role-Playing Abilities of Large Language Models

**Source**: [https://aclanthology.org/2024.findings-acl.878/](https://aclanthology.org/2024.findings-acl.878/)

**TLDR**: RoleLLM provides a benchmark and pipeline for eliciting and evaluating role-playing capabilities in large language models.

## Abstract

AbstractThe advent of Large Language Models (LLMs) has paved the way for complex tasks such as role-playing, which enhances user interactions by enabling models to imitate various characters. However, the closed-source nature of state-of-the-art LLMs and their general-purpose training limit role-playing optimization. In this paper, we introduce RoleLLM, a framework to benchmark, elicit, and enhance role-playing abilities in LLMs. RoleLLM comprises four stages: (1) Role Profile Construction for 100 roles; (2) Context-Based Instruction Generation (Context-Instruct) for role-specific knowledge extraction; (3) Role Prompting using GPT (RoleGPT) for speaking style imitation; and (4) Role-Conditioned Instruction Tuning (RoCIT) for fine-tuning open-source models along with role customization. By Context-Instruct and RoleGPT, we create RoleBench, the first systematic and fine-grained character-level benchmark dataset for role-playing with 168,093 samples. Moreover, RoCIT on RoleBench yields RoleLLaMA (English) and RoleGLM (Chinese), significantly enhancing role-playing abilities and even achieving comparable results with RoleGPT (using GPT-4).