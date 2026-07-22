---
title: "CR-LLM: A Dataset and Optimization for Concept Reasoning of Large Language Models"
source: "https://aclanthology.org/2024.findings-acl.815/"
categories: ['llm-reasoning-and-knowledge-graph-benchmarks', 'llm-training-alignment-and-evaluation']
tags: ['concept-reasoning', 'dataset', 'llm-evaluation']
venue: "ACL 2024"
tldr: "Introduces a dataset and optimization approach to improve concept reasoning capabilities in large language models."
---

# CR-LLM: A Dataset and Optimization for Concept Reasoning of Large Language Models

**Source**: [https://aclanthology.org/2024.findings-acl.815/](https://aclanthology.org/2024.findings-acl.815/)

**TLDR**: Introduces a dataset and optimization approach to improve concept reasoning capabilities in large language models.

## Abstract

AbstractConcept reasoning is an important capability for models to understand the world. However, the existing datasets, such as concept extraction and concept generation, suffer from modeledge leakage and context leakage. To address these limitations, we construct a dataset of concept reasoning for large language models (CR-LLM) with modeledge leakage prevention and context leakage prevention, which consists of 2,167 samples and covers different concept types. In addition, we propose a hybrid reasoning method, consisting of inductive reasoning, deductive reasoning and a controller. This method allows large language models to adaptively select the optimal reasoning method for each input sample. Finally, we conduct extensive experiments on CR-LLM using different models and methods. The results show that existing large language models and reasoning methods perform sub-optimally in the concept reasoning task. In contrast, our proposed method significantly improves the capabilities, achieving a 7% increase in accuracy compared to CoT and demonstrating better granularity. We release CR-LLM and code at https://github.com/Nianqi-Li/Concept-Reasoning-for-LLMs.