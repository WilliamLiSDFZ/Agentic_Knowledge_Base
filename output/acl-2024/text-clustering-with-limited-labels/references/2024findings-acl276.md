---
title: "X-Shot: A Unified System to Handle Frequent, Few-shot and Zero-shot Learning Simultaneously in Classification"
source: "https://aclanthology.org/2024.findings-acl.276/"
pdf_url: ""
categories: ['text-clustering-with-limited-labels', 'nlp-text-classification-applied-tasks']
tags: ['few-shot-learning', 'zero-shot-learning', 'unified-classification']
venue: "ACL 2024"
tldr: "Proposes X-Shot, a unified framework that simultaneously handles frequent-shot, few-shot, and zero-shot classification scenarios."
---

# X-Shot: A Unified System to Handle Frequent, Few-shot and Zero-shot Learning Simultaneously in Classification

**Source**: [https://aclanthology.org/2024.findings-acl.276/](https://aclanthology.org/2024.findings-acl.276/)

**TLDR**: Proposes X-Shot, a unified framework that simultaneously handles frequent-shot, few-shot, and zero-shot classification scenarios.

## Abstract

AbstractIn recent years, few-shot and zero-shot learning, which learn to predict labels with limited annotated instances, have garnered significant attention. Traditional approaches often treat frequent-shot (freq-shot; labels with abundant instances), few-shot, and zero-shot learning as distinct challenges, optimizing systems for just one of these scenarios. Yet, in real-world settings, label occurrences vary greatly. Some of them might appear thousands of times, while others might only appear sporadically or not at all. For practical deployment, it is crucial that a system can adapt to any label occurrence. We introduce a novel classification challenge: **X-shot**, reflecting a real-world context where freq-shot, few-shot, and zero-shot labels co-occur without predefined limits. Here, **X** can span from 0 to positive infinity. The crux of **X-shot** centers on open-domain generalization and devising a system versatile enough to manage various label scenarios. To solve **X-shot**, we propose **BinBin** (**B**inary **IN**ference **B**ased on **IN**struction following) that leverages the Indirect Supervision from a large collection of NLP tasks via instruction following, bolstered by Weak Supervision provided by large language models. **BinBin** surpasses previous state-of-the-art techniques on three benchmark datasets across multiple domains. To our knowledge, this is the first work addressing **X-shot** learning, where **X** remains variable.