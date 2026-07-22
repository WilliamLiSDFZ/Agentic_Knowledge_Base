---
title: "Forward-Backward Reasoning in Large Language Models for Mathematical Verification"
source: "https://aclanthology.org/2024.findings-acl.397/"
categories: ['llm-agents-reasoning-and-planning', 'llm-reasoning-and-knowledge-graph-benchmarks']
tags: ['mathematical-reasoning', 'LLM', 'forward-backward-reasoning', 'self-consistency', 'verification']
venue: "ACL 2024"
tldr: "Introduces backward reasoning to complement forward self-consistency sampling, improving LLM mathematical verification performance."
---

# Forward-Backward Reasoning in Large Language Models for Mathematical Verification

**Source**: [https://aclanthology.org/2024.findings-acl.397/](https://aclanthology.org/2024.findings-acl.397/)

**TLDR**: Introduces backward reasoning to complement forward self-consistency sampling, improving LLM mathematical verification performance.

## Abstract

AbstractSelf-Consistency samples diverse reasoning chains with answers and chooses the final answer by majority voting. It is based on forward reasoning and cannot further improve performance by sampling more reasoning chains when saturated. To further boost performance, we introduce backward reasoning to verify candidate answers. Specifically, for mathematical tasks, we mask a number in the question and ask the LLM to answer a backward question created by a simple template, i.e., to predict the masked number when a candidate answer is provided. Instead of using forward or backward reasoning alone, we propose **FOBAR** to combine **FO**rward and **BA**ckward **R**easoning for verification. Extensive experiments on six standard mathematical data sets and three LLMs show that FOBAR achieves state-of-the-art performance. In particular, FOBAR outperforms Self-Consistency, which uses forward reasoning alone, demonstrating that combining forward and backward reasoning is more accurate in verification. In addition, FOBAR achieves higher accuracy than existing verification methods, showing the effectiveness of the simple template used in backward reasoning and the proposed combination.