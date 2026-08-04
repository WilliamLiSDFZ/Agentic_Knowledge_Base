---
title: "Reducing Item Discrepancy via Differentially Private Robust Embedding Alignment for Privacy-Preserving Cross Domain Recommendation"
source: "https://proceedings.mlr.press/v235/liu24cf.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/liu24cf/liu24cf.pdf"
categories: ['privacy-preserving-federated-and-distributed-learning', 'information-retrieval-and-recommendation-systems']
tags: ['cross-domain-recommendation', 'differential-privacy', 'embedding-alignment', 'item-discrepancy', 'privacy-preserving']
venue: "ICML 2024"
tldr: "A differentially private robust embedding alignment method for cross-domain recommendation that reduces item discrepancy while preserving user privacy."
---

# Reducing Item Discrepancy via Differentially Private Robust Embedding Alignment for Privacy-Preserving Cross Domain Recommendation

**Source**: [https://proceedings.mlr.press/v235/liu24cf.html](https://proceedings.mlr.press/v235/liu24cf.html)

**TLDR**: A differentially private robust embedding alignment method for cross-domain recommendation that reduces item discrepancy while preserving user privacy.

## Abstract

Cross-Domain Recommendation (CDR) have become increasingly appealing by leveraging useful information to tackle the data sparsity problem across domains. Most of latest CDR models assume that domain-shareable user-item information (e.g., rating and review on overlapped users or items) are accessible across domains. However, these assumptions become impractical due to the strict data privacy protection policy. In this paper, we propose Reducing Item Discrepancy (RidCDR) model on solving Privacy-Preserving Cross-Domain Recommendation (PPCDR) problem. Specifically, we aim to enhance the model performance on both source and target domains without overlapped users and items while protecting the data privacy. We innovatively propose private-robust embedding alignment module in RidCDR for knowledge sharing across domains while avoiding negative transfer privately. Our empirical study on Amazon and Douban datasets demonstrates that RidCDR significantly outperforms the state-of-the-art models under the PPCDR without overlapped users and items.