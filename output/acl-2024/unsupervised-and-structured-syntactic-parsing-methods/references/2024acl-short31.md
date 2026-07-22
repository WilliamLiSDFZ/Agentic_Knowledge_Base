---
title: "What Does Parameter-free Probing Really Uncover?"
source: "https://aclanthology.org/2024.acl-short.31/"
categories: ['language-model-representations-and-embedding-spaces', 'unsupervised-and-structured-syntactic-parsing-methods']
tags: ['probing', 'parameter-free', 'syntactic-representations']
venue: "ACL 2024"
tldr: "Analyzes what parameter-free probing methods genuinely uncover about linguistic structure in large language models."
---

# What Does Parameter-free Probing Really Uncover?

**Source**: [https://aclanthology.org/2024.acl-short.31/](https://aclanthology.org/2024.acl-short.31/)

**TLDR**: Analyzes what parameter-free probing methods genuinely uncover about linguistic structure in large language models.

## Abstract

AbstractSupervised approaches to probing large language models (LLMs) have been criticized of using pre-defined theory-laden target labels. As an alternative, parameter-free probing constructs structural representations bottom-up via information derived from the LLM alone. This has been suggested to capture a genuine “LLM-internal grammar”. However, its relation to familiar linguistic formalisms remains unclear. I extend prior work on a parameter-free probing technique called perturbed masking applied to BERT, by comparing its results to the Universal Dependencies (UD) formalism for English. The results highlight several major discrepancies between BERT and UD, which lack correlates in linguistic theory. This raises the question of whether human grammar is the correct analogy to interpret BERT in the first place.