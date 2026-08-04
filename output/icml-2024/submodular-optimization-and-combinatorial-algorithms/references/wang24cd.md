---
title: "Quality-Diversity with Limited Resources"
source: "https://proceedings.mlr.press/v235/wang24cd.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/wang24cd/wang24cd.pdf"
categories: ['bayesian-optimization-and-surrogate-methods', 'submodular-optimization-and-combinatorial-algorithms']
tags: ['quality-diversity', 'evolutionary-algorithms', 'resource-constrained-optimization', 'archive-management']
venue: "ICML 2024"
tldr: "Proposes resource-efficient quality-diversity algorithms that maintain high-quality diverse solution archives under limited computational and memory budgets."
---

# Quality-Diversity with Limited Resources

**Source**: [https://proceedings.mlr.press/v235/wang24cd.html](https://proceedings.mlr.press/v235/wang24cd.html)

**TLDR**: Proposes resource-efficient quality-diversity algorithms that maintain high-quality diverse solution archives under limited computational and memory budgets.

## Abstract

Quality-Diversity (QD) algorithms have emerged as a powerful optimization paradigm with the aim of generating a set of high-quality and diverse solutions. To achieve such a challenging goal, QD algorithms require maintaining a large archive and a large population in each iteration, which brings two main issues, sample and resource efficiency. Most advanced QD algorithms focus on improving the sample efficiency, while the resource efficiency is overlooked to some extent. Particularly, the resource overhead during the training process has not been touched yet, hindering the wider application of QD algorithms. In this paper, we highlight this important research question, i.e., how to efficiently train QD algorithms with limited resources, and propose a novel and effective method called RefQD to address it. RefQD decomposes a neural network into representation and decision parts, and shares the representation part with all decision parts in the archive to reduce the resource overhead. It also employs a series of strategies to address the mismatch issue between the old decision parts and the newly updated representation part. Experiments on different types of tasks from small to large resource consumption demonstrate the excellent performance of RefQD: it not only uses significantly fewer resources (e.g., 16% GPU memories on QDax and 3.7% on Atari) but also achieves comparable or better performance compared to sample-efficient QD algorithms. Our code is available at https://github.com/lamda-bbo/RefQD.