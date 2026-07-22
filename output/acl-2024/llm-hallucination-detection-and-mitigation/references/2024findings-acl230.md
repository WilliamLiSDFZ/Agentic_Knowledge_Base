---
title: "Just Ask One More Time! Self-Agreement Improves Reasoning of Language Models in (Almost) All Scenarios"
source: "https://aclanthology.org/2024.findings-acl.230/"
pdf_url: ""
categories: ['llm-agents-reasoning-and-planning', 'llm-hallucination-detection-and-mitigation']
tags: ['chain-of-thought', 'self-consistency', 'reasoning', 'ensemble']
venue: "ACL 2024"
tldr: "Proposes a self-agreement method that queries language models multiple times and aggregates answers to improve reasoning across diverse scenarios."
---

# Just Ask One More Time! Self-Agreement Improves Reasoning of Language Models in (Almost) All Scenarios

**Source**: [https://aclanthology.org/2024.findings-acl.230/](https://aclanthology.org/2024.findings-acl.230/)

**TLDR**: Proposes a self-agreement method that queries language models multiple times and aggregates answers to improve reasoning across diverse scenarios.

## Abstract

AbstractAlthough chain-of-thought (CoT) prompting combined with language models has achieved encouraging results on complex reasoning tasks, the naive greedy decoding used in CoT prompting usually causes the repetitiveness and local optimality. To address this shortcoming, ensemble-optimization tries to obtain multiple reasoning paths to get the final answer assembly. However, current ensemble-optimization methods either simply employ rule-based post-processing such as self-consistency, or train an additional model based on several task-related human annotations to select the best one among multiple reasoning paths, yet fail to generalize to realistic settings where the type of input questions is unknown or the answer format of reasoning paths is unknown. To avoid their limitations, we propose Self-Agreement, a generalizable ensemble-optimization method applying in almost all scenarios where the type of input questions and the answer format of reasoning paths may be known or unknown. Self-agreement firstly samples from language model’s decoder to generate a diverse set of reasoning paths, and subsequently prompts the language model one more time to determine the optimal answer by selecting the most agreed answer among the sampled reasoning paths. Self-agreement simultaneously achieves remarkable performance on six public reasoning benchmarks and superior generalization capabilities.