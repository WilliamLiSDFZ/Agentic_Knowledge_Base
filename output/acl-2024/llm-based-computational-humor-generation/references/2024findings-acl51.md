---
title: "Are U a Joke Master? Pun Generation via Multi-Stage Curriculum Learning towards a Humor LLM"
source: "https://aclanthology.org/2024.findings-acl.51/"
pdf_url: ""
categories: ['llm-based-computational-humor-generation', 'llm-training-alignment-and-evaluation']
tags: ['pun-generation', 'humor', 'curriculum-learning', 'LLM', 'fine-tuning']
venue: "ACL 2024"
tldr: "Proposes a multi-stage curriculum learning approach to improve pun and humor generation in large language models."
---

# Are U a Joke Master? Pun Generation via Multi-Stage Curriculum Learning towards a Humor LLM

**Source**: [https://aclanthology.org/2024.findings-acl.51/](https://aclanthology.org/2024.findings-acl.51/)

**TLDR**: Proposes a multi-stage curriculum learning approach to improve pun and humor generation in large language models.

## Abstract

AbstractAlthough large language models (LLMs) acquire extensive world knowledge and some reasoning abilities, their proficiency in generating humorous sentences remains a challenge. Previous research has demonstrated that the humor generation capabilities of ChatGPT are confined to producing merely 25 unique jokes. In this work, we concentrate on endowing LLMs with the ability of generating puns, a particular category of humor by preference learning method. We propose a multi-stage curriculum preference learning framework to optimize both pun structure preferences and humor preferences. Specifically, we improve the Direct Preference Optimization (DPO) algorithm to address the challenge of multi-objective alignment problem. Besides, to facilitate further advancement in this field, we collect a Chinese Pun (ChinesePun) dataset, containing 2.1k puns and corresponding annotations. Experimental results on both Chinese and English benchmark datasets demonstrate that our method significantly outperforms all the baseline models.