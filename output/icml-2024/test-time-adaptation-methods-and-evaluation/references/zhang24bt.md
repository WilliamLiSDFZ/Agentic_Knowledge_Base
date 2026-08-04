---
title: "Rethinking Guidance Information to Utilize Unlabeled Samples: A Label Encoding Perspective"
source: "https://proceedings.mlr.press/v235/zhang24bt.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/zhang24bt/zhang24bt.pdf"
categories: ['learning-with-imperfect-data-and-bias', 'test-time-adaptation-methods-and-evaluation']
tags: ['semi-supervised-learning', 'label-encoding', 'entropy-minimization', 'unlabeled-data', 'ERM']
venue: "ICML 2024"
tldr: "Proposes a label encoding perspective to better exploit unlabeled samples beyond entropy minimization in empirical risk minimization."
---

# Rethinking Guidance Information to Utilize Unlabeled Samples: A Label Encoding Perspective

**Source**: [https://proceedings.mlr.press/v235/zhang24bt.html](https://proceedings.mlr.press/v235/zhang24bt.html)

**TLDR**: Proposes a label encoding perspective to better exploit unlabeled samples beyond entropy minimization in empirical risk minimization.

## Abstract

Empirical Risk Minimization (ERM) is fragile in scenarios with insufficient labeled samples. A vanilla extension of ERM to unlabeled samples is Entropy Minimization (EntMin), which employs the soft-labels of unlabeled samples to guide their learning. However, EntMin emphasizes prediction discriminability while neglecting prediction diversity. To alleviate this issue, in this paper, we rethink the guidance information to utilize unlabeled samples. By analyzing the learning objective of ERM, we find that the guidance information for labeled samples in a specific category is the corresponding label encoding. Inspired by this finding, we propose a Label-Encoding Risk Minimization (LERM). It first estimates the label encodings through prediction means of unlabeled samples and then aligns them with their corresponding ground-truth label encodings. As a result, the LERM ensures both prediction discriminability and diversity, and it can be integrated into existing methods as a plugin. Theoretically, we analyze the relationships between LERM and ERM as well as EntMin. Empirically, we verify the superiority of the LERM under several label insufficient scenarios. The codes are available at https://github.com/zhangyl660/LERM.