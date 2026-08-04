---
title: "Fair Risk Control: A Generalized Framework for Calibrating Multi-group Fairness Risks"
source: "https://proceedings.mlr.press/v235/zhang24be.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/zhang24be/zhang24be.pdf"
categories: ['fairness-aware-algorithmic-decision-making', 'statistical-learning-robustness-uncertainty-quantification']
tags: ['fairness', 'multicalibration', 'risk-control', 'multi-group', 'post-processing']
venue: "ICML 2024"
tldr: "Introduces a generalized multicalibration framework for post-processing ML models to satisfy multi-group fairness risk guarantees."
---

# Fair Risk Control: A Generalized Framework for Calibrating Multi-group Fairness Risks

**Source**: [https://proceedings.mlr.press/v235/zhang24be.html](https://proceedings.mlr.press/v235/zhang24be.html)

**TLDR**: Introduces a generalized multicalibration framework for post-processing ML models to satisfy multi-group fairness risk guarantees.

## Abstract

This paper introduces a framework for post-processing machine learning models so that their predictions satisfy multi-group fairness guarantees. Based on the celebrated notion of multicalibration, we introduce $(s,g,\alpha)-$GMC (Generalized Multi-Dimensional Multicalibration) for multi-dimensional mappings $s$, constraints $g$, and a pre-specified threshold level $\alpha$. We propose associated algorithms to achieve this notion in general settings. This framework is then applied to diverse scenarios encompassing different fairness concerns, including false negative rate control in image segmentation, prediction set conditional uncertainty quantification in hierarchical classification, and de-biased text generation in language models. We conduct numerical studies on several datasets and tasks.