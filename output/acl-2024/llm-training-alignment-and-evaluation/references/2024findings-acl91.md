---
title: "CriticBench: Benchmarking LLMs for Critique-Correct Reasoning"
source: "https://aclanthology.org/2024.findings-acl.91/"
categories: ['llm-training-alignment-and-evaluation']
tags: ['LLM-evaluation', 'critique-correction', 'reasoning-benchmark']
venue: "ACL 2024"
tldr: "Introduces CriticBench to benchmark LLMs' ability to critique and correct their own reasoning."
---

# CriticBench: Benchmarking LLMs for Critique-Correct Reasoning

**Source**: [https://aclanthology.org/2024.findings-acl.91/](https://aclanthology.org/2024.findings-acl.91/)

**TLDR**: Introduces CriticBench to benchmark LLMs' ability to critique and correct their own reasoning.

## Abstract

AbstractThe ability of Large Language Models (LLMs) to critique and refine their reasoning is crucial for their application in evaluation, feedback provision, and self-improvement. This paper introduces CriticBench, a comprehensive benchmark designed to assess LLMs’ abilities to critique and rectify their reasoning across a variety of tasks. CriticBench encompasses five reasoning domains: mathematical, commonsense, symbolic, coding, and algorithmic. It compiles 15 datasets and incorporates responses from three LLM families. Utilizing CriticBench, we evaluate and dissect the performance of 17 LLMs in generation, critique, and correction reasoning, i.e., GQC reasoning. Our findings reveal: (1) a linear relationship in GQC capabilities, with critique-focused training markedly enhancing performance; (2) a task-dependent variation in correction effectiveness, with logic-oriented tasks being more amenable to correction; (3) GQC knowledge inconsistencies that decrease as model size increases; and (4) an intriguing inter-model critiquing dynamic, where stronger models are better at critiquing weaker ones, while weaker models can surprisingly surpass stronger ones in their self-critique. We hope these insights into the nuanced critique-correct reasoning of LLMs will foster further research in LLM critique and self-improvement.