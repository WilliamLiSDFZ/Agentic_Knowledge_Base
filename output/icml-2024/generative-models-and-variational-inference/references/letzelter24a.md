---
title: "Winner-takes-all learners are geometry-aware conditional density estimators"
source: "https://proceedings.mlr.press/v235/letzelter24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/letzelter24a/letzelter24a.pdf"
categories: ['generative-models-and-variational-inference', 'sampling-compression-and-dimensionality-reduction']
tags: ['winner-takes-all', 'Voronoi-tessellation', 'conditional-density-estimation', 'ambiguous-tasks', 'hypothesis-prediction']
venue: "ICML 2024"
tldr: "Shows that winner-takes-all trained models are geometry-aware conditional density estimators linked to centroidal Voronoi tessellations."
---

# Winner-takes-all learners are geometry-aware conditional density estimators

**Source**: [https://proceedings.mlr.press/v235/letzelter24a.html](https://proceedings.mlr.press/v235/letzelter24a.html)

**TLDR**: Shows that winner-takes-all trained models are geometry-aware conditional density estimators linked to centroidal Voronoi tessellations.

## Abstract

Winner-takes-all training is a simple learning paradigm, which handles ambiguous tasks by predicting a set of plausible hypotheses. Recently, a connection was established between Winner-takes-all training and centroidal Voronoi tessellations, showing that, once trained, hypotheses should quantize optimally the shape of the conditional distribution to predict. However, the best use of these hypotheses for uncertainty quantification is still an open question. In this work, we show how to leverage the appealing geometric properties of the Winner-takes-all learners for conditional density estimation, without modifying its original training scheme. We theoretically establish the advantages of our novel estimator both in terms of quantization and density estimation, and we demonstrate its competitiveness on synthetic and real-world datasets, including audio data.