---
title: "Improving Group Robustness on Spurious Correlation Requires Preciser Group Inference"
source: "https://proceedings.mlr.press/v235/han24g.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/han24g/han24g.pdf"
categories: ['fairness-aware-algorithmic-decision-making', 'learning-with-imperfect-data-and-bias']
tags: ['spurious-correlation', 'group-robustness', 'group-inference']
venue: "ICML 2024"
tldr: "Improving group robustness against spurious correlations requires more precise group inference, reducing reliance on expensive group labels."
---

# Improving Group Robustness on Spurious Correlation Requires Preciser Group Inference

**Source**: [https://proceedings.mlr.press/v235/han24g.html](https://proceedings.mlr.press/v235/han24g.html)

**TLDR**: Improving group robustness against spurious correlations requires more precise group inference, reducing reliance on expensive group labels.

## Abstract

Standard empirical risk minimization (ERM) models may prioritize learning spurious correlations between spurious features and true labels, leading to poor accuracy on groups where these correlations do not hold. Mitigating this issue often requires expensive spurious attribute (group) labels or relies on trained ERM models to infer group labels when group information is unavailable. However, the significant performance gap in worst-group accuracy between using pseudo group labels and using oracle group labels inspires us to consider further improving group robustness through preciser group inference. Therefore, we propose GIC, a novel method that accurately infers group labels, resulting in improved worst-group performance. GIC trains a spurious attribute classifier based on two key properties of spurious correlations: (1) high correlation between spurious attributes and true labels, and (2) variability in this correlation between datasets with different group distributions. Empirical studies on multiple datasets demonstrate the effectiveness of GIC in inferring group labels, and combining GIC with various downstream invariant learning methods improves worst-group accuracy, showcasing its powerful flexibility. Additionally, through analyzing the misclassifications in GIC, we identify an interesting phenomenon called semantic consistency, which may contribute to better decoupling the association between spurious attributes and labels, thereby mitigating spurious correlation. The code for GIC is available at https://github.com/yujinhanml/GIC9.