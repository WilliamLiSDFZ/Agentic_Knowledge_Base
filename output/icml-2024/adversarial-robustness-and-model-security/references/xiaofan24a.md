---
title: "Intersecting-Boundary-Sensitive Fingerprinting for Tampering Detection of DNN Models"
source: "https://proceedings.mlr.press/v235/xiaofan24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/xiaofan24a/xiaofan24a.pdf"
categories: ['adversarial-robustness-and-model-security', 'anomaly-and-out-of-distribution-detection']
tags: ['DNN-fingerprinting', 'tampering-detection', 'model-security']
venue: "ICML 2024"
tldr: "A boundary-sensitive fingerprinting method to detect tampering of deployed DNN models in cloud-based AI services."
---

# Intersecting-Boundary-Sensitive Fingerprinting for Tampering Detection of DNN Models

**Source**: [https://proceedings.mlr.press/v235/xiaofan24a.html](https://proceedings.mlr.press/v235/xiaofan24a.html)

**TLDR**: A boundary-sensitive fingerprinting method to detect tampering of deployed DNN models in cloud-based AI services.

## Abstract

Cloud-based AI services offer numerous benefits but also introduce vulnerabilities, allowing for tampering with deployed DNN models, ranging from injecting malicious behaviors to reducing computing resources. Fingerprint samples are generated to query models to detect such tampering. In this paper, we present Intersecting-Boundary-Sensitive Fingerprinting (IBSF), a novel method for black-box integrity verification of DNN models using only top-1 labels. Recognizing that tampering with a model alters its decision boundary, IBSF crafts fingerprint samples from normal samples by maximizing the partial Shannon entropy of a selected subset of categories to position the fingerprint samples near decision boundaries where the categories in the subset intersect. These fingerprint samples are almost indistinguishable from their source samples. We theoretically establish and confirm experimentally that these fingerprint samples’ expected sensitivity to tampering increases with the cardinality of the subset. Extensive evaluation demonstrates that IBSF surpasses existing state-of-the-art fingerprinting methods, particularly with larger subset cardinality, establishing its state-of-the-art performance in black-box tampering detection using only top-1 labels. The IBSF code is available at https://github.com/CGCL-codes/IBSF.