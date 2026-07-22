---
title: "Topic Modeling for Short Texts with Large Language Models"
source: "https://aclanthology.org/2024.acl-srw.3/"
pdf_url: ""
categories: ['topic-modeling-and-essay-evaluation', 'natural-language-processing-information-extraction']
tags: ['topic-modeling', 'short-texts', 'LLMs']
venue: "ACL 2024"
tldr: "LLMs are leveraged to overcome word co-occurrence limitations in topic modeling for short texts."
---

# Topic Modeling for Short Texts with Large Language Models

**Source**: [https://aclanthology.org/2024.acl-srw.3/](https://aclanthology.org/2024.acl-srw.3/)

**TLDR**: LLMs are leveraged to overcome word co-occurrence limitations in topic modeling for short texts.

## Abstract

AbstractAs conventional topic models rely on word co-occurrence to infer latent topics, topic modeling for short texts has been a long-standing challenge. Large Language Models (LLMs) can potentially overcome this challenge by contextually learning the meanings of words via pretraining. In this paper, we study two approaches to using LLMs for topic modeling: parallel prompting and sequential prompting. Input length limitations prevent LLMs from processing many texts at once. However, an arbitrary number of texts can be handled by LLMs by splitting the texts into smaller subsets and processing them in parallel or sequentially. Our experimental results demonstrate that our methods can identify more coherent topics than existing ones while maintaining the diversity of the induced topics. Furthermore, we found that the inferred topics cover the input texts to some extent, while hallucinated topics are hardly generated.