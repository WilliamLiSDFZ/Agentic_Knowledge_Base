---
title: "TIC-TAC: A Framework For Improved Covariance Estimation In Deep Heteroscedastic Regression"
source: "https://proceedings.mlr.press/v235/shukla24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/shukla24a/shukla24a.pdf"
categories: ['statistical-learning-robustness-uncertainty-quantification', 'generative-models-and-variational-inference']
tags: ['heteroscedastic-regression', 'covariance-estimation', 'deep-learning']
venue: "ICML 2024"
tldr: "Proposes TIC-TAC, a framework improving covariance estimation in deep heteroscedastic regression to address sub-optimal convergence."
---

# TIC-TAC: A Framework For Improved Covariance Estimation In Deep Heteroscedastic Regression

**Source**: [https://proceedings.mlr.press/v235/shukla24a.html](https://proceedings.mlr.press/v235/shukla24a.html)

**TLDR**: Proposes TIC-TAC, a framework improving covariance estimation in deep heteroscedastic regression to address sub-optimal convergence.

## Abstract

Deep heteroscedastic regression involves jointly optimizing the mean and covariance of the predicted distribution using the negative log-likelihood. However, recent works show that this may result in sub-optimal convergence due to the challenges associated with covariance estimation. While the literature addresses this by proposing alternate formulations to mitigate the impact of the predicted covariance, we focus on improving the predicted covariance itself. We study two questions: (1) Does the predicted covariance truly capture the randomness of the predicted mean? (2) In the absence of supervision, how can we quantify the accuracy of covariance estimation? We address (1) with a Taylor Induced Covariance (TIC), which captures the randomness of the predicted mean by incorporating its gradient and curvature through the second order Taylor polynomial. Furthermore, we tackle (2) by introducing a Task Agnostic Correlations (TAC) metric, which combines the notion of correlations and absolute error to evaluate the covariance. We evaluate TIC-TAC across multiple experiments spanning synthetic and real-world datasets. Our results show that not only does TIC accurately learn the covariance, it additionally facilitates an improved convergence of the negative log-likelihood. Our code is available at https://github.com/vita-epfl/TIC-TAC