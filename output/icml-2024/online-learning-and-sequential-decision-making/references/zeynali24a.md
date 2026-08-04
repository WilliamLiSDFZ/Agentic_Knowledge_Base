---
title: "Robust Learning-Augmented Dictionaries"
source: "https://proceedings.mlr.press/v235/zeynali24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/zeynali24a/zeynali24a.pdf"
categories: ['online-learning-and-sequential-decision-making', 'dynamic-algorithms-and-complexity-theory']
tags: ['learning-augmented', 'skip-list', 'dictionary']
venue: "ICML 2024"
tldr: "The first learning-augmented skip list data structure for dictionaries with provably optimal consistency and robustness guarantees."
---

# Robust Learning-Augmented Dictionaries

**Source**: [https://proceedings.mlr.press/v235/zeynali24a.html](https://proceedings.mlr.press/v235/zeynali24a.html)

**TLDR**: The first learning-augmented skip list data structure for dictionaries with provably optimal consistency and robustness guarantees.

## Abstract

We present the first learning-augmented data structure for implementing dictionaries with optimal consistency and robustness. Our data structure, named RobustSL, is a Skip list augmented by predictions of access frequencies of elements in a data sequence. With proper predictions, RobustSL has optimal consistency (achieves static optimality). At the same time, it maintains a logarithmic running time for each operation, ensuring optimal robustness, even if predictions are generated adversarially. Therefore, RobustSL has all the advantages of the recent learning-augmented data structures of Lin, Luo, and Woodruff (ICML 2022) and Cao et al. (arXiv 2023), while providing robustness guarantees that are absent in the previous work. Numerical experiments show that RobustSL outperforms alternative data structures using both synthetic and real datasets.