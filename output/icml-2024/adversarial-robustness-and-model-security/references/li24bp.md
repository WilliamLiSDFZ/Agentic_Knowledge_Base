---
title: "OODRobustBench: a Benchmark and Large-Scale Analysis of Adversarial Robustness under Distribution Shift"
source: "https://proceedings.mlr.press/v235/li24bp.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/li24bp/li24bp.pdf"
categories: ['adversarial-robustness-and-model-security', 'anomaly-and-out-of-distribution-detection']
tags: ['adversarial-robustness', 'distribution-shift', 'OOD-benchmark']
venue: "ICML 2024"
tldr: "Introduces OODRobustBench to benchmark adversarial robustness of models under input distribution shifts."
---

# OODRobustBench: a Benchmark and Large-Scale Analysis of Adversarial Robustness under Distribution Shift

**Source**: [https://proceedings.mlr.press/v235/li24bp.html](https://proceedings.mlr.press/v235/li24bp.html)

**TLDR**: Introduces OODRobustBench to benchmark adversarial robustness of models under input distribution shifts.

## Abstract

Existing works have made great progress in improving adversarial robustness, but typically test their method only on data from the same distribution as the training data, i.e. in-distribution (ID) testing. As a result, it is unclear how such robustness generalizes under input distribution shifts, i.e. out-of-distribution (OOD) testing. This omission is concerning as such distribution shifts are unavoidable when methods are deployed in the wild. To address this issue we propose a benchmark named OODRobustBench to comprehensively assess OOD adversarial robustness using 23 dataset-wise shifts (i.e. naturalistic shifts in input distribution) and 6 threat-wise shifts (i.e., unforeseen adversarial threat models). OODRobustBench is used to assess 706 robust models using 60.7K adversarial evaluations. This large-scale analysis shows that: 1) adversarial robustness suffers from a severe OOD generalization issue; 2) ID robustness correlates strongly with OOD robustness in a positive linear way. The latter enables the prediction of OOD robustness from ID robustness. We then predict and verify that existing methods are unlikely to achieve high OOD robustness. Novel methods are therefore required to achieve OOD robustness beyond our prediction. To facilitate the development of these methods, we investigate a wide range of techniques and identify several promising directions. Code and models are available at: https://github.com/OODRobustBench/OODRobustBench.