---
title: "Don’t Augment, Rewrite? Assessing Abusive Language Detection with Synthetic Data"
source: "https://aclanthology.org/2024.findings-acl.669/"
pdf_url: ""
categories: ['hate-speech-and-toxic-content-detection']
tags: ['abusive-language-detection', 'synthetic-data', 'data-augmentation']
venue: "ACL 2024"
tldr: "Investigates replacing real abusive language datasets with synthetic rewrites for training content moderation classifiers."
---

# Don’t Augment, Rewrite? Assessing Abusive Language Detection with Synthetic Data

**Source**: [https://aclanthology.org/2024.findings-acl.669/](https://aclanthology.org/2024.findings-acl.669/)

**TLDR**: Investigates replacing real abusive language datasets with synthetic rewrites for training content moderation classifiers.

## Abstract

AbstractResearch on abusive language detection and content moderation is crucial to combat online harm. However, current limitations set by regulatory bodies and social media platforms can make it difficult to share collected data. We address this challenge by exploring the possibility to replace existing datasets in English for abusive language detection with synthetic data obtained by rewriting original texts with an instruction-based generative model.We show that such data can be effectively used to train a classifier whose performance is in line, and sometimes better, than a classifier trained on original data. Training with synthetic data also seems to improve robustness in a cross-dataset setting. A manual inspection of the generated data confirms that rewriting makes it impossible to retrieve the original texts online.