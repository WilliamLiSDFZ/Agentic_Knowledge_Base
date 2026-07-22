---
title: "PRewrite: Prompt Rewriting with Reinforcement Learning"
source: "https://aclanthology.org/2024.acl-short.54/"
categories: ['llm-training-alignment-and-evaluation', 'llm-agents-reasoning-and-planning']
tags: ['prompt-engineering', 'reinforcement-learning', 'prompt-optimization']
venue: "ACL 2024"
tldr: "PRewrite automates prompt rewriting using reinforcement learning to optimize LLM task performance beyond manual trial-and-error engineering."
---

# PRewrite: Prompt Rewriting with Reinforcement Learning

**Source**: [https://aclanthology.org/2024.acl-short.54/](https://aclanthology.org/2024.acl-short.54/)

**TLDR**: PRewrite automates prompt rewriting using reinforcement learning to optimize LLM task performance beyond manual trial-and-error engineering.

## Abstract

AbstractPrompt engineering is critical for the development of LLM-based applications. However, it is usually done manually in a “trial and error” fashion that can be time consuming, ineffective, and sub-optimal. Even for the prompts which seemingly work well, there is always a lingering question: can the prompts be made better with further modifications?To address these problems, we investigate automated prompt engineering in this paper. Specifically, we propose PRewrite, an automated method to rewrite an under-optimized prompt to a more effective prompt. We instantiate the prompt rewriter using an LLM. The rewriter LLM is trained using reinforcement learning to optimize the performance on a given downstream task. We conduct experiments on diverse benchmark datasets, which demonstrates the effectiveness of PRewrite.