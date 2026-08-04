---
title: "Generalized Preference Optimization: A Unified Approach to Offline Alignment"
source: "https://proceedings.mlr.press/v235/tang24b.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/tang24b/tang24b.pdf"
categories: ['large-language-model-alignment-and-capabilities']
tags: ['preference-optimization', 'offline-alignment', 'unified-framework']
venue: "ICML 2024"
tldr: "Generalized Preference Optimization (GPO) unifies offline alignment losses via a family of convex function parameterizations including DPO and SLiC."
---

# Generalized Preference Optimization: A Unified Approach to Offline Alignment

**Source**: [https://proceedings.mlr.press/v235/tang24b.html](https://proceedings.mlr.press/v235/tang24b.html)

**TLDR**: Generalized Preference Optimization (GPO) unifies offline alignment losses via a family of convex function parameterizations including DPO and SLiC.

## Abstract

Offline preference optimization allows fine-tuning large models directly from offline data, and has proved effective in recent alignment practices. We propose generalized preference optimization (GPO), a family of offline losses parameterized by a general class of convex functions. GPO enables a unified view over preference optimization, encompassing existing algorithms such as DPO, IPO and SLiC as special cases, while naturally introducing new variants. The GPO framework also sheds light on how offline algorithms enforce regularization, through the design of the convex function that defines the loss. Our analysis and experiments reveal the connections and subtle differences between the offline regularization and the KL divergence regularization intended by the canonical RLHF formulation. In a controlled setting akin to Gao et al 2023, we also show that different GPO variants achieve similar trade-offs between regularization and performance, though the optimal values of hyper-parameter might differ as predicted by theory. In all, our results present new algorithmic toolkits and empirical insights to alignment practitioners.