---
title: "Conformal Predictions under Markovian Data"
source: "https://proceedings.mlr.press/v235/zheng24j.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/zheng24j/zheng24j.pdf"
categories: ['statistical-learning-robustness-uncertainty-quantification']
tags: ['conformal-prediction', 'Markovian-data', 'coverage-gap', 'mixing-properties']
venue: "ICML 2024"
tldr: "This paper quantifies the coverage gap of split conformal prediction under Markovian (non-exchangeable) data as a function of the chain's mixing properties."
---

# Conformal Predictions under Markovian Data

**Source**: [https://proceedings.mlr.press/v235/zheng24j.html](https://proceedings.mlr.press/v235/zheng24j.html)

**TLDR**: This paper quantifies the coverage gap of split conformal prediction under Markovian (non-exchangeable) data as a function of the chain's mixing properties.

## Abstract

We study the split Conformal Prediction method when applied to Markovian data. We quantify the gap in terms of coverage induced by the correlations in the data (compared to exchangeable data). This gap strongly depends on the mixing properties of the underlying Markov chain, and we prove that it typically scales as $\sqrt{t_\mathrm{mix}\ln(n)/n}$ (where $t_\mathrm{mix}$ is the mixing time of the chain). We also derive upper bounds on the impact of the correlations on the size of the prediction set. Finally we present $K$-split CP, a method that consists in thinning the calibration dataset and that adapts to the mixing properties of the chain. Its coverage gap is reduced to $t_\mathrm{mix}/(n\ln(n))$ without really affecting the size of the prediction set. We finally test our algorithms on synthetic and real-world datasets.