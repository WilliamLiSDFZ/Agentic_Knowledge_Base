---
title: "IW-GAE: Importance weighted group accuracy estimation for improved calibration and model selection in unsupervised domain adaptation"
source: "https://proceedings.mlr.press/v235/joo24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/joo24a/joo24a.pdf"
categories: ['test-time-adaptation-methods-and-evaluation', 'uncertainty-calibration-and-distribution-shift-adaptation']
tags: ['domain-adaptation', 'calibration', 'model-selection', 'importance-weighting']
venue: "ICML 2024"
tldr: "Introduces importance-weighted group accuracy estimation to improve calibration and model selection under unsupervised domain adaptation."
---

# IW-GAE: Importance weighted group accuracy estimation for improved calibration and model selection in unsupervised domain adaptation

**Source**: [https://proceedings.mlr.press/v235/joo24a.html](https://proceedings.mlr.press/v235/joo24a.html)

**TLDR**: Introduces importance-weighted group accuracy estimation to improve calibration and model selection under unsupervised domain adaptation.

## Abstract

Distribution shifts pose significant challenges for model calibration and model selection tasks in the unsupervised domain adaptation problem—a scenario where the goal is to perform well in a distribution shifted domain without labels. In this work, we tackle difficulties coming from distribution shifts by developing a novel importance weighted group accuracy estimator. Specifically, we present a new perspective of addressing the model calibration and model selection tasks by estimating the group accuracy. Then, we formulate an optimization problem for finding an importance weight that leads to an accurate group accuracy estimation with theoretical analyses. Our extensive experiments show that our approach improves state-of-the-art performances by 22% in the model calibration task and 14% in the model selection task.