---
title: "Identifying and Mitigating Annotation Bias in Natural Language Understanding using Causal Mediation Analysis"
source: "https://aclanthology.org/2024.findings-acl.686/"
pdf_url: ""
categories: ['bias-and-fairness-in-llms', 'causal-reasoning-and-explanation-in-nlp']
tags: ['annotation-bias', 'causal-mediation', 'natural-language-understanding']
venue: "ACL 2024"
tldr: "Applies causal mediation analysis to identify and mitigate annotation bias in NLU models to improve out-of-distribution performance."
---

# Identifying and Mitigating Annotation Bias in Natural Language Understanding using Causal Mediation Analysis

**Source**: [https://aclanthology.org/2024.findings-acl.686/](https://aclanthology.org/2024.findings-acl.686/)

**TLDR**: Applies causal mediation analysis to identify and mitigate annotation bias in NLU models to improve out-of-distribution performance.

## Abstract

AbstractNLU models have achieved promising results on standard benchmarks. Despite state-of-the-art accuracy, analysis reveals that many models make predictions using annotation bias rather than the properties we intend the model to learn. Consequently, these models perform poorly on out-of-distribution datasets. Recent advances in bias mitigation show that annotation bias can be alleviated through fine-tuning debiasing objectives. In this paper, we apply causal mediation analysis to gauge how much each model component mediates annotation biases. Using the knowledge from the causal analysis, we improve the model’s robustness against annotation bias through two bias mitigation methods: causal-grounded masking and gradient unlearning. Causal analysis reveals that biases concentrated in specific components, even after employing other training-time debiasing techniques. Manipulating these components by masking out neurons’ activations or updating specific weight blocks both demonstrably improve robustness against annotation artifacts.