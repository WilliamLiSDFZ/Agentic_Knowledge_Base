---
title: "Beyond Implicit Bias: The Insignificance of SGD Noise in Online Learning"
source: "https://proceedings.mlr.press/v235/vyas24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/vyas24a/vyas24a.pdf"
categories: ['online-learning-and-sequential-decision-making', 'neural-network-learning-dynamics-theory']
tags: ['SGD', 'implicit-bias', 'online-learning', 'single-epoch', 'noise']
venue: "ICML 2024"
tldr: "Demonstrates that SGD noise has negligible impact on online single-epoch learning, challenging the implicit bias narrative established for offline multi-epoch training."
---

# Beyond Implicit Bias: The Insignificance of SGD Noise in Online Learning

**Source**: [https://proceedings.mlr.press/v235/vyas24a.html](https://proceedings.mlr.press/v235/vyas24a.html)

**TLDR**: Demonstrates that SGD noise has negligible impact on online single-epoch learning, challenging the implicit bias narrative established for offline multi-epoch training.

## Abstract

The success of SGD in deep learning has been ascribed by prior works to the implicit bias induced by finite batch sizes (”SGD noise”). While prior works focused on offline learning (i.e., multiple-epoch training), we study the impact of SGD noise on online (i.e., single epoch) learning. Through an extensive empirical analysis of image and language data, we demonstrate that small batch sizes do not confer any implicit bias advantages in online learning. In contrast to offline learning, the benefits of SGD noise in online learning are strictly computational, facilitating more cost-effective gradient steps. This suggests that SGD in the online regime can be construed as taking noisy steps along the ”golden path” of the noiseless gradient descent algorithm. We study this hypothesis and provide supporting evidence in loss and function space. Our findings challenge the prevailing understanding of SGD and offer novel insights into its role in online learning.