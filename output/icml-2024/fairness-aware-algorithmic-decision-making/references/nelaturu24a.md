---
title: "On The Fairness Impacts of Hardware Selection in Machine Learning"
source: "https://proceedings.mlr.press/v235/nelaturu24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/nelaturu24a/nelaturu24a.pdf"
categories: ['fairness-aware-algorithmic-decision-making']
tags: ['hardware-fairness', 'ml-as-a-service', 'model-deployment']
venue: "ICML 2024"
tldr: "Hardware selection in ML deployment is shown to have significant and underexplored fairness impacts on model predictions across demographic groups."
---

# On The Fairness Impacts of Hardware Selection in Machine Learning

**Source**: [https://proceedings.mlr.press/v235/nelaturu24a.html](https://proceedings.mlr.press/v235/nelaturu24a.html)

**TLDR**: Hardware selection in ML deployment is shown to have significant and underexplored fairness impacts on model predictions across demographic groups.

## Abstract

In the machine learning ecosystem, hardware selection is often regarded as a mere utility, overshadowed by the spotlight on algorithms and data. This is especially relevant in contexts like ML-as-a-service platforms, where users often lack control over the hardware used for model deployment. This paper investigates the influence of hardware on the delicate balance between model performance and fairness. We demonstrate that hardware choices can exacerbate existing disparities, attributing these discrepancies to variations in gradient flows and loss surfaces across different demographic groups. Through both theoretical and empirical analysis, the paper not only identifies the underlying factors but also proposes an effective strategy for mitigating hardware-induced performance imbalances.