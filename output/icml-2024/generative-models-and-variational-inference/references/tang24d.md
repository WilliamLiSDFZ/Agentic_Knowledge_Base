---
title: "Residual-Conditioned Optimal Transport: Towards Structure-Preserving Unpaired and Paired Image Restoration"
source: "https://proceedings.mlr.press/v235/tang24d.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/tang24d/tang24d.pdf"
categories: ['generative-models-and-variational-inference']
tags: ['image-restoration', 'optimal-transport', 'structure-preservation']
venue: "ICML 2024"
tldr: "Residual-Conditioned Optimal Transport models image restoration as an OT problem conditioned on residuals to preserve structural fidelity."
---

# Residual-Conditioned Optimal Transport: Towards Structure-Preserving Unpaired and Paired Image Restoration

**Source**: [https://proceedings.mlr.press/v235/tang24d.html](https://proceedings.mlr.press/v235/tang24d.html)

**TLDR**: Residual-Conditioned Optimal Transport models image restoration as an OT problem conditioned on residuals to preserve structural fidelity.

## Abstract

Deep learning-based image restoration methods generally struggle with faithfully preserving the structures of the original image. In this work, we propose a novel Residual-Conditioned Optimal Transport (RCOT) approach, which models image restoration as an optimal transport (OT) problem for both unpaired and paired settings, introducing the transport residual as a unique degradation-specific cue for both the transport cost and the transport map. Specifically, we first formalize a Fourier residual-guided OT objective by incorporating the degradation-specific information of the residual into the transport cost. We further design the transport map as a two-pass RCOT map that comprises a base model and a refinement process, in which the transport residual is computed by the base model in the first pass and then encoded as a degradation-specific embedding to condition the second-pass restoration. By duality, the RCOT problem is transformed into a minimax optimization problem, which can be solved by adversarially training neural networks. Extensive experiments on multiple restoration tasks show that RCOT achieves competitive performance in terms of both distortion measures and perceptual quality, restoring images with more faithful structures as compared with state-of-the-art methods.