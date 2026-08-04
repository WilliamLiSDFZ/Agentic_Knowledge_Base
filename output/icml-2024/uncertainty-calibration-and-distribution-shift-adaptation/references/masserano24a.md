---
title: "Classification under Nuisance Parameters and Generalized Label Shift in Likelihood-Free Inference"
source: "https://proceedings.mlr.press/v235/masserano24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/masserano24a/masserano24a.pdf"
categories: ['uncertainty-calibration-and-distribution-shift-adaptation']
tags: ['likelihood-free-inference', 'label-shift', 'nuisance-parameters']
venue: "ICML 2024"
tldr: "A classification framework for handling generalized label shift with nuisance parameters in likelihood-free scientific inference."
---

# Classification under Nuisance Parameters and Generalized Label Shift in Likelihood-Free Inference

**Source**: [https://proceedings.mlr.press/v235/masserano24a.html](https://proceedings.mlr.press/v235/masserano24a.html)

**TLDR**: A classification framework for handling generalized label shift with nuisance parameters in likelihood-free scientific inference.

## Abstract

An open scientific challenge is how to classify events with reliable measures of uncertainty, when we have a mechanistic model of the data-generating process but the distribution over both labels and latent nuisance parameters is different between train and target data. We refer to this type of distributional shift as generalized label shift (GLS). Direct classification using observed data $\mathbf{X}$ as covariates leads to biased predictions and invalid uncertainty estimates of labels $Y$. We overcome these biases by proposing a new method for robust uncertainty quantification that casts classification as a hypothesis testing problem under nuisance parameters. The key idea is to estimate the classifier’s receiver operating characteristic (ROC) across the entire nuisance parameter space, which allows us to devise cutoffs that are invariant under GLS. Our method effectively endows a pre-trained classifier with domain adaptation capabilities and returns valid prediction sets while maintaining high power. We demonstrate its performance on two challenging scientific problems in biology and astroparticle physics with data from realistic mechanistic models.