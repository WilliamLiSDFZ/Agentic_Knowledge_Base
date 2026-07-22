---
title: "RePALM: Popular Quote Tweet Generation via Auto-Response Augmentation"
source: "https://aclanthology.org/2024.findings-acl.570/"
pdf_url: ""
categories: ['social-ai-temporal-dynamics-evaluation', 'llm-based-ranking-and-recommendation']
tags: ['quote-tweet', 'text-generation', 'social-media', 'popularity-prediction', 'augmentation']
venue: "ACL 2024"
tldr: "Introduces RePALM, a framework for generating popular quote tweets via auto-response augmentation to boost social engagement."
---

# RePALM: Popular Quote Tweet Generation via Auto-Response Augmentation

**Source**: [https://aclanthology.org/2024.findings-acl.570/](https://aclanthology.org/2024.findings-acl.570/)

**TLDR**: Introduces RePALM, a framework for generating popular quote tweets via auto-response augmentation to boost social engagement.

## Abstract

AbstractA quote tweet enables users to share others’ content while adding their own commentary. In order to enhance public engagement through quote tweets, we investigate the task of generating popular quote tweets. This task aims to produce quote tweets that garner higher popularity, as indicated by increased likes, replies, and retweets. Despite the impressive language generation capabilities of large language models (LLMs), there has been limited research on how LLMs can effectively learn the popularity of text to better engage the public. Therefore, we introduce a novel approach called Response-augmented Popularity-Aligned Language Model (RePALM), which aligns language generation with popularity by leveraging insights from augmented auto-responses provided by readers. We utilize the Proximal Policy Optimization framework with a dual-reward mechanism to jointly optimize for the popularity of the quote tweet and its consistency with the auto-responses. In our experiments, we collected two datasets consisting of quote tweets containing external links and those referencing others’ tweets. Extensive results demonstrate the superiority of RePALM over advanced language models that do not incorporate response augmentation.