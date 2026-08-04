---
title: "LeaPformer: Enabling Linear Transformers for Autoregressive and Simultaneous Tasks via Learned Proportions"
source: "https://proceedings.mlr.press/v235/agostinelli-iii24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/agostinelli-iii24a/agostinelli-iii24a.pdf"
categories: ['transformer-architecture-efficiency-and-scaling']
tags: ['linear-transformers', 'autoregressive', 'position-reweighting', 'learned-proportions', 'simultaneous-translation']
venue: "ICML 2024"
tldr: "LeaPformer enables linear transformers for autoregressive and simultaneous tasks via learned position-based re-weighting."
---

# LeaPformer: Enabling Linear Transformers for Autoregressive and Simultaneous Tasks via Learned Proportions

**Source**: [https://proceedings.mlr.press/v235/agostinelli-iii24a.html](https://proceedings.mlr.press/v235/agostinelli-iii24a.html)

**TLDR**: LeaPformer enables linear transformers for autoregressive and simultaneous tasks via learned position-based re-weighting.

## Abstract

A promising approach to preserving model performance in linearized transformers is to employ position-based re-weighting functions. However, state-of-the-art re-weighting functions rely heavily on target sequence lengths, making it difficult or impossible to apply them to autoregressive and simultaneous tasks, where the target and sometimes even the input sequence length are unknown. To address this issue, we propose Learned Proportions (LeaP) and LeaPformers. Our contribution is built on two major components. First, we generalize the dependence on explicit positional representations and sequence lengths into dependence on sequence proportions for re-weighting. Second, we replace static positional representations with dynamic proportions derived via a compact module, enabling more flexible attention concentration patterns. We evaluate LeaPformer against eight representative efficient transformers on the Long-Range Arena benchmark, where we show that LeaPformer achieves the best quality-throughput trade-off, as well as apply LeaPformer to Wikitext-103b autoregressive language modeling and simultaneous speech-to-text translation for two language pairs, achieving competitive results in both tasks.