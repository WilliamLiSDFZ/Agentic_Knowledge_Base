---
title: "On the Effect of (Near) Duplicate Subwords in Language Modelling"
source: "https://aclanthology.org/2024.findings-acl.571/"
categories: ['transformer-architecture-analysis-and-design']
tags: ['tokenization', 'subword-duplication', 'language-modeling-efficiency']
venue: "ACL 2024"
tldr: "Analyzes how near-duplicate subword tokens in tokenization negatively affect language model training efficiency."
---

# On the Effect of (Near) Duplicate Subwords in Language Modelling

**Source**: [https://aclanthology.org/2024.findings-acl.571/](https://aclanthology.org/2024.findings-acl.571/)

**TLDR**: Analyzes how near-duplicate subword tokens in tokenization negatively affect language model training efficiency.

## Abstract

AbstractTokenisation is a core part of language models (LMs). It involves splitting a character sequence into subwords which are assigned random indices before being served to the LM. However, this process—while typically lossless—may lead to less efficient LM training, because it removes character-level information, thereby making it more difficult to generalise across similar subwords, such as *now* and *Now*. We refer to such subwords as **near duplicates**. In this paper, we study the impact of near duplicate subwords on LM training efficiency. First, we design an experiment that gives us an upper bound to how much we should expect a model to improve if we could perfectly generalise across near duplicates. We do this, by duplicating each token in our LM’s vocabulary, creating perfectly equivalent classes of subwords. Experimentally, we find that LMs need roughly 17% more data when trained in a fully duplicated setting. Second, we investigate the impact of naturally occurring near duplicates on LMs. Here, we see that deduplicating them considerably hurts LM performance; but that this loss in performance can be easily mitigated.