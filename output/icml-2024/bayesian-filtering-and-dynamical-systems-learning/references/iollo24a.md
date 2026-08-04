---
title: "PASOA- PArticle baSed Bayesian Optimal Adaptive design"
source: "https://proceedings.mlr.press/v235/iollo24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/iollo24a/iollo24a.pdf"
categories: ['bayesian-filtering-and-dynamical-systems-learning', 'bayesian-optimization-and-surrogate-methods']
tags: ['Bayesian-experimental-design', 'particle-filters', 'sequential-design', 'posterior-estimation', 'contrastive-learning']
venue: "ICML 2024"
tldr: "PASOA is a particle-based procedure for Bayesian experimental design that simultaneously optimizes sequential experiments and estimates posterior distributions."
---

# PASOA- PArticle baSed Bayesian Optimal Adaptive design

**Source**: [https://proceedings.mlr.press/v235/iollo24a.html](https://proceedings.mlr.press/v235/iollo24a.html)

**TLDR**: PASOA is a particle-based procedure for Bayesian experimental design that simultaneously optimizes sequential experiments and estimates posterior distributions.

## Abstract

We propose a new procedure named PASOA, for Bayesian experimental design, that performs sequential design optimization by simultaneously providing accurate estimates of successive posterior distributions for parameter inference. The sequential design process is carried out via a contrastive estimation principle, using stochastic optimization and Sequential Monte Carlo (SMC) samplers to maximise the Expected Information Gain (EIG). As larger information gains are obtained for larger distances between successive posterior distributions, this EIG objective may worsen classical SMC performance. To handle this issue, tempering is proposed to have both a large information gain and an accurate SMC sampling, that we show is crucial for performance. This novel combination of stochastic optimization and tempered SMC allows to jointly handle design optimization and parameter inference. We provide a proof that the obtained optimal design estimators benefit from some consistency property. Numerical experiments confirm the potential of the approach, which outperforms other recent existing procedures.