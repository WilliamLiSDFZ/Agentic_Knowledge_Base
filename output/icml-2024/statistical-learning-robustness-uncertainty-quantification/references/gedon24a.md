---
title: "No Double Descent in Principal Component Regression: A High-Dimensional Analysis"
source: "https://proceedings.mlr.press/v235/gedon24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/gedon24a/gedon24a.pdf"
categories: ['statistical-learning-robustness-uncertainty-quantification', 'sampling-compression-and-dimensionality-reduction']
tags: ['principal-component-regression', 'double-descent', 'high-dimensional-analysis']
venue: "ICML 2024"
tldr: "Shows that principal component regression on low-dimensional manifold data does not exhibit double descent in high dimensions."
---

# No Double Descent in Principal Component Regression: A High-Dimensional Analysis

**Source**: [https://proceedings.mlr.press/v235/gedon24a.html](https://proceedings.mlr.press/v235/gedon24a.html)

**TLDR**: Shows that principal component regression on low-dimensional manifold data does not exhibit double descent in high dimensions.

## Abstract

Understanding the generalization properties of large-scale models necessitates incorporating realistic data assumptions into the analysis. Therefore, we consider Principal Component Regression (PCR)—combining principal component analysis and linear regression—on data from a low-dimensional manifold. We present an analysis of PCR when the data is sampled from a spiked covariance model, obtaining fundamental asymptotic guarantees for the generalization risk of this model. Our analysis is based on random matrix theory and allows us to provide guarantees for high-dimensional data. We additionally present an analysis of the distribution shift between training and test data. The results allow us to disentangle the effects of (1) the number of parameters, (2) the data-generating model and, (3) model misspecification on the generalization risk. The use of PCR effectively regularizes the model and prevents the interpolation peak of the double descent. Our theoretical findings are empirically validated in simulation, demonstrating their practical relevance.