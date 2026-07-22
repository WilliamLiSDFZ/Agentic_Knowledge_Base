---
title: "Investigating Subtler Biases in LLMs: Ageism, Beauty, Institutional, and Nationality Bias in Generative Models"
source: "https://aclanthology.org/2024.findings-acl.530/"
pdf_url: ""
categories: ['bias-and-fairness-in-llms']
tags: ['ageism', 'beauty-bias', 'nationality-bias', 'llm-bias']
venue: "ACL 2024"
tldr: "Investigates subtle biases including ageism, beauty, institutional, and nationality bias in large language models."
---

# Investigating Subtler Biases in LLMs: Ageism, Beauty, Institutional, and Nationality Bias in Generative Models

**Source**: [https://aclanthology.org/2024.findings-acl.530/](https://aclanthology.org/2024.findings-acl.530/)

**TLDR**: Investigates subtle biases including ageism, beauty, institutional, and nationality bias in large language models.

## Abstract

AbstractLLMs are increasingly powerful and widely used to assist users in a variety of tasks. This use risks introducing LLM biases into consequential decisions such as job hiring, human performance evaluation, and criminal sentencing. Bias in NLP systems along the lines of gender and ethnicity has been widely studied, especially for specific stereotypes (e.g., Asians are good at math). In this paper, we investigate bias along less-studied but still consequential, dimensions, such as age and beauty, measuring subtler correlated decisions that LLMs make between social groups and unrelated positive and negative attributes. Although these subtler biases are understudied they follow people as much as gender and ethnicity do. So, we want to see whether they also follow one with LLMs.We introduce a template-generated dataset of sentence completion tasks that asks the model to select the most appropriate attribute to complete an evaluative statement about a person described as a member of a specific social group. We also reverse the completion task to select the social group based on an attribute. We report the correlations that we find for 4 cutting-edge LLMs. This dataset can be used as a benchmark to evaluate progress in more generalized biases and the templating technique can be used to expand the benchmark with minimal additional human annotation.