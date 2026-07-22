---
title: "Pushing the Limits of Low-Resource NER Using LLM Artificial Data Generation"
source: "https://aclanthology.org/2024.findings-acl.575/"
categories: ['natural-language-processing-information-extraction', 'language-technology-cultural-linguistic-diversity']
tags: ['named-entity-recognition', 'low-resource', 'data-augmentation']
venue: "ACL 2024"
tldr: "Proposes using LLM-generated artificial data to push the limits of low-resource named entity recognition."
---

# Pushing the Limits of Low-Resource NER Using LLM Artificial Data Generation

**Source**: [https://aclanthology.org/2024.findings-acl.575/](https://aclanthology.org/2024.findings-acl.575/)

**TLDR**: Proposes using LLM-generated artificial data to push the limits of low-resource named entity recognition.

## Abstract

AbstractNamed Entity Recognition (NER) is an important task, but to achieve great performance, it is usually necessary to collect a large amount of labeled data, incurring high costs. In this paper, we propose using open-source Large Language Models (LLM) to generate NER data with only a few labeled examples, reducing the cost of human annotations. Our proposed method is very simple and can perform well using only a few labeled data points. Experimental results on diverse low-resource NER datasets show that our proposed data generation method can significantly improve the baseline. Additionally, our method can be used to augment datasets with class-imbalance problems and consistently improves model performance on macro-F1 metrics.