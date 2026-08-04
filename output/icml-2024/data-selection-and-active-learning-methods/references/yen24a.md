---
title: "Adaptive Sampling of k-Space in Magnetic Resonance for Rapid Pathology Prediction"
source: "https://proceedings.mlr.press/v235/yen24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/yen24a/yen24a.pdf"
categories: ['data-selection-and-active-learning-methods']
tags: ['MRI', 'k-space', 'adaptive-sampling', 'pathology-prediction']
venue: "ICML 2024"
tldr: "An adaptive k-space sampling strategy for MRI is proposed to enable rapid pathology prediction with fewer measurements."
---

# Adaptive Sampling of k-Space in Magnetic Resonance for Rapid Pathology Prediction

**Source**: [https://proceedings.mlr.press/v235/yen24a.html](https://proceedings.mlr.press/v235/yen24a.html)

**TLDR**: An adaptive k-space sampling strategy for MRI is proposed to enable rapid pathology prediction with fewer measurements.

## Abstract

Magnetic Resonance (MR) imaging, despite its proven diagnostic utility, remains an inaccessible imaging modality for disease surveillance at the population level. A major factor rendering MR inaccessible is lengthy scan times. An MR scanner collects measurements associated with the underlying anatomy in the Fourier space, also known as the k-space. Creating a high-fidelity image requires collecting large quantities of such measurements, increasing the scan time. Traditionally to accelerate an MR scan, image reconstruction from under-sampled k-space data is the method of choice. However, recent works show the feasibility of bypassing image reconstruction and directly learning to detect disease directly from a sparser learned subset of the k-space measurements. In this work, we propose Adaptive Sampling for MR (ASMR), a sampling method that learns an adaptive policy to sequentially select k-space samples to optimize for target disease detection. On 6 out of 8 pathology classification tasks spanning the Knee, Brain, and Prostate MR scans, ASMR reaches within 2% of the performance of a fully sampled classifier while using only 8% of the k-space, as well as outperforming prior state-of-the-art work in k-space sampling such as EMRT, LOUPE, and DPS.