---
title: "Pro-Woman, Anti-Man? Identifying Gender Bias in Stance Detection"
source: "https://aclanthology.org/2024.findings-acl.192/"
pdf_url: ""
categories: ['bias-and-fairness-in-llms', 'multilingual-text-classification-and-sentiment-analysis']
tags: ['gender-bias', 'stance-detection', 'dataset-construction']
venue: "ACL 2024"
tldr: "A 36k-sample GenderStance dataset is constructed to measure and analyze gender bias in NLP stance detection models."
---

# Pro-Woman, Anti-Man? Identifying Gender Bias in Stance Detection

**Source**: [https://aclanthology.org/2024.findings-acl.192/](https://aclanthology.org/2024.findings-acl.192/)

**TLDR**: A 36k-sample GenderStance dataset is constructed to measure and analyze gender bias in NLP stance detection models.

## Abstract

AbstractGender bias has been widely observed in NLP models, which has the potential to perpetuate harmful stereotypes and discrimination. In this paper, we construct a dataset GenderStance of 36k samples to measure gender bias in stance detection, determining whether models consistently predict the same stance for a particular gender group. We find that all models are gender-biased and prone to classify sentences that contain male nouns as Against and those with female nouns as Favor. Moreover, extensive experiments indicate that sources of gender bias stem from the fine-tuning data and the foundation model itself. We will publicly release our code and dataset.