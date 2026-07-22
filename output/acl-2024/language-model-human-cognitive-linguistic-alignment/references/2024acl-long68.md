---
title: "ANALOGYKB: Unlocking Analogical Reasoning of Language Models with A Million-scale Knowledge Base"
source: "https://aclanthology.org/2024.acl-long.68/"
pdf_url: ""
categories: ['llm-reasoning-and-knowledge-graph-benchmarks', 'language-model-human-cognitive-linguistic-alignment']
tags: ['analogical-reasoning', 'knowledge-base', 'language-models', 'benchmark']
venue: "ACL 2024"
tldr: "Introduces ANALOGYKB, a million-scale knowledge base to improve analogical reasoning in language models."
---

# ANALOGYKB: Unlocking Analogical Reasoning of Language Models with A Million-scale Knowledge Base

**Source**: [https://aclanthology.org/2024.acl-long.68/](https://aclanthology.org/2024.acl-long.68/)

**TLDR**: Introduces ANALOGYKB, a million-scale knowledge base to improve analogical reasoning in language models.

## Abstract

AbstractAnalogical reasoning is a fundamental cognitive ability of humans. However, current language models (LMs) still struggle to achieve human-like performance in analogical reasoning tasks due to a lack of resources for model training. In this work, we address this gap by proposing ANALOGYKB, a million-scale analogy knowledge base (KB) derived from existing knowledge graphs (KGs). ANALOGYKB identifies two types of analogies from the KGs: 1) analogies of the same relations, which can be directly extracted from the KGs, and 2) analogies of analogous relations, which are identified with a selection and filtering pipeline enabled by large language models (LLMs), followed by minor human efforts for data quality control. Evaluations on a series of datasets of two analogical reasoning tasks (analogy recognition and generation) demonstrate that ANALOGYKB successfully enables both smaller LMs and LLMs to gain better analogical reasoning capabilities. Resources of this paper can be found at https://github.com/siyuyuan/analogykb.