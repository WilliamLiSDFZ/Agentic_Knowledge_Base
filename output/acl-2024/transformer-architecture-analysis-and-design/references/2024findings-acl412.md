---
title: "Identifying Semantic Induction Heads to Understand In-Context Learning"
source: "https://aclanthology.org/2024.findings-acl.412/"
categories: ['transformer-architecture-analysis-and-design']
tags: ['attention-heads', 'in-context-learning', 'interpretability']
venue: "ACL 2024"
tldr: "Identifies semantic induction heads in LLMs to better understand the mechanistic basis of in-context learning."
---

# Identifying Semantic Induction Heads to Understand In-Context Learning

**Source**: [https://aclanthology.org/2024.findings-acl.412/](https://aclanthology.org/2024.findings-acl.412/)

**TLDR**: Identifies semantic induction heads in LLMs to better understand the mechanistic basis of in-context learning.

## Abstract

AbstractAlthough large language models (LLMs) have demonstrated remarkable performance, the lack of transparency in their inference logic raises concerns about their trustworthiness. To gain a better understanding of LLMs, we conduct a detailed analysis of the operations of attention heads and aim to better understand the in-context learning of LLMs. Specifically, we investigate whether attention heads encode two types of relationships between tokens present in natural languages: the syntactic dependency parsed from sentences and the relation within knowledge graphs. We find that certain attention heads exhibit a pattern where, when attending to subject tokens, they recall object tokens and increase the output logits of those object tokens. More crucially, the formulation of such semantic induction heads has a close correlation with the emergence of the in-context learning ability of language models. The study of semantic attention heads advances our understanding of the intricate operations of attention heads in transformers, and further provides new insights into the in-context learning of LLMs.