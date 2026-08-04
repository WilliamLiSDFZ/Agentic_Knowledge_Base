---
title: "Energy-based Backdoor Defense without Task-Specific Samples and Model Retraining"
source: "https://proceedings.mlr.press/v235/gao24b.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/gao24b/gao24b.pdf"
categories: ['adversarial-robustness-and-model-security', 'anomaly-and-out-of-distribution-detection']
tags: ['backdoor-defense', 'energy-based-models', 'anomaly-detection', 'adversarial-robustness']
venue: "ICML 2024"
tldr: "An energy-based backdoor defense framework jointly detects and removes backdoors without requiring task-specific clean samples or model retraining."
---

# Energy-based Backdoor Defense without Task-Specific Samples and Model Retraining

**Source**: [https://proceedings.mlr.press/v235/gao24b.html](https://proceedings.mlr.press/v235/gao24b.html)

**TLDR**: An energy-based backdoor defense framework jointly detects and removes backdoors without requiring task-specific clean samples or model retraining.

## Abstract

Backdoor defense is crucial to ensure the safety and robustness of machine learning models when under attack. However, most existing methods specialize in either the detection or removal of backdoors, but seldom both. While few works have addressed both, these methods rely on strong assumptions or entail significant overhead costs, such as the need of task-specific samples for detection and model retraining for removal. Hence, the key challenge is how to reduce overhead and relax unrealistic assumptions. In this work, we propose two Energy-Based BAckdoor defense methods, called EBBA and EBBA+, that can achieve both backdoored model detection and backdoor removal with low overhead. Our contributions are twofold: First, we offer theoretical analysis for our observation that a predefined target label is more likely to occur among the top results for various samples. Inspired by this, we develop an enhanced energy-based technique, called EBBA, to detect backdoored models without task-specific samples (i.e., samples from any tasks). Secondly, we theoretically analyze that after data corruption, the original clean label of a poisoned sample is more likely to be predicted as a top output by the model, a sharp contrast to clean samples. Accordingly, we extend EBBA to develop EBBA+, a new transferred energy approach to efficiently detect poisoned images and remove backdoors without model retraining. Extensive experiments on multiple benchmark datasets demonstrate the superior performance of our methods over baselines in both backdoor detection and removal. Notably, the proposed methods can effectively detect backdoored model and poisoned images as well as remove backdoors at the same time.