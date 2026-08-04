---
title: "Implicit Representations for Constrained Image Segmentation"
source: "https://proceedings.mlr.press/v235/schneider24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/schneider24a/schneider24a.pdf"
categories: ['generative-models-and-variational-inference', 'image-quality-assessment-and-super-resolution']
tags: ['implicit-representations', 'image-segmentation', 'constraints', 'neural-fields', 'coordinate-networks']
venue: "ICML 2024"
tldr: "Implicit neural representations are used as internal representations for constrained image segmentation, enabling smooth incorporation of shape and topology constraints."
---

# Implicit Representations for Constrained Image Segmentation

**Source**: [https://proceedings.mlr.press/v235/schneider24a.html](https://proceedings.mlr.press/v235/schneider24a.html)

**TLDR**: Implicit neural representations are used as internal representations for constrained image segmentation, enabling smooth incorporation of shape and topology constraints.

## Abstract

Implicit representations allow to use a parametric function that maps (spatial) coordinates to the value that is traditionally stored in each pixel, e.g. RGB values, instead of a discrete grid. This has recently proven quite advantageous as an internal representation for images or scenes for deep learning models. Yet, its potential to ensure certain properties of the solution has not yet been fully explored. In this work, we demonstrate that implicit representations are a powerful tool for enforcing a variety of different geometric constraints in image segmentation. While convexity, star-shape, path-connectedness, periodicity, or symmetry of the (spatial or space-time) region to be segmented are very challenging to enforce for pixel-wise discretizations, a suitable parametrization of an implicit representation, mapping spatial or spatio-temporal coordinates to the likeliness of a pixel belonging to the fore- or background, allows to provably ensure such constraints. Several numerical examples demonstrate that challenging segmentation scenarios can benefit from the inclusion of application-specific constraints, e.g. when occlusions prevent a faithful segmentation with classical approaches.