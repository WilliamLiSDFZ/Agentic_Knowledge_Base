---
title: "An Information-Theoretic Approach to Analyze NLP Classification Tasks"
source: "https://aclanthology.org/2024.acl-long.32/"
categories: ['nlp-benchmark-design-and-interpretability', 'causal-reasoning-and-explanation-in-nlp']
tags: ['information-theory', 'text-classification', 'input-contribution']
venue: "ACL 2024"
tldr: "An information-theoretic framework quantifies the influence of single and multiple text inputs on NLP classification tasks."
---

# An Information-Theoretic Approach to Analyze NLP Classification Tasks

**Source**: [https://aclanthology.org/2024.acl-long.32/](https://aclanthology.org/2024.acl-long.32/)

**TLDR**: An information-theoretic framework quantifies the influence of single and multiple text inputs on NLP classification tasks.

## Abstract

AbstractUnderstanding the contribution of the inputs on the output is useful across many tasks. This work provides an information-theoretic framework to analyse the influence of inputs for text classification tasks. Natural language processing (NLP) tasks take either a single or multiple text elements to predict an output variable. Each text element has two components: the semantic meaning and a linguistic realization. Multiple-choice reading comprehension (MCRC) and sentiment classification (SC) are selected to showcase the framework. For MCRC, it is found that the relative context influence on the output reduces on more challenging datasets. In particular, more challenging contexts allows greater variation in the question complexity. Hence, test creators need to carefully consider the choice of the context when designing multiple-choice questions for assessment. For SC, it is found the semantic meaning of the input dominates compared to its linguistic realization when determining the sentiment. The framework is made available at: https://github.com/WangLuran/nlp-element-influence.