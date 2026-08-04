---
title: "Binary Decomposition: A Problem Transformation Perspective for Open-Set Semi-Supervised Learning"
source: "https://proceedings.mlr.press/v235/hang24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/hang24a/hang24a.pdf"
categories: ['learning-with-imperfect-data-and-bias', 'anomaly-and-out-of-distribution-detection']
tags: ['semi-supervised-learning', 'open-set', 'binary-decomposition']
venue: "ICML 2024"
tldr: "A binary decomposition problem transformation is proposed for open-set semi-supervised learning to handle outliers from novel categories in unlabeled data."
---

# Binary Decomposition: A Problem Transformation Perspective for Open-Set Semi-Supervised Learning

**Source**: [https://proceedings.mlr.press/v235/hang24a.html](https://proceedings.mlr.press/v235/hang24a.html)

**TLDR**: A binary decomposition problem transformation is proposed for open-set semi-supervised learning to handle outliers from novel categories in unlabeled data.

## Abstract

Semi-supervised learning (SSL) is a classical machine learning paradigm dealing with labeled and unlabeled data. However, it often suffers performance degradation in real-world open-set scenarios, where unlabeled data contains outliers from novel categories that do not appear in labeled data. Existing studies commonly tackle this challenging open-set SSL problem with detect-and-filter strategy, which attempts to purify unlabeled data by detecting and filtering outliers. In this paper, we propose a novel binary decomposition strategy, which refrains from error-prone procedure of outlier detection by directly transforming the original open-set SSL problem into a number of standard binary SSL problems. Accordingly, a concise yet effective approach named BDMatch is presented. BDMatch confronts two attendant issues brought by binary decomposition, i.e. class-imbalance and representation-compromise, with adaptive logit adjustment and label-specific feature learning respectively. Comprehensive experiments on diversified benchmarks clearly validate the superiority of BDMatch as well as the effectiveness of our binary decomposition strategy.