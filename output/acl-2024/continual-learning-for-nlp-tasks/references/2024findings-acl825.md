---
title: "DADA: Distribution-Aware Domain Adaptation of PLMs for Information Retrieval"
source: "https://aclanthology.org/2024.findings-acl.825/"
pdf_url: ""
categories: ['language-model-representations-and-embedding-spaces', 'continual-learning-for-nlp-tasks']
tags: ['domain-adaptation', 'information-retrieval', 'distribution-shift']
venue: "ACL 2024"
tldr: "DADA improves pre-trained language model adaptation for retrieval by accounting for distribution shifts between source and target domains."
---

# DADA: Distribution-Aware Domain Adaptation of PLMs for Information Retrieval

**Source**: [https://aclanthology.org/2024.findings-acl.825/](https://aclanthology.org/2024.findings-acl.825/)

**TLDR**: DADA improves pre-trained language model adaptation for retrieval by accounting for distribution shifts between source and target domains.

## Abstract

AbstractPre-trained language models (PLMs) exhibit promise in retrieval tasks but struggle with out-of-domain data due to distribution shifts.Addressing this, generative domain adaptation (DA), known as GPL, tackles distribution shifts by generating pseudo queries and labels to train models for predicting query-document relationships in new domains.However, it overlooks the domain distribution, causing the model to struggle with aligning the distribution in the target domain.We, therefore, propose a Distribution-Aware Domain Adaptation (DADA) to guide the model to consider the domain distribution knowledge at the level of both a single document and the corpus, which is referred to as observation-level feedback and domain-level feedback, respectively.Our method effectively adapts the model to the target domain and expands document representation to unseen gold query terms using domain and observation feedback, as demonstrated by empirical results on the BEIR benchmark.