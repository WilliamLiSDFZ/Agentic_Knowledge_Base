---
title: "Conformalized Survival Distributions: A Generic Post-Process to Increase Calibration"
source: "https://proceedings.mlr.press/v235/qi24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/qi24a/qi24a.pdf"
categories: ['statistical-learning-robustness-uncertainty-quantification', 'uncertainty-calibration-and-distribution-shift-adaptation']
tags: ['survival-analysis', 'calibration', 'conformal-prediction']
venue: "ICML 2024"
tldr: "A conformal post-processing method to improve calibration of survival analysis models without sacrificing discrimination."
---

# Conformalized Survival Distributions: A Generic Post-Process to Increase Calibration

**Source**: [https://proceedings.mlr.press/v235/qi24a.html](https://proceedings.mlr.press/v235/qi24a.html)

**TLDR**: A conformal post-processing method to improve calibration of survival analysis models without sacrificing discrimination.

## Abstract

Discrimination and calibration represent two important properties of survival analysis, with the former assessing the model’s ability to accurately rank subjects and the latter evaluating the alignment of predicted outcomes with actual events. With their distinct nature, it is hard for survival models to simultaneously optimize both of them especially as many previous results found improving calibration tends to diminish discrimination performance. This paper introduces a novel approach utilizing conformal regression that can improve a model’s calibration without degrading discrimination. We provide theoretical guarantees for the above claim, and rigorously validate the efficiency of our approach across 11 real-world datasets, showcasing its practical applicability and robustness in diverse scenarios.