---
title: "Tilt and Average : Geometric Adjustment of the Last Layer for Recalibration"
source: "https://proceedings.mlr.press/v235/cho24g.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/cho24g/cho24g.pdf"
categories: ['uncertainty-calibration-and-distribution-shift-adaptation', 'statistical-learning-robustness-uncertainty-quantification']
tags: ['calibration', 'last-layer', 'geometric-adjustment']
venue: "ICML 2024"
tldr: "A geometric tilt-and-average adjustment of the last layer is proposed for post-hoc recalibration of neural network predictions."
---

# Tilt and Average : Geometric Adjustment of the Last Layer for Recalibration

**Source**: [https://proceedings.mlr.press/v235/cho24g.html](https://proceedings.mlr.press/v235/cho24g.html)

**TLDR**: A geometric tilt-and-average adjustment of the last layer is proposed for post-hoc recalibration of neural network predictions.

## Abstract

After the revelation that neural networks tend to produce overconfident predictions, the problem of calibration, which aims to align confidence with accuracy to enhance the reliability of predictions, has gained significant importance. Several solutions based on calibration maps have been proposed to address the problem of recalibrating a trained classifier using additional datasets. In this paper, we offer an algorithm that transforms the weights of the last layer of the classifier, distinct from the calibration-map-based approach. We concentrate on the geometry of the final linear layer, specifically its angular aspect, and adjust the weights of the corresponding layer. We name the method Tilt and Average, and validate the calibration effect empirically and theoretically. Through this, we demonstrate that our approach, in addition to the existing calibration-map-based techniques, can yield improved calibration performance.