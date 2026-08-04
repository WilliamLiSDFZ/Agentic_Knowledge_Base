---
title: "Two Fists, One Heart: Multi-Objective Optimization Based Strategy Fusion for Long-tailed Learning"
source: "https://proceedings.mlr.press/v235/zhao24o.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/zhao24o/zhao24o.pdf"
categories: ['learning-with-imperfect-data-and-bias']
tags: ['long-tailed-learning', 'multi-objective-optimization', 'strategy-fusion', 'imbalanced-data']
venue: "ICML 2024"
tldr: "This paper proposes a multi-objective optimization framework to fuse complementary training strategies for long-tailed data distributions."
---

# Two Fists, One Heart: Multi-Objective Optimization Based Strategy Fusion for Long-tailed Learning

**Source**: [https://proceedings.mlr.press/v235/zhao24o.html](https://proceedings.mlr.press/v235/zhao24o.html)

**TLDR**: This paper proposes a multi-objective optimization framework to fuse complementary training strategies for long-tailed data distributions.

## Abstract

Real-world data generally follows a long-tailed distribution, which makes traditional high-performance training strategies unable to show their usual effects. Various insights have been proposed to alleviate this challenging distribution. However, some observations indicate that models trained on long-tailed distributions always show a trade-off between the performance of head and tail classes. For a profound understanding of the trade-off, we first theoretically analyze the trade-off problem in long-tailed learning and creatively transform the trade-off problem in long-tailed learning into a multi-objective optimization (MOO) problem. Motivated by these analyses, we propose the idea of strategy fusion for MOO long-tailed learning and point out the potential conflict problem. We further design a Multi-Objective Optimization based Strategy Fusion (MOOSF), which effectively resolves conflicts, and achieves an efficient fusion of heterogeneous strategies. Comprehensive experiments on mainstream datasets show that even the simplest strategy fusion can outperform complex long-tailed strategies. More importantly, it provides a new perspective for generalized long-tailed learning. The code is available in the accompanying supplementary materials.