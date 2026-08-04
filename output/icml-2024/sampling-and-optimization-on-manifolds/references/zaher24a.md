---
title: "Manifold Integrated Gradients: Riemannian Geometry for Feature Attribution"
source: "https://proceedings.mlr.press/v235/zaher24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/zaher24a/zaher24a.pdf"
categories: ['ai-explainability-uncertainty-human-decision-making', 'sampling-and-optimization-on-manifolds']
tags: ['integrated-gradients', 'feature-attribution', 'Riemannian-geometry', 'explainability']
venue: "ICML 2024"
tldr: "Manifold Integrated Gradients improves feature attribution reliability by constraining integration paths to data manifolds using Riemannian geometry."
---

# Manifold Integrated Gradients: Riemannian Geometry for Feature Attribution

**Source**: [https://proceedings.mlr.press/v235/zaher24a.html](https://proceedings.mlr.press/v235/zaher24a.html)

**TLDR**: Manifold Integrated Gradients improves feature attribution reliability by constraining integration paths to data manifolds using Riemannian geometry.

## Abstract

In this paper, we dive into the reliability concerns of Integrated Gradients (IG), a prevalent feature attribution method for black-box deep learning models. We particularly address two predominant challenges associated with IG: the generation of noisy feature visualizations for vision models and the vulnerability to adversarial attributional attacks. Our approach involves an adaptation of path-based feature attribution, aligning the path of attribution more closely to the intrinsic geometry of the data manifold. Our experiments utilise deep generative models applied to several real-world image datasets. They demonstrate that IG along the geodesics conforms to the curved geometry of the Riemannian data manifold, generating more perceptually intuitive explanations and, subsequently, substantially increasing robustness to targeted attributional attacks.