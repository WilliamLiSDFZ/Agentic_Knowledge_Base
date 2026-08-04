---
title: "Improved Bounds for Pure Private Agnostic Learning: Item-Level and User-Level Privacy"
source: "https://proceedings.mlr.press/v235/li24bq.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/li24bq/li24bq.pdf"
categories: ['privacy-preserving-federated-and-distributed-learning', 'learning-with-imperfect-data-and-bias']
tags: ['differential-privacy', 'agnostic-learning', 'user-level-privacy']
venue: "ICML 2024"
tldr: "Derives improved bounds for pure private agnostic learning under both item-level and user-level privacy settings."
---

# Improved Bounds for Pure Private Agnostic Learning: Item-Level and User-Level Privacy

**Source**: [https://proceedings.mlr.press/v235/li24bq.html](https://proceedings.mlr.press/v235/li24bq.html)

**TLDR**: Derives improved bounds for pure private agnostic learning under both item-level and user-level privacy settings.

## Abstract

Machine Learning has made remarkable progress in a wide range of fields. In many scenarios, learning is performed on datasets involving sensitive information, in which privacy protection is essential for learning algorithms. In this work, we study pure private learning in the agnostic model – a framework reflecting the learning process in practice. We examine the number of users required under item-level (where each user contributes one example) and user-level (where each user contributes multiple examples) privacy and derive several improved upper bounds. For item-level privacy, our algorithm achieves a near optimal bound for general concept classes. We extend this to the user-level setting, rendering a tighter upper bound than the one proved by Ghazi et al. (2023). Lastly, we consider the problem of learning thresholds under user-level privacy and present an algorithm with a nearly tight user complexity.