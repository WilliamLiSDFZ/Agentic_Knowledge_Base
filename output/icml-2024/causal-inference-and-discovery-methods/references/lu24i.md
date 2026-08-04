---
title: "CauDiTS: Causal Disentangled Domain Adaptation of Multivariate Time Series"
source: "https://proceedings.mlr.press/v235/lu24i.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/lu24i/lu24i.pdf"
categories: ['causal-inference-and-discovery-methods', 'time-series-modeling-and-forecasting-methods']
tags: ['domain-adaptation', 'causal-disentanglement', 'multivariate-time-series', 'distribution-shift']
venue: "ICML 2024"
tldr: "Proposes causal disentanglement-based domain adaptation for multivariate time series classification across distribution shifts."
---

# CauDiTS: Causal Disentangled Domain Adaptation of Multivariate Time Series

**Source**: [https://proceedings.mlr.press/v235/lu24i.html](https://proceedings.mlr.press/v235/lu24i.html)

**TLDR**: Proposes causal disentanglement-based domain adaptation for multivariate time series classification across distribution shifts.

## Abstract

Unsupervised domain adaptation of multivariate time series aims to train a model to adapt its classification ability from a labeled source domain to an unlabeled target domain, where there are differences in the distribution between domains. Existing methods extract domain-invariant features directly via a shared feature extractor, neglecting the exploration of the underlying causal patterns, which undermines their reliability, especially in complex multivariate dynamic systems. To address this problem, we propose CauDiTS, an innovative framework for unsupervised domain adaptation of multivariate time series. CauDiTS adopts an adaptive rationale disentangler to disentangle domain-common causal rationales and domain-specific correlations from variable interrelationships. The stability of causal rationales across domains is vital for filtering domainspecific perturbations and facilitating the extraction of domain-invariant representations. Moreover, we promote the cross-domain consistency of intra-class causal rationales employing the learning strategies of causal prototype consistency and domain-intervention causality invariance. CauDiTS is evaluated on four benchmark datasets, demonstrating its effectiveness and outperforming state-of-the-art methods.