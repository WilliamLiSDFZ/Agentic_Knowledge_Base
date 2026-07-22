---
title: "RaDA: Retrieval-augmented Web Agent Planning with LLMs"
source: "https://aclanthology.org/2024.findings-acl.802/"
pdf_url: ""
categories: ['llm-agents-reasoning-and-planning', 'collaborative-llm-deployment-and-inference-optimization']
tags: ['web-agents', 'retrieval-augmented-planning', 'llm-agents']
venue: "ACL 2024"
tldr: "RaDA is a retrieval-augmented planning method for LLM-based web agents that addresses context length limits and reduces dependency on human-engineered exemplars."
---

# RaDA: Retrieval-augmented Web Agent Planning with LLMs

**Source**: [https://aclanthology.org/2024.findings-acl.802/](https://aclanthology.org/2024.findings-acl.802/)

**TLDR**: RaDA is a retrieval-augmented planning method for LLM-based web agents that addresses context length limits and reduces dependency on human-engineered exemplars.

## Abstract

AbstractAgents powered by large language models (LLMs) inherit important limitations, such as the restricted context length, dependency on human-engineered exemplars (e.g., for task decomposition), and insufficient generalization. To address these challenges, we propose RaDA, a novel planning method for Web agents that does not require manual exemplars, efficiently leverages the LLMs’ context, and enhances generalization. RaDA disentangles planning into two stages: for a new given task, during Retrieval-augmented Task Decomposition (RaD), it decomposes tasks into high-level subtasks; next, during Retrieval-augmented Action Generation (RaA), it traverses the trajectory obtained with RaD to iteratively synthesize actions based on dynamically retrieved exemplars. We compare RaDA with strong baselines covering a broad space of design choices, using both GPT-3.5 and GPT-4 as backbones; and we find consistent improvements over previous SOTA in two challenging benchmarks, CompWoB and Mind2Web, covering settings with different complexities. We show the contributions of RaDA via ablation studies and qualitative analysis; and we discuss the structural benefits of our more compositional design.