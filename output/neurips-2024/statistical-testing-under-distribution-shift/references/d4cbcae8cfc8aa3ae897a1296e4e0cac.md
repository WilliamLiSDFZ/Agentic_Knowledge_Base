---
title: "Truthfulness of Calibration Measures"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/d4cbcae8cfc8aa3ae897a1296e4e0cac-Abstract-Conference.html"
categories: ['machine-learning-theory-and-evaluation-methods', 'statistical-testing-under-distribution-shift']
tags: ['calibration', 'truthfulness', 'sequential-prediction']
venue: "NeurIPS 2024"
tldr: "Studies truthfulness as a desideratum for calibration measures in sequential prediction, alongside completeness and soundness properties."
---

# Truthfulness of Calibration Measures

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/d4cbcae8cfc8aa3ae897a1296e4e0cac-Abstract-Conference.html](https://papers.nips.cc/paper_files/paper/2024/hash/d4cbcae8cfc8aa3ae897a1296e4e0cac-Abstract-Conference.html)

**TLDR**: Studies truthfulness as a desideratum for calibration measures in sequential prediction, alongside completeness and soundness properties.

## Abstract

We study calibration measures in a sequential prediction setup. In addition to rewarding accurate predictions (completeness) and penalizing incorrect ones (soundness), an important desideratum of calibration measures is truthfulness, a minimal condition for the forecaster not to be incentivized to exploit the system. Formally, a calibration measure is truthful if the forecaster (approximately) minimizes the expected penalty by predicting the conditional expectation of the next outcome, given the prior distribution of outcomes. We conduct a taxonomy of existing calibration measures. Perhaps surprisingly, all of them are far from being truthful. We introduce a new calibration measure termed the Subsampled Smooth Calibration Error (SSCE), which is complete and sound, and under which truthful prediction is optimal up to a constant multiplicative factor. In contrast, under existing calibration measures, there are simple distributions on which a polylogarithmic (or even zero) penalty is achievable, while truthful prediction leads to a polynomial penalty.