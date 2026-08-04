---
title: "Federated Representation Learning in the Under-Parameterized Regime"
source: "https://proceedings.mlr.press/v235/liu24ba.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/liu24ba/liu24ba.pdf"
categories: ['privacy-preserving-federated-and-distributed-learning', 'neural-network-learning-dynamics-theory']
tags: ['federated-learning', 'representation-learning', 'under-parameterized']
venue: "ICML 2024"
tldr: "A theoretical study of federated representation learning in the under-parameterized regime, extending understanding beyond the commonly studied over-parameterized setting."
---

# Federated Representation Learning in the Under-Parameterized Regime

**Source**: [https://proceedings.mlr.press/v235/liu24ba.html](https://proceedings.mlr.press/v235/liu24ba.html)

**TLDR**: A theoretical study of federated representation learning in the under-parameterized regime, extending understanding beyond the commonly studied over-parameterized setting.

## Abstract

Federated representation learning (FRL) is a popular personalized federated learning (FL) framework where clients work together to train a common representation while retaining their personalized heads. Existing studies, however, largely focus on the over-parameterized regime. In this paper, we make the initial efforts to investigate FRL in the under-parameterized regime, where the FL model is insufficient to express the variations in all ground-truth models. We propose a novel FRL algorithm FLUTE, and theoretically characterize its sample complexity and convergence rate for linear models in the under-parameterized regime. To the best of our knowledge, this is the first FRL algorithm with provable performance guarantees in this regime. FLUTE features a data-independent random initialization and a carefully designed objective function that aids the distillation of subspace spanned by the global optimal representation from the misaligned local representations. On the technical side, we bridge low-rank matrix approximation techniques with the FL analysis, which may be of broad interest. We also extend FLUTE beyond linear representations. Experimental results demonstrate that FLUTE outperforms state-of-the-art FRL solutions in both synthetic and real-world tasks.