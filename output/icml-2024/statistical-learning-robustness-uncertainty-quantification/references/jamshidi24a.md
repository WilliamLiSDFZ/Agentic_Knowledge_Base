---
title: "On the sample complexity of conditional independence testing with Von Mises estimator with application to causal discovery"
source: "https://proceedings.mlr.press/v235/jamshidi24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/jamshidi24a/jamshidi24a.pdf"
categories: ['causal-inference-and-discovery-methods', 'statistical-learning-robustness-uncertainty-quantification']
tags: ['conditional-independence-testing', 'causal-discovery', 'Von-Mises-estimator', 'kernel-density-estimation', 'sample-complexity']
venue: "ICML 2024"
tldr: "This paper establishes sample complexity bounds for a nonparametric Von Mises entropy estimator applied to conditional independence testing in causal discovery."
---

# On the sample complexity of conditional independence testing with Von Mises estimator with application to causal discovery

**Source**: [https://proceedings.mlr.press/v235/jamshidi24a.html](https://proceedings.mlr.press/v235/jamshidi24a.html)

**TLDR**: This paper establishes sample complexity bounds for a nonparametric Von Mises entropy estimator applied to conditional independence testing in causal discovery.

## Abstract

Motivated by conditional independence testing, an essential step in constraint-based causal discovery algorithms, we study the nonparametric Von Mises estimator for the entropy of multivariate distributions built on a kernel density estimator. We establish an exponential concentration inequality for this estimator. We design a test for conditional independence (CI) based on our estimator, called VM-CI, which achieves optimal parametric rates under smoothness assumptions. Leveraging the exponential concentration, we prove a tight upper bound for the overall error of VM-CI. This, in turn, allows us to characterize the sample complexity of any constraint-based causal discovery algorithm that uses VM-CI for CI tests. To the best of our knowledge, this is the first sample complexity guarantee for causal discovery for non-linear models and non-Gaussian continuous variables. Furthermore, we empirically show that VM-CI outperforms other popular CI tests in terms of either time, sample complexity, or both. This enhancement significantly improves the performance in structure learning as well.