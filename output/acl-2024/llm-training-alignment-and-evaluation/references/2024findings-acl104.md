---
title: "RankMean: Module-Level Importance Score for Merging Fine-tuned LLM Models"
source: "https://aclanthology.org/2024.findings-acl.104/"
categories: ['llm-training-alignment-and-evaluation', 'collaborative-llm-deployment-and-inference-optimization']
tags: ['model-merging', 'fine-tuned-LLMs', 'importance-scoring', 'multi-task', 'module-level']
venue: "ACL 2024"
tldr: "RankMean proposes a module-level importance scoring method for efficiently merging fine-tuned LLMs to handle multiple tasks without costly retraining."
---

# RankMean: Module-Level Importance Score for Merging Fine-tuned LLM Models

**Source**: [https://aclanthology.org/2024.findings-acl.104/](https://aclanthology.org/2024.findings-acl.104/)

**TLDR**: RankMean proposes a module-level importance scoring method for efficiently merging fine-tuned LLMs to handle multiple tasks without costly retraining.

## Abstract

AbstractTraditionally, developing new language models (LMs) capable of addressing multiple tasks involves fine-tuning pre-trained LMs using a wide collection of datasets, a process that often incurs significant computational expenses. Model merging emerges as a cost-effective alternative, allowing the integration of existing models fine-tuned on different tasks into a single model that performs well across all tasks, eliminating the need for additional training. In this paper, we propose RankMean, an algorithm for merging fine-tuned LMs without requiring any downstream data. RankMean determines merging coefficients based on the relative rankings of weight change magnitudes and applies these coefficients for module-wise integration of various fine-tuned models. Our experimental results demonstrate that RankMean outperforms existing baseline methods on multiple benchmarks. The code is available at https://github.com/VITA-Group/RankMean.