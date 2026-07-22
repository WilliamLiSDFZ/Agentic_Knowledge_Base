---
title: "Hierarchy-aware Biased Bound Margin Loss Function for Hierarchical Text Classification"
source: "https://aclanthology.org/2024.findings-acl.457/"
pdf_url: ""
categories: ['hierarchical-text-classification-methods']
tags: ['hierarchical-text-classification', 'label-imbalance', 'margin-loss']
venue: "ACL 2024"
tldr: "Proposes a hierarchy-aware biased bound margin loss to address structural information use and label imbalance in hierarchical text classification."
---

# Hierarchy-aware Biased Bound Margin Loss Function for Hierarchical Text Classification

**Source**: [https://aclanthology.org/2024.findings-acl.457/](https://aclanthology.org/2024.findings-acl.457/)

**TLDR**: Proposes a hierarchy-aware biased bound margin loss to address structural information use and label imbalance in hierarchical text classification.

## Abstract

AbstractHierarchical text classification (HTC) is a challenging problem with two key issues: utilizing structural information and mitigating label imbalance. Recently, the unit-based approach generating unit-based feature representations has outperformed the global approach focusing on a global feature representation. Nevertheless, unit-based models using BCE and ZLPR losses still face static thresholding and label imbalance challenges. Those challenges become more critical in large-scale hierarchies. This paper introduces a novel hierarchy-aware loss function for unit-based HTC models: Hierarchy-aware Biased Bound Margin (HBM) loss. HBM integrates learnable bounds, biases, and a margin to address static thresholding and mitigate label imbalance adaptively. Experimental results on benchmark datasets demonstrate the superior performance of HBM compared to competitive HTC models.