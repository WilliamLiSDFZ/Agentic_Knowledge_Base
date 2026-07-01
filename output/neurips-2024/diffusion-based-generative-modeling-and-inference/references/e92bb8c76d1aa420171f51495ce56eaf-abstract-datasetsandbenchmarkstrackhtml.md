---
title: "TSGM: A Flexible Framework for Generative Modeling of Synthetic Time Series"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/e92bb8c76d1aa420171f51495ce56eaf-Abstract-Datasets_and_Benchmarks_Track.html"
categories: ['time-series-forecasting-and-analysis', 'diffusion-based-generative-modeling-and-inference']
tags: ['synthetic-time-series', 'generative-modeling', 'framework']
venue: "NeurIPS 2024"
tldr: "TSGM is a flexible framework for generating synthetic time series data to address data scarcity and privacy concerns."
---

# TSGM: A Flexible Framework for Generative Modeling of Synthetic Time Series

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/e92bb8c76d1aa420171f51495ce56eaf-Abstract-Datasets_and_Benchmarks_Track.html](https://papers.nips.cc/paper_files/paper/2024/hash/e92bb8c76d1aa420171f51495ce56eaf-Abstract-Datasets_and_Benchmarks_Track.html)

**TLDR**: TSGM is a flexible framework for generating synthetic time series data to address data scarcity and privacy concerns.

## Abstract

Time series data are essential in a wide range of machine learning (ML) applications. However, temporal data are often scarce or highly sensitive, limiting data sharing and the use of data-intensive ML methods. A possible solution to this problem is the generation of synthetic datasets that resemble real data. In this work, we introduce Time Series Generative Modeling (TSGM), an open-source framework for the generative modeling and evaluation of synthetic time series datasets. TSGM includes a broad repertoire of machine learning methods: generative models, probabilistic, simulation-based approaches, and augmentation techniques. The framework enables users to evaluate the quality of the produced data from different angles: similarity, downstream effectiveness, predictive consistency, diversity, fairness, and privacy. TSGM is extensible and user-friendly, which allows researchers to rapidly implement their own methods and compare them in a shareable environment. The framework has been tested on open datasets and in production and proved to be beneficial in both cases. https://github.com/AlexanderVNikitin/tsgm