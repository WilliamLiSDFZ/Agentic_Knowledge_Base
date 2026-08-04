---
title: "Conformal Prediction with Learned Features"
source: "https://proceedings.mlr.press/v235/kiyani24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/kiyani24a/kiyani24a.pdf"
categories: ['statistical-learning-robustness-uncertainty-quantification', 'uncertainty-calibration-and-distribution-shift-adaptation']
tags: ['conformal-prediction', 'conditional-coverage', 'learned-features', 'distribution-shift']
venue: "ICML 2024"
tldr: "A method for conformal prediction that learns features to achieve improved conditional coverage guarantees beyond existing relaxations."
---

# Conformal Prediction with Learned Features

**Source**: [https://proceedings.mlr.press/v235/kiyani24a.html](https://proceedings.mlr.press/v235/kiyani24a.html)

**TLDR**: A method for conformal prediction that learns features to achieve improved conditional coverage guarantees beyond existing relaxations.

## Abstract

In this paper, we focus on the problem of conformal prediction with conditional guarantees. Prior work has shown that it is impossible to construct nontrivial prediction sets with full conditional coverage guarantees. A wealth of research has considered relaxations of full conditional guarantees, relying on some predefined uncertainty structures. Departing from this line of thinking, we propose Partition Learning Conformal Prediction (PLCP), a framework to improve conditional validity of prediction sets through learning uncertainty-guided features from the calibration data. We implement PLCP efficiently with alternating gradient descent, utilizing off-the-shelf machine learning models. We further analyze PLCP theoretically and provide conditional guarantees for infinite and finite sample sizes. Finally, our experimental results over four real-world and synthetic datasets show the superior performance of PLCP compared to state-of-the-art methods in terms of coverage and length in both classification and regression scenarios.