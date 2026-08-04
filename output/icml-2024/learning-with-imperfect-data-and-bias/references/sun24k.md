---
title: "Regression Learning with Limited Observations of Multivariate Outcomes and Features"
source: "https://proceedings.mlr.press/v235/sun24k.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/sun24k/sun24k.pdf"
categories: ['learning-with-imperfect-data-and-bias', 'sufficient-dimension-reduction-correlation-methods']
tags: ['multivariate-regression', 'missing-data', 'limited-observations', 'linear-models', 'statistical-learning']
venue: "ICML 2024"
tldr: "A regression learning framework is developed for multivariate linear models when only limited and incomplete observations of outcomes and features are available."
---

# Regression Learning with Limited Observations of Multivariate Outcomes and Features

**Source**: [https://proceedings.mlr.press/v235/sun24k.html](https://proceedings.mlr.press/v235/sun24k.html)

**TLDR**: A regression learning framework is developed for multivariate linear models when only limited and incomplete observations of outcomes and features are available.

## Abstract

Multivariate linear regression models are broadly used to facilitate relationships between outcomes and features. However, their effectiveness is compromised by the presence of missing observations, a ubiquitous challenge in real-world applications. Considering a scenario where learners access only limited components for both outcomes and features, we develop efficient algorithms tailored for the least squares ($L_2$) and least absolute ($L_1$) loss functions, each coupled with a ridge-like and Lasso-type penalty, respectively. Moreover, we establish rigorous error bounds for all proposed algorithms. Notably, our $L_2$ loss function algorithms are probably approximately correct (PAC), distinguishing them from their $L_1$ counterparts. Extensive numerical experiments show that our approach outperforms methods that apply existing algorithms for univariate outcome individually to each coordinate of multivariate outcomes in a naive manner. Further, utilizing the $L_1$ loss function or introducing a Lasso-type penalty can enhance predictions in the presence of outliers or high dimensional features. This research contributes valuable insights into addressing the challenges posed by incomplete data.