---
title: "Extracting Training Data From Document-Based VQA Models"
source: "https://proceedings.mlr.press/v235/pinto24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/pinto24a/pinto24a.pdf"
categories: ['adversarial-robustness-and-model-security', 'large-language-model-alignment-and-capabilities']
tags: ['vision-language-models', 'memorization', 'training-data-extraction']
venue: "ICML 2024"
tldr: "Demonstrates that document-based VQA models can memorize and leak training data responses."
---

# Extracting Training Data From Document-Based VQA Models

**Source**: [https://proceedings.mlr.press/v235/pinto24a.html](https://proceedings.mlr.press/v235/pinto24a.html)

**TLDR**: Demonstrates that document-based VQA models can memorize and leak training data responses.

## Abstract

Vision-Language Models (VLMs) have made remarkable progress in document-based Visual Question Answering (i.e., responding to queries about the contents of an input document provided as an image). In this work, we show these models can memorize responses for training samples and regurgitate them even when the relevant visual information has been removed. This includes Personal Identifiable Information (PII) repeated once in the training set, indicating these models could divulge memorised sensitive information and therefore pose a privacy risk. We quantitatively measure the extractability of information in controlled experiments and differentiate between cases where it arises from generalization capabilities or from memorization. We further investigate the factors that influence memorization across multiple state-of-the-art models and propose an effective heuristic countermeasure that empirically prevents the extractability of PII.