---
title: "Causal Representation Learning Made Identifiable by Grouping of Observational Variables"
source: "https://proceedings.mlr.press/v235/morioka24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/morioka24a/morioka24a.pdf"
categories: ['causal-inference-and-discovery-methods', 'generative-models-and-variational-inference']
tags: ['causal-representation-learning', 'identifiability', 'observational-grouping', 'latent-causal-models']
venue: "ICML 2024"
tldr: "Grouping of observed variables is shown to provide sufficient structure for identifiable causal representation learning without additional supervision."
---

# Causal Representation Learning Made Identifiable by Grouping of Observational Variables

**Source**: [https://proceedings.mlr.press/v235/morioka24a.html](https://proceedings.mlr.press/v235/morioka24a.html)

**TLDR**: Grouping of observed variables is shown to provide sufficient structure for identifiable causal representation learning without additional supervision.

## Abstract

A topic of great current interest is Causal Representation Learning (CRL), whose goal is to learn a causal model for hidden features in a data-driven manner. Unfortunately, CRL is severely ill-posed since it is a combination of the two notoriously ill-posed problems of representation learning and causal discovery. Yet, finding practical identifiability conditions that guarantee a unique solution is crucial for its practical applicability. Most approaches so far have been based on assumptions on the latent causal mechanisms, such as temporal causality, or existence of supervision or interventions; these can be too restrictive in actual applications. Here, we show identifiability based on novel, weak constraints, which requires no temporal structure, intervention, nor weak supervision. The approach is based on assuming the observational mixing exhibits a suitable grouping of the observational variables. We also propose a novel self-supervised estimation framework consistent with the model, prove its statistical consistency, and experimentally show its superior CRL performances compared to the state-of-the-art baselines. We further demonstrate its robustness against latent confounders and causal cycles.