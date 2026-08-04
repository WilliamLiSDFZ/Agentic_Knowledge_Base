---
title: "Correlation-Induced Label Prior for Semi-Supervised Multi-Label Learning"
source: "https://proceedings.mlr.press/v235/liu24bt.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/liu24bt/liu24bt.pdf"
categories: ['learning-with-imperfect-data-and-bias', 'clustering-methods-and-multi-view-learning']
tags: ['semi-supervised-learning', 'multi-label-learning', 'label-correlation', 'label-prior', 'unlabeled-data']
venue: "ICML 2024"
tldr: "A correlation-induced label prior method for semi-supervised multi-label learning that leverages label correlations from minimal labeled data to improve performance on unlabeled data."
---

# Correlation-Induced Label Prior for Semi-Supervised Multi-Label Learning

**Source**: [https://proceedings.mlr.press/v235/liu24bt.html](https://proceedings.mlr.press/v235/liu24bt.html)

**TLDR**: A correlation-induced label prior method for semi-supervised multi-label learning that leverages label correlations from minimal labeled data to improve performance on unlabeled data.

## Abstract

Semi-supervised multi-label learning (SSMLL) aims to address the challenge of limited labeled data availability in multi-label learning (MLL) by leveraging unlabeled data to improve the model’s performance. Due to the difficulty of estimating the reliable label correlation on minimal multi-labeled data, previous SSMLL methods fail to unlash the power of the correlation among multiple labels to improve the performance of the predictive model in SSMLL. To deal with this problem, we propose a novel SSMLL method named PCLP where the correlation-induced label prior is inferred to enhance the pseudo-labeling instead of dirtily estimating the correlation among labels. Specifically, we construct the correlated label prior probability distribution using structural causal model (SCM), constraining the correlations of generated pseudo-labels to conform to the prior, which can be integrated into a variational label enhancement framework optimized by both labeled and unlabeled instances in a unified manner. Theoretically, we demonstrate the accuracy of the generated pseudo-labels and guarantee the learning consistency of the proposed method. Comprehensive experiments on several benchmark datasets have validated the superiority of the proposed method.