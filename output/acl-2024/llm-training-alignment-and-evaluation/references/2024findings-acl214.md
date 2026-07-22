---
title: "DevEval: A Manually-Annotated Code Generation Benchmark Aligned with Real-World Code Repositories"
source: "https://aclanthology.org/2024.findings-acl.214/"
pdf_url: ""
categories: ['code-llm-generation-and-evaluation', 'llm-training-alignment-and-evaluation']
tags: ['code-generation', 'benchmark', 'LLM-evaluation', 'real-world', 'repository-level']
venue: "ACL 2024"
tldr: "Introduces DevEval, a manually annotated code generation benchmark aligned with real-world code repositories to better evaluate LLM coding abilities."
---

# DevEval: A Manually-Annotated Code Generation Benchmark Aligned with Real-World Code Repositories

**Source**: [https://aclanthology.org/2024.findings-acl.214/](https://aclanthology.org/2024.findings-acl.214/)

**TLDR**: Introduces DevEval, a manually annotated code generation benchmark aligned with real-world code repositories to better evaluate LLM coding abilities.

## Abstract

AbstractHow to evaluate the coding abilities of Large Language Models (LLMs) remains an open question. We find that existing benchmarks are poorly aligned with real-world code repositories and are insufficient to evaluate the coding abilities of LLMs.To address the knowledge gap, we propose a new benchmark named DevEval, which has three advances. (1) DevEval aligns with real-world repositories in multiple dimensions, e.g., code and dependency distributions. (2) DevEval is annotated by 13 developers and contains comprehensive annotations (e.g., requirements, original repositories, reference code, and reference dependencies). (3) DevEval comprises 1,825 testing samples from 115 repositories, covering 10 popular domains (e.g., Internet, Database). Based on DevEval, we propose repository-level code generation and evaluate 8 popular LLMs on DevEval (e.g., gpt-4, gpt-3.5, StarCoder 2, DeepSeek Coder, CodeLLaMa). Our experiments reveal these LLMs’ coding abilities in real-world code repositories. For example, the highest Pass@1 of gpt-4 only is 53.04% in our experiments. We also analyze LLMs’ failed cases and summarize their shortcomings. We hope DevEval can facilitate the development of LLMs in real code repositories. DevEval, prompts, and LLMs’ predictions have been released.