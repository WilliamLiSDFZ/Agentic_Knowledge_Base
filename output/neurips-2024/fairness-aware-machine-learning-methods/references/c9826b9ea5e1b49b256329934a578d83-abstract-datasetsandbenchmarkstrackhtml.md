---
title: "FairMedFM: Fairness Benchmarking for Medical Imaging Foundation Models"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/c9826b9ea5e1b49b256329934a578d83-Abstract-Datasets_and_Benchmarks_Track.html"
categories: ['fairness-aware-machine-learning-methods', 'ai-benchmarking-and-evaluation-methodology']
tags: ['fairness-benchmarking', 'medical-imaging', 'foundation-models', 'bias', 'healthcare']
venue: "NeurIPS 2024"
tldr: "Introduces FairMedFM, a comprehensive fairness benchmark for evaluating medical imaging foundation models across diverse demographic groups and clinical tasks."
---

# FairMedFM: Fairness Benchmarking for Medical Imaging Foundation Models

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/c9826b9ea5e1b49b256329934a578d83-Abstract-Datasets_and_Benchmarks_Track.html](https://papers.nips.cc/paper_files/paper/2024/hash/c9826b9ea5e1b49b256329934a578d83-Abstract-Datasets_and_Benchmarks_Track.html)

**TLDR**: Introduces FairMedFM, a comprehensive fairness benchmark for evaluating medical imaging foundation models across diverse demographic groups and clinical tasks.

## Abstract

The advent of foundation models (FMs) in healthcare offers unprecedented opportunities to enhance medical diagnostics through automated classification and segmentation tasks. However, these models also raise significant concerns about their fairness, especially when applied to diverse and underrepresented populations in healthcare applications. Currently, there is a lack of comprehensive benchmarks, standardized pipelines, and easily adaptable libraries to evaluate and understand the fairness performance of FMs in medical imaging, leading to considerable challenges in formulating and implementing solutions that ensure equitable outcomes across diverse patient populations. To fill this gap, we introduce FairMedFM, a fairness benchmark for FM research in medical imaging. FairMedFM integrates with 17 popular medical imaging datasets, encompassing different modalities, dimensionalities, and sensitive attributes. It explores 20 widely used FMs, with various usages such as zero-shot learning, linear probing, parameter-efficient fine-tuning, and prompting in various downstream tasks -- classification and segmentation. Our exhaustive analysis evaluates the fairness performance over different evaluation metrics from multiple perspectives, revealing the existence of bias, varied utility-fairness trade-offs on different FMs, consistent disparities on the same datasets regardless FMs, and limited effectiveness of existing unfairness mitigation methods. Furthermore, FairMedFM provides an open-sourced codebase at https://github.com/FairMedFM/FairMedFM, supporting extendible functionalities and applications and inclusive for studies on FMs in medical imaging over the long term.