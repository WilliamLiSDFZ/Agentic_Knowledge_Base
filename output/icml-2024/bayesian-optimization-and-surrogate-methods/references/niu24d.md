---
title: "Multi-Fidelity Residual Neural Processes for Scalable Surrogate Modeling"
source: "https://proceedings.mlr.press/v235/niu24d.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/niu24d/niu24d.pdf"
categories: ['bayesian-optimization-and-surrogate-methods', 'neural-operators-for-pde-solving']
tags: ['multi-fidelity', 'surrogate-modeling', 'neural-processes']
venue: "ICML 2024"
tldr: "Introduces multi-fidelity residual neural processes for scalable surrogate modeling that combines data from multiple fidelity sources efficiently."
---

# Multi-Fidelity Residual Neural Processes for Scalable Surrogate Modeling

**Source**: [https://proceedings.mlr.press/v235/niu24d.html](https://proceedings.mlr.press/v235/niu24d.html)

**TLDR**: Introduces multi-fidelity residual neural processes for scalable surrogate modeling that combines data from multiple fidelity sources efficiently.

## Abstract

Multi-fidelity surrogate modeling aims to learn an accurate surrogate at the highest fidelity level by combining data from multiple sources. Traditional methods relying on Gaussian processes can hardly scale to high-dimensional data. Deep learning approaches utilize neural network based encoders and decoders to improve scalability. These approaches share encoded representations across fidelities without including corresponding decoder parameters. This hinders inference performance, especially in out-of-distribution scenarios when the highest fidelity data has limited domain coverage. To address these limitations, we propose Multi-fidelity Residual Neural Processes (MFRNP), a novel multi-fidelity surrogate modeling framework. MFRNP explicitly models the residual between the aggregated output from lower fidelities and ground truth at the highest fidelity. The aggregation introduces decoders into the information sharing step and optimizes lower fidelity decoders to accurately capture both in-fidelity and cross-fidelity information. We show that MFRNP significantly outperforms state-of-the-art in learning partial differential equations and a real-world climate modeling task. Our code is published at: https://github.com/Rose-STL-Lab/MFRNP