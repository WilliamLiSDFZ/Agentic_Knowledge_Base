---
title: "OTMatch: Improving Semi-Supervised Learning with Optimal Transport"
source: "https://proceedings.mlr.press/v235/tan24f.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/tan24f/tan24f.pdf"
categories: ['learning-with-imperfect-data-and-bias']
tags: ['semi-supervised-learning', 'optimal-transport', 'pseudo-labels']
venue: "ICML 2024"
tldr: "OTMatch improves semi-supervised learning by using optimal transport to align pseudo-label distributions with true class distributions."
---

# OTMatch: Improving Semi-Supervised Learning with Optimal Transport

**Source**: [https://proceedings.mlr.press/v235/tan24f.html](https://proceedings.mlr.press/v235/tan24f.html)

**TLDR**: OTMatch improves semi-supervised learning by using optimal transport to align pseudo-label distributions with true class distributions.

## Abstract

Semi-supervised learning has made remarkable strides by effectively utilizing a limited amount of labeled data while capitalizing on the abundant information present in unlabeled data. However, current algorithms often prioritize aligning image predictions with specific classes generated through self-training techniques, thereby neglecting the inherent relationships that exist within these classes. In this paper, we present a new approach called OTMatch, which leverages semantic relationships among classes by employing an optimal transport loss function to match distributions. We conduct experiments on many standard vision and language datasets. The empirical results show improvements in our method above baseline, this demonstrates the effectiveness and superiority of our approach in harnessing semantic relationships to enhance learning performance in a semi-supervised setting.