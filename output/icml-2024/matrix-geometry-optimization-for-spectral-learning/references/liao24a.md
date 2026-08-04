---
title: "On the Error-Propagation of Inexact Hotelling’s Deflation for Principal Component Analysis"
source: "https://proceedings.mlr.press/v235/liao24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/liao24a/liao24a.pdf"
categories: ['matrix-geometry-optimization-for-spectral-learning']
tags: ['PCA', 'deflation', 'error-propagation']
venue: "ICML 2024"
tldr: "This paper analyzes error propagation in inexact Hotelling's deflation for sequential principal component analysis."
---

# On the Error-Propagation of Inexact Hotelling’s Deflation for Principal Component Analysis

**Source**: [https://proceedings.mlr.press/v235/liao24a.html](https://proceedings.mlr.press/v235/liao24a.html)

**TLDR**: This paper analyzes error propagation in inexact Hotelling's deflation for sequential principal component analysis.

## Abstract

Principal Component Analysis (PCA) aims to find subspaces spanned by the so-called principal components that best represent the variance in the dataset. The deflation method is a popular meta-algorithm that sequentially finds individual principal components, starting from the most important ones and working towards the less important ones. However, as deflation proceeds, numerical errors from the imprecise estimation of principal components propagate due to its sequential nature. This paper mathematically characterizes the error propagation of the inexact Hotelling’s deflation method. We consider two scenarios: $i)$ when the sub-routine for finding the leading eigenvector is abstract and can represent various algorithms; and $ii)$ when power iteration is used as the sub-routine. In the latter case, the additional directional information from power iteration allows us to obtain a tighter error bound than the sub-routine agnostic case. For both scenarios, we explicitly characterize how the errors progress and affect subsequent principal component estimations.