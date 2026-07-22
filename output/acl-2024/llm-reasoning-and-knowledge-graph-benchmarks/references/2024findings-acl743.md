---
title: "Propagation and Pitfalls: Reasoning-based Assessment of Knowledge Editing through Counterfactual Tasks"
source: "https://aclanthology.org/2024.findings-acl.743/"
pdf_url: ""
categories: ['llm-reasoning-and-knowledge-graph-benchmarks']
tags: ['knowledge-editing', 'counterfactual-reasoning', 'knowledge-propagation']
venue: "ACL 2024"
tldr: "This work analyzes barriers to knowledge propagation in LLM editing approaches using a novel counterfactual reasoning benchmark."
---

# Propagation and Pitfalls: Reasoning-based Assessment of Knowledge Editing through Counterfactual Tasks

**Source**: [https://aclanthology.org/2024.findings-acl.743/](https://aclanthology.org/2024.findings-acl.743/)

**TLDR**: This work analyzes barriers to knowledge propagation in LLM editing approaches using a novel counterfactual reasoning benchmark.

## Abstract

AbstractCurrent knowledge editing approaches struggle to effectively propagate updates to interconnected facts.In this work, we delve into the barriers that hinder the appropriate propagation of updated knowledge within these models for accurate reasoning. To support our analysis, we introduce a novel reasoning-based benchmark, ReCoE (Reasoning-based Counterfactual Editing dataset), which covers six common reasoning schemes in the real world. We conduct an extensive analysis of existing knowledge editing techniques, including input-augmentation, finetuning, and locate-and-edit methods. We found that all model editing methods exhibit notably low performance on this dataset, especially within certain reasoning schemes. Our analysis of the chain-of-thought responses from edited models indicate that, while the models effectively update individual facts, they struggle to recall these facts in reasoning tasks. Moreover, locate-and-edit methods severely deteriorate the models’ language modeling capabilities, leading to poor perplexity and logical coherence in their outputs.