---
title: "Enhancing Hallucination Detection through Perturbation-Based Synthetic Data Generation in System Responses"
source: "https://aclanthology.org/2024.findings-acl.789/"
categories: ['llm-hallucination-detection-and-mitigation', 'collaborative-llm-deployment-and-inference-optimization']
tags: ['hallucination-detection', 'synthetic-data', 'perturbation']
venue: "ACL 2024"
tldr: "Uses perturbation-based synthetic data generation to train hallucination classifiers for LLM outputs without expensive manual annotation."
---

# Enhancing Hallucination Detection through Perturbation-Based Synthetic Data Generation in System Responses

**Source**: [https://aclanthology.org/2024.findings-acl.789/](https://aclanthology.org/2024.findings-acl.789/)

**TLDR**: Uses perturbation-based synthetic data generation to train hallucination classifiers for LLM outputs without expensive manual annotation.

## Abstract

AbstractDetecting hallucinations in large language model (LLM) outputs is pivotal, yet traditional fine-tuning for this classification task is impeded by the expensive and quickly outdated annotation process, especially across numerous vertical domains and in the face of rapid LLM advancements. In this study, we introduce an approach that automatically generates both faithful and hallucinated outputs by rewriting system responses. Experimental findings demonstrate that a T5-base model, fine-tuned on our generated dataset, surpasses state-of-the-art zero-shot detectors and existing synthetic generation methods in both accuracy and latency, indicating efficacy of our approach.