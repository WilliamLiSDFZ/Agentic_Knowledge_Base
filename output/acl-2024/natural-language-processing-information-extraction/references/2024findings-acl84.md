---
title: "Temporal Validity Change Prediction"
source: "https://aclanthology.org/2024.findings-acl.84/"
pdf_url: ""
categories: ['social-ai-temporal-dynamics-evaluation', 'natural-language-processing-information-extraction']
tags: ['temporal-validity', 'text-classification', 'temporal-reasoning']
venue: "ACL 2024"
tldr: "A new task predicts changes in temporal validity of statements over time for downstream applications like recommender systems."
---

# Temporal Validity Change Prediction

**Source**: [https://aclanthology.org/2024.findings-acl.84/](https://aclanthology.org/2024.findings-acl.84/)

**TLDR**: A new task predicts changes in temporal validity of statements over time for downstream applications like recommender systems.

## Abstract

AbstractTemporal validity is an important property of text that has many downstream applications, such as recommender systems, conversational AI, and user status tracking. Existing benchmarking tasks often require models to identify the temporal validity duration of a single statement. However, many data sources contain additional context, such as successive sentences in a story or posts on a social media profile. This context may alter the duration for which the originally collected statement is expected to be valid. We propose Temporal Validity Change Prediction, a natural language processing task benchmarking the capability of machine learning models to detect context statements that induce such change. We create a dataset consisting of temporal target statements sourced from Twitter and crowdsource corresponding context statements. We then benchmark a set of transformer-based language models on our dataset. Finally, we experiment with a multitasking approach to improve the state-of-the-art performance.