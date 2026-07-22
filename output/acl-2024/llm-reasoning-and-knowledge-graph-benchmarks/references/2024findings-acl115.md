---
title: "A Graph per Persona: Reasoning about Subjective Natural Language Descriptions"
source: "https://aclanthology.org/2024.findings-acl.115/"
categories: ['llm-reasoning-and-knowledge-graph-benchmarks']
tags: ['subjective-reasoning', 'knowledge-graph', 'persona', 'opinions-preferences']
venue: "ACL 2024"
tldr: "Proposes a per-persona graph-based framework for reasoning about subjective natural language descriptions such as opinions and preferences."
---

# A Graph per Persona: Reasoning about Subjective Natural Language Descriptions

**Source**: [https://aclanthology.org/2024.findings-acl.115/](https://aclanthology.org/2024.findings-acl.115/)

**TLDR**: Proposes a per-persona graph-based framework for reasoning about subjective natural language descriptions such as opinions and preferences.

## Abstract

AbstractReasoning about subjective natural language descriptions, such as opinions and preferences, is a challenging topic that largely remains unsolved to date. In particular, state-of-the-art large language models (LLMs) perform disappointingly in this task, show strong biases, and do not meet the interpretability requirements often needed in these kinds of applications. We propose a novel approach for reasoning about subjective knowledge that integrates potential and implicit meanings and explicitly models the relational nature of the information. We apply supervised graph learning, offer explanations for the model’s reasoning, and show that our model performs well across all 15 topics of OpinionQA, outperforming several prominent LLMs. Our detailed analysis further shows its unique advantages and the complementary nature it offers in comparison to LLMs.