---
title: "Latent Learningscape Guided In-context Learning"
source: "https://aclanthology.org/2024.findings-acl.482/"
categories: ['llm-reasoning-and-knowledge-graph-benchmarks', 'llm-agents-reasoning-and-planning']
tags: ['in-context-learning', 'example-selection', 'latent-space']
venue: "ACL 2024"
tldr: "Proposes latent learningscape guidance for better demonstration selection in in-context learning for LLMs."
---

# Latent Learningscape Guided In-context Learning

**Source**: [https://aclanthology.org/2024.findings-acl.482/](https://aclanthology.org/2024.findings-acl.482/)

**TLDR**: Proposes latent learningscape guidance for better demonstration selection in in-context learning for LLMs.

## Abstract

AbstractThe growing interest in leveraging large language models is driven by their exceptional imitation and reasoning capabilities. In-context learning (ICL), a streamlined method, has shown potential in boosting these models’ performance without modifying their underlying parameters, especially when supplied with suitable demonstrations. However, existing methods mainly choose demonstrations by comparing surface-level semantic similarities (e.g., based on embedding) and fall short of identifying the most fitting ones. This paper introduces the concept of a “latent learningscape”, a more nuanced representation that describes the characteristic of the demonstrations. Building on this concept, we develop a results-driven approach to characterize the latent learningscape features of demonstrations, which then inform the creation of more effective prompts. Through comprehensive testing across datasets in arithmetic, commonsense, and symbolic reasoning tasks, our approach outperforms leading models, showing an average increase in scores by 7.4 percentage points.