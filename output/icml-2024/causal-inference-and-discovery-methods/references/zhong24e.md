---
title: "Causal-IQA: Towards the Generalization of Image Quality Assessment Based on Causal Inference"
source: "https://proceedings.mlr.press/v235/zhong24e.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/zhong24e/zhong24e.pdf"
categories: ['image-quality-assessment-and-super-resolution', 'causal-inference-and-discovery-methods']
tags: ['image-quality-assessment', 'causal-inference', 'generalization']
venue: "ICML 2024"
tldr: "Introduces Causal-IQA, a blind IQA method using causal inference to improve generalization across datasets with limited labeled data."
---

# Causal-IQA: Towards the Generalization of Image Quality Assessment Based on Causal Inference

**Source**: [https://proceedings.mlr.press/v235/zhong24e.html](https://proceedings.mlr.press/v235/zhong24e.html)

**TLDR**: Introduces Causal-IQA, a blind IQA method using causal inference to improve generalization across datasets with limited labeled data.

## Abstract

Due to the high cost of Image Quality Assessment (IQA) datasets, achieving robust generalization remains challenging for prevalent deep learning-based IQA methods. To address this, this paper proposes a novel end-to-end blind IQA method: Causal-IQA. Specifically, we first analyze the causal mechanisms in IQA tasks and construct a causal graph to understand the interplay and confounding effects between distortion types, image contents, and subjective human ratings. Then, through shifting the focus from correlations to causality, Causal-IQA aims to improve the estimation accuracy of image quality scores by mitigating the confounding effects using a causality-based optimization strategy. This optimization strategy is implemented on the sample subsets constructed by a Counterfactual Division process based on the Backdoor Criterion. Extensive experiments illustrate the superiority of Causal-IQA.