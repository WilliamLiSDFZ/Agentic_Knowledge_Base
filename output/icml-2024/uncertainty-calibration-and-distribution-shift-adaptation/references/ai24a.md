---
title: "Not all distributional shifts are equal: Fine-grained robust conformal inference"
source: "https://proceedings.mlr.press/v235/ai24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/ai24a/ai24a.pdf"
categories: ['uncertainty-calibration-and-distribution-shift-adaptation']
tags: ['conformal-inference', 'distributional-shift', 'covariate-shift', 'conditional-shift', 'uncertainty-quantification']
venue: "ICML 2024"
tldr: "Introduces a fine-grained conformal inference framework that separately handles covariate and conditional distribution shifts."
---

# Not all distributional shifts are equal: Fine-grained robust conformal inference

**Source**: [https://proceedings.mlr.press/v235/ai24a.html](https://proceedings.mlr.press/v235/ai24a.html)

**TLDR**: Introduces a fine-grained conformal inference framework that separately handles covariate and conditional distribution shifts.

## Abstract

We introduce a fine-grained framework for uncertainty quantification of predictive models under distributional shifts. This framework distinguishes the shift in covariate distributions from that in the conditional relationship between the outcome ($Y$) and the covariates ($X$). We propose to reweight the training samples to adjust for an identifiable shift in covariate distribution while protecting against the worst-case conditional distribution shift bounded in an $f$-divergence ball. Based on ideas from conformal inference and distributionally robust learning, we present an algorithm that outputs (approximately) valid and efficient prediction intervals in the presence of distributional shifts. As a use case, we apply the framework to sensitivity analysis of individual treatment effects with hidden confounding. The proposed methods are evaluated in simulations and four real data applications, demonstrating superior robustness and efficiency compared with existing benchmarks.