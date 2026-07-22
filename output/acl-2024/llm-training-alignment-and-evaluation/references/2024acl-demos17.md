---
title: "IMGTB: A Framework for Machine-Generated Text Detection Benchmarking"
source: "https://aclanthology.org/2024.acl-demos.17/"
categories: ['llm-security-robustness-and-detection', 'llm-training-alignment-and-evaluation']
tags: ['machine-generated-text', 'detection', 'benchmarking']
venue: "ACL 2024"
tldr: "IMGTB provides a standardized benchmarking framework for evaluating machine-generated text detection methods."
---

# IMGTB: A Framework for Machine-Generated Text Detection Benchmarking

**Source**: [https://aclanthology.org/2024.acl-demos.17/](https://aclanthology.org/2024.acl-demos.17/)

**TLDR**: IMGTB provides a standardized benchmarking framework for evaluating machine-generated text detection methods.

## Abstract

AbstractIn the era of large language models generating high quality texts, it is a necessity to develop methods for detection of machine-generated text to avoid their harmful use or simply for annotation purposes. It is, however, also important to properly evaluate and compare such developed methods. Recently, a few benchmarks have been proposed for this purpose; however, integration of newest detection methods is rather challenging, since new methods appear each month and provide slightly different evaluation pipelines.In this paper, we present the IMGTB framework, which simplifies the benchmarking of machine-generated text detection methods by easy integration of custom (new) methods and evaluation datasets. In comparison to existing frameworks, it enables to objectively compare statistical metric-based zero-shot detectors with classification-based detectors and with differently fine-tuned detectors. Its configurability and flexibility makes research and development of new detection methods easier, especially their comparison to the existing state-of-the-art detectors. The default set of analyses, metrics and visualizations offered by the tool follows the established practices of machine-generated text detection benchmarking found in state-of-the-art literature.