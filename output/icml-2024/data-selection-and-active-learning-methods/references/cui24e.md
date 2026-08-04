---
title: "Ameliorate Spurious Correlations in Dataset Condensation"
source: "https://proceedings.mlr.press/v235/cui24e.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/cui24e/cui24e.pdf"
categories: ['learning-with-imperfect-data-and-bias', 'data-selection-and-active-learning-methods']
tags: ['dataset-condensation', 'spurious-correlations', 'bias']
venue: "ICML 2024"
tldr: "Investigates the impact of dataset bias on dataset condensation and proposes methods to ameliorate spurious correlations in condensed datasets."
---

# Ameliorate Spurious Correlations in Dataset Condensation

**Source**: [https://proceedings.mlr.press/v235/cui24e.html](https://proceedings.mlr.press/v235/cui24e.html)

**TLDR**: Investigates the impact of dataset bias on dataset condensation and proposes methods to ameliorate spurious correlations in condensed datasets.

## Abstract

Dataset Condensation has emerged as a technique for compressing large datasets into smaller synthetic counterparts, facilitating downstream training tasks. In this paper, we study the impact of bias inside the original dataset on the performance of dataset condensation. With a comprehensive empirical evaluation on canonical datasets with color, corruption and background biases, we found that color and background biases in the original dataset will be amplified through the condensation process, resulting in a notable decline in the performance of models trained on the condensed dataset, while corruption bias is suppressed through the condensation process. To reduce bias amplification in dataset condensation, we introduce a simple yet highly effective approach based on a sample reweighting scheme utilizing kernel density estimation. Empirical results on multiple real-world and synthetic datasets demonstrate the effectiveness of the proposed method. Notably, on CMNIST with 5% bias-conflict ratio and IPC 50, our method achieves 91.5% test accuracy compared to 23.8% from vanilla DM, boosting the performance by 67.7%, whereas applying state-of-the-art debiasing method on the same dataset only achieves 53.7% accuracy. Our findings highlight the importance of addressing biases in dataset condensation and provide a promising avenue to address bias amplification in the process.