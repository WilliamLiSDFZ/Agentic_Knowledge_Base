---
title: "On the Calibration of Human Pose Estimation"
source: "https://proceedings.mlr.press/v235/gu24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/gu24a/gu24a.pdf"
categories: ['statistical-learning-robustness-uncertainty-quantification', 'uncertainty-calibration-and-distribution-shift-adaptation']
tags: ['pose-estimation', 'calibration', 'confidence-estimation']
venue: "ICML 2024"
tldr: "This work reveals miscalibration in human pose estimation confidence scores and proposes principled calibration methods to align confidence with accuracy."
---

# On the Calibration of Human Pose Estimation

**Source**: [https://proceedings.mlr.press/v235/gu24a.html](https://proceedings.mlr.press/v235/gu24a.html)

**TLDR**: This work reveals miscalibration in human pose estimation confidence scores and proposes principled calibration methods to align confidence with accuracy.

## Abstract

2D human pose estimation predicts keypoint locations and the corresponding confidence. Calibration-wise, the confidence should be aligned with the pose accuracy. Yet existing pose estimation methods tend to estimate confidence with heuristics such as the maximum value of heatmaps. This work shows, through theoretical analysis and empirical verification, a calibration gap in current pose estimation frameworks. Our derivations directly lead to closed-form adjustments in the confidence based on additionally inferred instance size and visibility. Given the black-box nature of deep neural networks, however, it is not possible to close the gap with only closed-form adjustments. We go one step further and propose a Calibrated ConfidenceNet (CCNet) to explicitly learn network-specific adjustments with a confidence prediction branch. The proposed CCNet, as a lightweight post-hoc addition, improves the calibration of standard off-the-shelf pose estimation frameworks.