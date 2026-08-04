---
title: "Domain-wise Data Acquisition to Improve Performance under Distribution Shift"
source: "https://proceedings.mlr.press/v235/he24f.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/he24f/he24f.pdf"
categories: ['data-selection-and-active-learning-methods', 'learning-with-imperfect-data-and-bias']
tags: ['data-acquisition', 'distribution-shift', 'domain-generalization']
venue: "ICML 2024"
tldr: "A domain-wise data acquisition strategy is proposed to improve model performance under distribution shift from a data-centric perspective."
---

# Domain-wise Data Acquisition to Improve Performance under Distribution Shift

**Source**: [https://proceedings.mlr.press/v235/he24f.html](https://proceedings.mlr.press/v235/he24f.html)

**TLDR**: A domain-wise data acquisition strategy is proposed to improve model performance under distribution shift from a data-centric perspective.

## Abstract

Despite notable progress in enhancing the capability of machine learning against distribution shifts, training data quality remains a bottleneck for cross-distribution generalization. Recently, from a data-centric perspective, there have been considerable efforts to improve model performance through refining the preparation of training data. Inspired by realistic scenarios, this paper addresses a practical requirement of acquiring training samples from various domains on a limited budget to facilitate model generalization to target test domain with distribution shift. Our empirical evidence indicates that the advance in data acquisition can significantly benefit the model performance on shifted data. Additionally, by leveraging unlabeled test domain data, we introduce a Domain-wise Active Acquisition framework. This framework iteratively optimizes the data acquisition strategy as training samples are accumulated, theoretically ensuring the effective approximation of test distribution. Extensive real-world experiments demonstrate our proposal’s advantages in machine learning applications. The code is available at https://github.com/dongbaili/DAA.