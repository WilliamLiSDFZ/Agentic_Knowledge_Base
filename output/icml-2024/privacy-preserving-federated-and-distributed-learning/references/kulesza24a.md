---
title: "Mean Estimation in the Add-Remove Model of Differential Privacy"
source: "https://proceedings.mlr.press/v235/kulesza24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/kulesza24a/kulesza24a.pdf"
categories: ['privacy-preserving-federated-and-distributed-learning', 'statistical-learning-robustness-uncertainty-quantification']
tags: ['differential-privacy', 'add-remove-model', 'mean-estimation']
venue: "ICML 2024"
tldr: "Analysis of mean estimation under the add-remove model of differential privacy, contrasting with the more commonly studied swap model."
---

# Mean Estimation in the Add-Remove Model of Differential Privacy

**Source**: [https://proceedings.mlr.press/v235/kulesza24a.html](https://proceedings.mlr.press/v235/kulesza24a.html)

**TLDR**: Analysis of mean estimation under the add-remove model of differential privacy, contrasting with the more commonly studied swap model.

## Abstract

Differential privacy is often studied under two different models of neighboring datasets: the add-remove model and the swap model. While the swap model is frequently used in the academic literature to simplify analysis, many practical applications rely on the more conservative add-remove model, where obtaining tight results can be difficult. Here, we study the problem of one-dimensional mean estimation under the add-remove model. We propose a new algorithm and show that it is min-max optimal, achieving the best possible constant in the leading term of the mean squared error for all $\epsilon$, and that this constant is the same as the optimal algorithm under the swap model. These results show that the add-remove and swap models give nearly identical errors for mean estimation, even though the add-remove model cannot treat the size of the dataset as public information. We also demonstrate empirically that our proposed algorithm yields at least a factor of two improvement in mean squared error over algorithms frequently used in practice. One of our main technical contributions is a new hourglass mechanism, which might be of independent interest in other scenarios.