---
title: "Zero-Shot ECG Classification with Multimodal Learning and Test-time Clinical Knowledge Enhancement"
source: "https://proceedings.mlr.press/v235/liu24bg.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/liu24bg/liu24bg.pdf"
categories: ['test-time-adaptation-methods-and-evaluation', 'uncertainty-calibration-and-distribution-shift-adaptation']
tags: ['ECG-classification', 'zero-shot-learning', 'multimodal-learning', 'test-time-adaptation', 'clinical-knowledge']
venue: "ICML 2024"
tldr: "A multimodal learning framework for zero-shot ECG classification is proposed with test-time enhancement using clinical knowledge to improve cardiac arrhythmia detection."
---

# Zero-Shot ECG Classification with Multimodal Learning and Test-time Clinical Knowledge Enhancement

**Source**: [https://proceedings.mlr.press/v235/liu24bg.html](https://proceedings.mlr.press/v235/liu24bg.html)

**TLDR**: A multimodal learning framework for zero-shot ECG classification is proposed with test-time enhancement using clinical knowledge to improve cardiac arrhythmia detection.

## Abstract

Electrocardiograms (ECGs) are non-invasive diagnostic tools crucial for detecting cardiac arrhythmic diseases in clinical practice. While ECG Self-supervised Learning (eSSL) methods show promise in representation learning from unannotated ECG data, they often overlook the clinical knowledge that can be found in reports. This oversight and the requirement for annotated samples for downstream tasks limit eSSL’s versatility. In this work, we address these issues with the Multimodal ECG Representation Learning (MERL) framework. Through multimodal learning on ECG records and associated reports, MERL is capable of performing zero-shot ECG classification with text prompts, eliminating the need for training data in downstream tasks. At test time, we propose the Clinical Knowledge Enhanced Prompt Engineering (CKEPE) approach, which uses Large Language Models (LLMs) to exploit external expert-verified clinical knowledge databases, generating more descriptive prompts and reducing hallucinations in LLM-generated content to boost zero-shot classification. Based on MERL, we perform the first benchmark across six public ECG datasets, showing the superior performance of MERL compared against eSSL methods. Notably, MERL achieves an average AUC score of 75.2% in zero-shot classification (without training data), 3.2% higher than linear probed eSSL methods with 10% annotated training data, averaged across all six datasets.