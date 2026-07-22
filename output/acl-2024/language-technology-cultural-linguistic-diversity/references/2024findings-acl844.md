---
title: "mCSQA: Multilingual Commonsense Reasoning Dataset with Unified Creation Strategy by Language Models and Humans"
source: "https://aclanthology.org/2024.findings-acl.844/"
categories: ['language-technology-cultural-linguistic-diversity']
tags: ['multilingual', 'commonsense-reasoning', 'dataset-creation', 'language-models']
venue: "ACL 2024"
tldr: "Introduces mCSQA, a multilingual commonsense reasoning dataset created through a unified strategy combining language models and human annotators."
---

# mCSQA: Multilingual Commonsense Reasoning Dataset with Unified Creation Strategy by Language Models and Humans

**Source**: [https://aclanthology.org/2024.findings-acl.844/](https://aclanthology.org/2024.findings-acl.844/)

**TLDR**: Introduces mCSQA, a multilingual commonsense reasoning dataset created through a unified strategy combining language models and human annotators.

## Abstract

AbstractIt is very challenging to curate a dataset for language-specific knowledge and common sense in order to evaluate natural language understanding capabilities of language models. Due to the limitation in the availability of annotators, most current multilingual datasets are created through translation, which cannot evaluate such language-specific aspects. Therefore, we propose Multilingual CommonsenseQA (mCSQA) based on the construction process of CSQA but leveraging language models for a more efficient construction, e.g., by asking LM to generate questions/answers, refine answers and verify QAs followed by reduced human efforts for verification. Constructed dataset is a benchmark for cross-lingual language-transfer capabilities of multilingual LMs, and experimental results showed high language-transfer capabilities for questions that LMs could easily solve, but lower transfer capabilities for questions requiring deep knowledge or commonsense. This highlights the necessity of language-specific datasets for evaluation and training. Finally, our method demonstrated that multilingual LMs could create QA including language-specific knowledge, significantly reducing the dataset creation cost compared to manual creation. The datasets are available at https://huggingface.co/datasets/yusuke1997/mCSQA.