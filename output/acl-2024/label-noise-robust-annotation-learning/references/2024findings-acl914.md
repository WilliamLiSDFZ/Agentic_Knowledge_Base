---
title: "Refining Corpora from a Model Calibration Perspective for Chinese Spelling Correction"
source: "https://aclanthology.org/2024.findings-acl.914/"
pdf_url: ""
categories: ['nlp-for-asian-languages', 'label-noise-robust-annotation-learning']
tags: ['chinese-spelling-correction', 'data-augmentation', 'model-calibration']
venue: "ACL 2024"
tldr: "Proposes a corpus refinement approach from a model calibration perspective to improve data quality for Chinese spelling correction."
---

# Refining Corpora from a Model Calibration Perspective for Chinese Spelling Correction

**Source**: [https://aclanthology.org/2024.findings-acl.914/](https://aclanthology.org/2024.findings-acl.914/)

**TLDR**: Proposes a corpus refinement approach from a model calibration perspective to improve data quality for Chinese spelling correction.

## Abstract

AbstractChinese Spelling Correction (CSC) commonly lacks large-scale high-quality corpora, due to the labor-intensive labeling of spelling errors in real-life human writing or typing scenarios. Two data augmentation methods are widely adopted: (1) *Random Replacement* with the guidance of confusion sets and (2) *OCR/ASR-based Generation* that simulates character misusing. However, both methods inevitably introduce noisy data (e.g., false spelling errors), potentially leading to over-correction. By carefully analyzing the two types of corpora, we find that though the latter achieves more robust generalization performance, the former yields better-calibrated CSC models. We then provide a theoretical analysis of this empirical observation, based on which a corpus refining strategy is proposed. Specifically, OCR/ASR-based data samples are fed into a well-calibrated CSC model trained on random replacement-based corpora and then filtered based on prediction confidence. By learning a simple BERT-based model on the refined OCR/ASR-based corpus, we set up impressive state-of-the-art performance on three widely-used benchmarks, while significantly alleviating over-correction (e.g., lowering false positive predictions).