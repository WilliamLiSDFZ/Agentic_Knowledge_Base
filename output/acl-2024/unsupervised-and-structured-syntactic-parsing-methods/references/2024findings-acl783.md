---
title: "Evaluating Structural Generalization in Neural Machine Translation"
source: "https://aclanthology.org/2024.findings-acl.783/"
pdf_url: ""
categories: ['unsupervised-and-structured-syntactic-parsing-methods', 'nlp-benchmark-design-and-interpretability']
tags: ['compositional-generalization', 'neural-machine-translation', 'structural-generalization', 'benchmark', 'syntactic-structures']
venue: "ACL 2024"
tldr: "This paper evaluates compositional and structural generalization capabilities of neural machine translation models on novel syntactic combinations."
---

# Evaluating Structural Generalization in Neural Machine Translation

**Source**: [https://aclanthology.org/2024.findings-acl.783/](https://aclanthology.org/2024.findings-acl.783/)

**TLDR**: This paper evaluates compositional and structural generalization capabilities of neural machine translation models on novel syntactic combinations.

## Abstract

AbstractCompositional generalization refers to the ability to generalize to novel combinations of previously observed words and syntactic structures.Since it is regarded as a desired property of neural models, recent work has assessed compositional generalization in machine translation as well as semantic parsing.However, previous evaluations with machine translation have focused mostly on lexical generalization (i.e., generalization to unseen combinations of known words).Thus, it remains unclear to what extent models can translate sentences that require structural generalization (i.e., generalization to different sorts of syntactic structures).To address this question, we construct SGET, a machine translation dataset covering various types of compositional generalization with control of words and sentence structures.We evaluate neural machine translation models on SGET and show that they struggle more in structural generalization than in lexical generalization.We also find different performance trends in semantic parsing and machine translation, which indicates the importance of evaluations across various tasks.