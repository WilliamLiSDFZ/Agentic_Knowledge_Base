---
title: "On the Minimal Degree Bias in Generalization on the Unseen for non-Boolean Functions"
source: "https://proceedings.mlr.press/v235/pushkin24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/pushkin24a/pushkin24a.pdf"
categories: ['neural-network-learning-dynamics-theory', 'transformer-architecture-efficiency-and-scaling']
tags: ['generalization', 'random-features', 'transformers']
venue: "ICML 2024"
tldr: "Analyzes out-of-domain generalization of random feature models and transformers, proving a minimal degree bias in unseen-domain settings."
---

# On the Minimal Degree Bias in Generalization on the Unseen for non-Boolean Functions

**Source**: [https://proceedings.mlr.press/v235/pushkin24a.html](https://proceedings.mlr.press/v235/pushkin24a.html)

**TLDR**: Analyzes out-of-domain generalization of random feature models and transformers, proving a minimal degree bias in unseen-domain settings.

## Abstract

We investigate the out-of-domain generalization of random feature (RF) models and Transformers. We first prove that in the ‘generalization on the unseen (GOTU)’ setting, where training data is fully seen in some part of the domain but testing is made on another part, and for RF models in the small feature regime, the convergence takes place to interpolators of minimal degree as in the Boolean case (Abbe et al., 2023). We then consider the sparse target regime and explain how this regime relates to the small feature regime, but with a different regularization term that can alter the picture in the non-Boolean case. We show two different outcomes for the sparse regime with q-ary data tokens: (1) if the data is embedded with roots of unities, then a min-degree interpolator is learned like in the Boolean case for RF models, (2) if the data is not embedded as such, e.g., simply as integers, then RF models and Transformers may not learn minimal degree interpolators. This shows that the Boolean setting and its roots of unities generalization are special cases where the minimal degree interpolator offers a rare characterization of how learning takes place. For more general integer and real-valued settings, a more nuanced picture remains to be fully characterized.