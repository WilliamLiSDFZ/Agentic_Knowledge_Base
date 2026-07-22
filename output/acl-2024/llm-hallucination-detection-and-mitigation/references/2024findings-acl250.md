---
title: "Selectively Answering Visual Questions"
source: "https://aclanthology.org/2024.findings-acl.250/"
pdf_url: ""
categories: ['multimodal-language-vision-learning-systems', 'llm-hallucination-detection-and-mitigation']
tags: ['visual-question-answering', 'selective-prediction', 'confidence-calibration']
venue: "ACL 2024"
tldr: "This paper addresses selective answering in large multimodal models for VQA, focusing on when to abstain to improve reliability for accessibility applications."
---

# Selectively Answering Visual Questions

**Source**: [https://aclanthology.org/2024.findings-acl.250/](https://aclanthology.org/2024.findings-acl.250/)

**TLDR**: This paper addresses selective answering in large multimodal models for VQA, focusing on when to abstain to improve reliability for accessibility applications.

## Abstract

AbstractRecently, large multi-modal models (LMMs) have emerged with the capacity to perform vision tasks such as captioning and visual question answering (VQA) with unprecedented accuracy. Applications such as helping the blind or visually impaired have a critical need for precise answers. It is specially important for models to be well calibrated and be able to quantify their uncertainty in order to selectively decide when to answer and when to abstain or ask for clarifications. We perform the first in-depth analysis of calibration methods and metrics for VQA with in-context learning LMMs. Studying VQA on two answerability benchmarks, we show that the likelihood score of visually grounded models is better calibrated than in their text-only counterparts for in-context learning, where sampling based methods are generally superior, but no clear winner arises. We propose Avg BLEU, a calibration score combining the benefits of both sampling and likelihood methods across modalities.