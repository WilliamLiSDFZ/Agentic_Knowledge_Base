---
title: "What Makes a Good Order of Examples in In-Context Learning"
source: "https://aclanthology.org/2024.findings-acl.884/"
categories: ['llm-training-alignment-and-evaluation', 'nlp-benchmark-design-and-interpretability']
tags: ['in-context-learning', 'example-ordering', 'few-shot-learning']
venue: "ACL 2024"
tldr: "Studies what makes a good ordering of examples in in-context learning and proposes heuristics to identify effective orderings."
---

# What Makes a Good Order of Examples in In-Context Learning

**Source**: [https://aclanthology.org/2024.findings-acl.884/](https://aclanthology.org/2024.findings-acl.884/)

**TLDR**: Studies what makes a good ordering of examples in in-context learning and proposes heuristics to identify effective orderings.

## Abstract

AbstractAlthough large language models (LLMs) have demonstrated impressive few-shot learning capabilities via in-context learning (ICL), ICL performance is known to be highly sensitive to the order of examples provided. To identify appropriate orders, recent studies propose heuristic methods to evaluate order performance using a set of unlabeled data. However, the requirement of in-domain data limits their utility in real-world scenarios where additional annotated data is challenging to acquire. Additionally, these dataset-based approaches are prone to being sub-optimal for a lack of consideration for individual differences. To address the problems, we first analyze the properties of performant example orders at both corpus level and instance level. Based on the analysis we propose **DEmO** to adaptively identify performant example order for each instance without extra data. DEmO works by filtering out a subset of orders featuring label fairness, then selecting the most influential order for each test instance. The employment of a content-free metric makes DEmO independent of in-domain data. Extensive experiments indicate the superiority of DEmO over a wide range of strong baselines. Further analysis validates the generalizability across various settings.