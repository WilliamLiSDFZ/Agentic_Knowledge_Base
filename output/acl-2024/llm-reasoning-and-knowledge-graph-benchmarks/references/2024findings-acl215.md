---
title: "LPNL: Scalable Link Prediction with Large Language Models"
source: "https://aclanthology.org/2024.findings-acl.215/"
categories: ['llm-reasoning-and-knowledge-graph-benchmarks']
tags: ['link-prediction', 'graph-learning', 'large-language-models']
venue: "ACL 2024"
tldr: "Introduces LPNL, a scalable framework leveraging LLMs for link prediction on large graphs."
---

# LPNL: Scalable Link Prediction with Large Language Models

**Source**: [https://aclanthology.org/2024.findings-acl.215/](https://aclanthology.org/2024.findings-acl.215/)

**TLDR**: Introduces LPNL, a scalable framework leveraging LLMs for link prediction on large graphs.

## Abstract

AbstractExploring the application of large language models (LLMs) to graph learning is an emerging endeavor. However, the vast amount of information inherent in large graphs poses significant challenges to graph learning with LLMs. This work focuses on the link prediction task and introduces **LPNL** (Link Prediction via Natural Language), a framework based on large language models designed for scalable link prediction on large-scale heterogeneous graphs. We design novel prompts for link prediction that articulate graph details in natural language. We propose a two-stage sampling pipeline to extract crucial information from the graphs, and a divide-and-conquer strategy to control the input tokens within predefined limits, addressing the challenge of overwhelming information. We fine-tune a T5 model based on our self-supervised learning designed for link prediction. Extensive experimental results demonstrate that LPNL outperforms multiple advanced baselines in link prediction tasks on large-scale graphs.