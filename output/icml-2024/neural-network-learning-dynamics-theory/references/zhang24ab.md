---
title: "Guarantees for Nonlinear Representation Learning: Non-identical Covariates, Dependent Data, Fewer Samples"
source: "https://proceedings.mlr.press/v235/zhang24ab.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/zhang24ab/zhang24ab.pdf"
categories: ['statistical-learning-robustness-uncertainty-quantification', 'neural-network-learning-dynamics-theory']
tags: ['representation-learning', 'non-iid-data', 'dependent-data']
venue: "ICML 2024"
tldr: "Provides theoretical guarantees for nonlinear representation learning under non-identical and statistically dependent multi-source data."
---

# Guarantees for Nonlinear Representation Learning: Non-identical Covariates, Dependent Data, Fewer Samples

**Source**: [https://proceedings.mlr.press/v235/zhang24ab.html](https://proceedings.mlr.press/v235/zhang24ab.html)

**TLDR**: Provides theoretical guarantees for nonlinear representation learning under non-identical and statistically dependent multi-source data.

## Abstract

A driving force behind the diverse applicability of modern machine learning is the ability to extract meaningful features across many sources. However, many practical domains involve data that are non-identically distributed across sources, and possibly statistically dependent within its source, violating vital assumptions in existing theoretical studies of representation learning. Toward addressing these issues, we establish statistical guarantees for learning general nonlinear representations from multiple data sources that admit different input distributions and possibly dependent data. Specifically, we study the sample-complexity of learning $T+1$ functions $f_\star^{(t)} \circ g_\star$ from a function class $\mathcal{F} \times \mathcal{G}$, where $f_\star^{(t)}$ are task specific linear functions and $g_\star$ is a shared non-linear representation. An approximate representation $\hat g$ is estimated using $N$ samples from each of $T$ source tasks, and a fine-tuning function $\hat f^{(0)}$ is fit using $N’$ samples from a target task passed through $\hat g$. Our results show that the excess risk of the estimate $\hat f^{(0)} \circ \hat g$ on the target task decays as $\tilde{\mathcal{O}}\Big(\frac{\mathrm{C}(\mathcal{G})}{N T} + \frac{\text{dim}(\mathcal{F})}{N’}\Big)$, where $\mathrm{C}(\mathcal{G})$ denotes the complexity of $\mathcal{G}$. Notably, our rates match that of the iid setting, while requiring fewer samples per task than prior analysis and admitting no dependence on the mixing time. We support our analysis with numerical experiments performing imitation learning over non-linear dynamical systems.