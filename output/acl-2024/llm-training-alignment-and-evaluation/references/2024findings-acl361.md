---
title: "Advancing Post-OCR Correction: A Comparative Study of Synthetic Data"
source: "https://aclanthology.org/2024.findings-acl.361/"
categories: ['ocr-and-ancient-script-nlp', 'llm-training-alignment-and-evaluation']
tags: ['post-ocr-correction', 'synthetic-data', 'data-augmentation']
venue: "ACL 2024"
tldr: "Explores synthetic data strategies for improving post-OCR text correction through volume, augmentation, and generation method comparisons."
---

# Advancing Post-OCR Correction: A Comparative Study of Synthetic Data

**Source**: [https://aclanthology.org/2024.findings-acl.361/](https://aclanthology.org/2024.findings-acl.361/)

**TLDR**: Explores synthetic data strategies for improving post-OCR text correction through volume, augmentation, and generation method comparisons.

## Abstract

AbstractThis paper explores the application of synthetic data in the post-OCR domain on multiple fronts by conducting experiments to assess the impact of data volume, augmentation, and synthetic data generation methods on model performance. Furthermore, we introduce a novel algorithm that leverages computer vision feature detection algorithms to calculate glyph similarity for constructing post-OCR synthetic data. Through experiments conducted across a variety of languages, including several low-resource ones, we demonstrate that models like ByT5 can significantly reduce Character Error Rates (CER) without the need for manually annotated data, and our proposed synthetic data generation method shows advantages over traditional methods, particularly in low-resource languages.