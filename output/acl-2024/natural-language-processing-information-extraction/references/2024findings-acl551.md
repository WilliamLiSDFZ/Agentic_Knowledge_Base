---
title: "Evidence Retrieval is almost All You Need for Fact Verification"
source: "https://aclanthology.org/2024.findings-acl.551/"
pdf_url: ""
categories: ['computational-misinformation-narrative-framing-detection', 'natural-language-processing-information-extraction']
tags: ['fact-verification', 'evidence-retrieval', 'claim-verification']
venue: "ACL 2024"
tldr: "High-quality evidence retrieval is shown to be the dominant factor in fact verification, outweighing sophisticated claim verification modules."
---

# Evidence Retrieval is almost All You Need for Fact Verification

**Source**: [https://aclanthology.org/2024.findings-acl.551/](https://aclanthology.org/2024.findings-acl.551/)

**TLDR**: High-quality evidence retrieval is shown to be the dominant factor in fact verification, outweighing sophisticated claim verification modules.

## Abstract

AbstractCurrent fact verification methods generally follow the two-stage training paradigm: evidence retrieval and claim verification. While existing works focus on developing sophisticated claim verification modules, the fundamental importance of evidence retrieval is largely ignored. Existing approaches usually adopt the heuristic semantic similarity-based retrieval strategy, resulting in the task-irrelevant evidence and undesirable performance. In this paper, we concentrate on evidence retrieval and propose a Retrieval-Augmented Verification framework RAV, consisting of two major modules: the hybrid evidence retrieval and the joint fact verification. Hybrid evidence retrieval module incorporates an efficient retriever for preliminary pruning of candidate evidence, succeeded by a ranker that generates more precise sorting results. Under this end-to-end training paradigm, gradients from the claim verification can be back-propagated to enhance evidence selection. Experimental results on FEVER dataset demonstrate the superiority of RAV.