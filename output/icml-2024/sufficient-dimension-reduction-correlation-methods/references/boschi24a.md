---
title: "A New Computationally Efficient Algorithm to solve Feature Selection for Functional Data Classification in High-dimensional Spaces"
source: "https://proceedings.mlr.press/v235/boschi24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/boschi24a/boschi24a.pdf"
categories: ['data-selection-and-active-learning-methods', 'sufficient-dimension-reduction-correlation-methods']
tags: ['feature-selection', 'functional-data', 'classification', 'high-dimensional']
venue: "ICML 2024"
tldr: "This paper proposes FSFC, a computationally efficient algorithm for joint feature selection and classification of multivariate functional data in high-dimensional spaces."
---

# A New Computationally Efficient Algorithm to solve Feature Selection for Functional Data Classification in High-dimensional Spaces

**Source**: [https://proceedings.mlr.press/v235/boschi24a.html](https://proceedings.mlr.press/v235/boschi24a.html)

**TLDR**: This paper proposes FSFC, a computationally efficient algorithm for joint feature selection and classification of multivariate functional data in high-dimensional spaces.

## Abstract

This paper introduces a novel methodology for Feature Selection for Functional Classification, FSFC, that addresses the challenge of jointly performing feature selection and classification of functional data in scenarios with categorical responses and multivariate longitudinal features. FSFC tackles a newly defined optimization problem that integrates logistic loss and functional features to identify the most crucial variables for classification. To address the minimization procedure, we employ functional principal components and develop a new adaptive version of the Dual Augmented Lagrangian algorithm. The computational efficiency of FSFC enables handling high-dimensional scenarios where the number of features may considerably exceed the number of statistical units. Simulation experiments demonstrate that FSFC outperforms other machine learning and deep learning methods in computational time and classification accuracy. Furthermore, the FSFC feature selection capability can be leveraged to significantly reduce the problem’s dimensionality and enhance the performances of other classification algorithms. The efficacy of FSFC is also demonstrated through a real data application, analyzing relationships between four chronic diseases and other health and demographic factors. FSFC source code is publicly available at https://github.com/IBM/funGCN.