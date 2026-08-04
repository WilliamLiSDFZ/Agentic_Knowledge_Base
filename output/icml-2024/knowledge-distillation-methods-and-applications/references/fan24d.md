---
title: "Revisit the Essence of Distilling Knowledge through Calibration"
source: "https://proceedings.mlr.press/v235/fan24d.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/fan24d/fan24d.pdf"
categories: ['knowledge-distillation-methods-and-applications']
tags: ['knowledge-distillation', 'calibration', 'capacity-mismatch']
venue: "ICML 2024"
tldr: "Revisits knowledge distillation through a calibration lens to explain and address the capacity mismatch phenomenon."
---

# Revisit the Essence of Distilling Knowledge through Calibration

**Source**: [https://proceedings.mlr.press/v235/fan24d.html](https://proceedings.mlr.press/v235/fan24d.html)

**TLDR**: Revisits knowledge distillation through a calibration lens to explain and address the capacity mismatch phenomenon.

## Abstract

Knowledge Distillation (KD) has evolved into a practical technology for transferring knowledge from a well-performing model (teacher) to a weak model (student). A counter-intuitive phenomenon known as capacity mismatch has been identified, wherein KD performance may not be good when a better teacher instructs the student. Various preliminary methods have been proposed to alleviate capacity mismatch, but a unifying explanation for its cause remains lacking. In this paper, we propose a unifying analytical framework to pinpoint the core of capacity mismatch based on calibration. Through extensive analytical experiments, we observe a positive correlation between the calibration of the teacher model and the KD performance with original KD methods. As this correlation arises due to the sensitivity of metrics (e.g., KL divergence) to calibration, we recommend employing measurements insensitive to calibration such as ranking-based loss. Our experiments demonstrate that ranking-based loss can effectively replace KL divergence, aiding large models with poor calibration to teach better.