---
title: "Does Label Smoothing Help Deep Partial Label Learning?"
source: "https://proceedings.mlr.press/v235/gong24b.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/gong24b/gong24b.pdf"
categories: ['learning-with-imperfect-data-and-bias', 'neural-network-learning-dynamics-theory']
tags: ['partial-label-learning', 'label-smoothing', 'noisy-labels']
venue: "ICML 2024"
tldr: "This paper theoretically and empirically investigates whether label smoothing can mitigate the negative effects of false-positive labels in deep partial label learning."
---

# Does Label Smoothing Help Deep Partial Label Learning?

**Source**: [https://proceedings.mlr.press/v235/gong24b.html](https://proceedings.mlr.press/v235/gong24b.html)

**TLDR**: This paper theoretically and empirically investigates whether label smoothing can mitigate the negative effects of false-positive labels in deep partial label learning.

## Abstract

Although deep partial label learning (deep PLL) classifiers have shown their competitive performance, they are heavily influenced by the noisy false-positive labels leading to poorer performance as the training progresses. Meanwhile, existing deep PLL research lacks theoretical guarantee on the analysis of correlation between label noise (or ambiguity degree) and classification performance. This paper addresses the above limitations with label smoothing (LS) from both theoretical and empirical aspects. In theory, we prove lower and upper bounds of the expected risk to show that label smoothing can help deep PLL. We further derive the optimal smoothing rate to investigate the conditions, i.e., when label smoothing benefits deep PLL. In practice, we design a benchmark solution and a novel optimization algorithm called Label Smoothing-based Partial Label Learning (LS-PLL). Extensive experimental results on benchmark PLL datasets and various deep architectures validate that label smoothing does help deep PLL in improving classification performance and learning distinguishable representations, and the best results can be achieved when the empirical smoothing rate approximately approaches the optimal smoothing rate in theoretical findings. Code is publicly available at https://github.com/kalpiree/LS-PLL.