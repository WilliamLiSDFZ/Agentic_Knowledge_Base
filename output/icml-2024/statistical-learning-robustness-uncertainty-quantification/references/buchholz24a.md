---
title: "Robustness of Nonlinear Representation Learning"
source: "https://proceedings.mlr.press/v235/buchholz24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/buchholz24a/buchholz24a.pdf"
categories: ['statistical-learning-robustness-uncertainty-quantification', 'learning-with-imperfect-data-and-bias']
tags: ['representation-learning', 'robustness', 'misspecification', 'nonlinear-ICA']
venue: "ICML 2024"
tldr: "Formalizes robustness of nonlinear representation learning under slightly misspecified settings using local isometry assumptions."
---

# Robustness of Nonlinear Representation Learning

**Source**: [https://proceedings.mlr.press/v235/buchholz24a.html](https://proceedings.mlr.press/v235/buchholz24a.html)

**TLDR**: Formalizes robustness of nonlinear representation learning under slightly misspecified settings using local isometry assumptions.

## Abstract

We study the problem of unsupervised representation learning in slightly misspecified settings, and thus formalize the study of robustness of nonlinear representation learning. We focus on the case where the mixing is close to a local isometry in a suitable distance and show based on existing rigidity results that the mixing can be identified up to linear transformations and small errors. In a second step, we investigate Independent Component Analysis (ICA) with observations generated according to $x=f(s)=As+h(s)$ where $A$ is an invertible mixing matrix and $h$ a small perturbation. We show that we can approximately recover the matrix $A$ and the independent components. Together, these two results show approximate identifiability of nonlinear ICA with almost isometric mixing functions. Those results are a step towards identifiability results for unsupervised representation learning for real-world data that do not follow restrictive model classes.