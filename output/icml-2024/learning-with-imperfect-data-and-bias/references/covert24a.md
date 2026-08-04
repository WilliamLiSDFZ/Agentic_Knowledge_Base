---
title: "Scaling Laws for the Value of Individual Data Points in Machine Learning"
source: "https://proceedings.mlr.press/v235/covert24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/covert24a/covert24a.pdf"
categories: ['data-selection-and-active-learning-methods', 'learning-with-imperfect-data-and-bias']
tags: ['scaling-laws', 'data-valuation', 'individual-data-points']
venue: "ICML 2024"
tldr: "Derives scaling laws describing how the value of individual data points changes with dataset size in machine learning models."
---

# Scaling Laws for the Value of Individual Data Points in Machine Learning

**Source**: [https://proceedings.mlr.press/v235/covert24a.html](https://proceedings.mlr.press/v235/covert24a.html)

**TLDR**: Derives scaling laws describing how the value of individual data points changes with dataset size in machine learning models.

## Abstract

Recent works have shown that machine learning models improve at a predictable rate with the amount of training data, leading to scaling laws that describe the relationship between error and dataset size. These scaling laws can help determine a model’s training dataset, but they take an aggregate view of the data by only considering the dataset’s size. We consider a new perspective by investigating scaling behavior for the value of individual data points: we find that a data point’s contribution to model’s performance shrinks predictably with the size of the dataset in a log-linear manner. Interestingly, there is significant variability in the scaling exponent among different data points, indicating that certain points are more valuable in small datasets and other points are relatively more useful as a part of large datasets. We provide learning theory support for our scaling laws and we observe empirically that it holds across several model classes. We further propose a maximum likelihood estimator and an amortized estimator to efficiently learn the individualized scaling behaviors from a small number of noisy observations per data point. Using our efficient estimators, we provide insights into factors that influence the scaling behavior of different data points. Finally we demonstrate applications of the individualized scaling laws to data valuation and data subset selection.