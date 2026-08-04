---
title: "Conformalized Adaptive Forecasting of Heterogeneous Trajectories"
source: "https://proceedings.mlr.press/v235/zhou24l.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/zhou24l/zhou24l.pdf"
categories: ['uncertainty-calibration-and-distribution-shift-adaptation', 'time-series-modeling-and-forecasting-methods']
tags: ['conformal-prediction', 'trajectory-forecasting', 'uncertainty-quantification']
venue: "ICML 2024"
tldr: "Presents a conformal prediction method for generating simultaneous forecasting bands with coverage guarantees over entire random trajectory paths."
---

# Conformalized Adaptive Forecasting of Heterogeneous Trajectories

**Source**: [https://proceedings.mlr.press/v235/zhou24l.html](https://proceedings.mlr.press/v235/zhou24l.html)

**TLDR**: Presents a conformal prediction method for generating simultaneous forecasting bands with coverage guarantees over entire random trajectory paths.

## Abstract

This paper presents a new conformal method for generating simultaneous forecasting bands guaranteed to cover the entire path of a new random trajectory with sufficiently high probability. Prompted by the need for dependable uncertainty estimates in motion planning applications where the behavior of diverse objects may be more or less unpredictable, we blend different techniques from online conformal prediction of single and multiple time series, as well as ideas for addressing heteroscedasticity in regression. This solution is both principled, providing precise finite-sample guarantees, and effective, often leading to more informative predictions than prior methods.