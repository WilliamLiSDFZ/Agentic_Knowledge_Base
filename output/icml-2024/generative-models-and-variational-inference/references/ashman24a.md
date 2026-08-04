---
title: "Translation Equivariant Transformer Neural Processes"
source: "https://proceedings.mlr.press/v235/ashman24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/ashman24a/ashman24a.pdf"
categories: ['equivariant-neural-networks-and-symmetry-learning', 'generative-models-and-variational-inference']
tags: ['neural-processes', 'translation-equivariance', 'transformers', 'posterior-prediction', 'meta-learning']
venue: "ICML 2024"
tldr: "Introduces translation equivariant transformer neural processes that improve posterior predictive modeling via architectural symmetry constraints."
---

# Translation Equivariant Transformer Neural Processes

**Source**: [https://proceedings.mlr.press/v235/ashman24a.html](https://proceedings.mlr.press/v235/ashman24a.html)

**TLDR**: Introduces translation equivariant transformer neural processes that improve posterior predictive modeling via architectural symmetry constraints.

## Abstract

The effectiveness of neural processes (NPs) in modelling posterior prediction maps—the mapping from data to posterior predictive distributions—has significantly improved since their inception. This improvement can be attributed to two principal factors: (1) advancements in the architecture of permutation invariant set functions, which are intrinsic to all NPs; and (2) leveraging symmetries present in the true posterior predictive map, which are problem dependent. Transformers are a notable development in permutation invariant set functions, and their utility within NPs has been demonstrated through the family of models we refer to as TNPs. Despite significant interest in TNPs, little attention has been given to incorporating symmetries. Notably, the posterior prediction maps for data that are stationary—a common assumption in spatio-temporal modelling—exhibit translation equivariance. In this paper, we introduce of a new family of translation equivariant TNPs that incorporate translation equivariance. Through an extensive range of experiments on synthetic and real-world spatio-temporal data, we demonstrate the effectiveness of TE-TNPs relative to their non-translation-equivariant counterparts and other NP baselines.