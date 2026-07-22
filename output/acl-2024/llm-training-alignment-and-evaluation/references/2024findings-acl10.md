---
title: "A Grounded Preference Model for LLM Alignment"
source: "https://aclanthology.org/2024.findings-acl.10/"
categories: ['llm-training-alignment-and-evaluation']
tags: ['alignment', 'hallucination', 'retrieval-augmented', 'preference-model']
venue: "ACL 2024"
tldr: "A grounded preference model is proposed to align LLMs to factual retrieval-augmented content and reduce hallucination."
---

# A Grounded Preference Model for LLM Alignment

**Source**: [https://aclanthology.org/2024.findings-acl.10/](https://aclanthology.org/2024.findings-acl.10/)

**TLDR**: A grounded preference model is proposed to align LLMs to factual retrieval-augmented content and reduce hallucination.

## Abstract

AbstractDespite LLMs’ recent advancements, they still suffer from factual inconsistency and hallucination. An often-opted remedy is retrieval-augmented generation – however, there is no guarantee that the model will strictly adhere to retrieved grounding. Fundamentally, LLMs need to be aligned to be more faithful to grounding, which will require high-quality preference annotations. This paper investigates whether we can create high-quality grounded preference data for model alignment without using annotations from humans or large proprietary models. We experimented with existing entailment data and proposed approaches to generate synthetic grounded preference data, with which we train a Grounded Preference Model(GPM). We demonstrate through Proximal Policy Optimization(PPO) training of Mistral-7B-Instruct that our GPM model can successfully align powerful LLMs to generate much better grounded responses as judged by GPT4. Moreover, we show that our GPM is also a great faithfulness classifier, achieving SoTA in dialogue sub-tasks of the TRUE faithfulness Benchmark. We will release our GPM under the Apache 2.0 license.