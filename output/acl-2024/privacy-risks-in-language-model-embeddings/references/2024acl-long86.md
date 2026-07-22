---
title: "Probing Language Models for Pre-training Data Detection"
source: "https://aclanthology.org/2024.acl-long.86/"
pdf_url: ""
categories: ['llm-security-robustness-and-detection', 'privacy-risks-in-language-model-embeddings']
tags: ['data-contamination', 'membership-inference', 'pretraining-detection']
venue: "ACL 2024"
tldr: "Investigates probing techniques to detect whether specific data was used in LLM pretraining to address contamination concerns."
---

# Probing Language Models for Pre-training Data Detection

**Source**: [https://aclanthology.org/2024.acl-long.86/](https://aclanthology.org/2024.acl-long.86/)

**TLDR**: Investigates probing techniques to detect whether specific data was used in LLM pretraining to address contamination concerns.

## Abstract

AbstractLarge Language Models (LLMs) have shown their impressive capabilities, while also raising concerns about the data contamination problems due to privacy issues and leakage of benchmark datasets in the pre-training phase. Therefore, it is vital to detect the contamination by checking whether an LLM has been pre-trained on the target texts. Recent studies focus on the generated texts and compute perplexities, which are superficial features and not reliable. In this study, we propose to utilize the probing technique for pre-training data detection by examining the model’s internal activations. Our method is simple and effective and leads to more trustworthy pre-training data detection. Additionally, we propose ArxivMIA, a new challenging benchmark comprising arxiv abstracts from Computer Science and Mathematics categories. Our experiments demonstrate that our method outperforms all baselines, and achieves state-of-the-art performance on both WikiMIA and ArxivMIA, with additional experiments confirming its efficacy.