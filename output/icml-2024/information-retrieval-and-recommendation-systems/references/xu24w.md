---
title: "Learning Exceptional Subgroups by End-to-End Maximizing KL-Divergence"
source: "https://proceedings.mlr.press/v235/xu24w.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/xu24w/xu24w.pdf"
categories: ['information-retrieval-and-recommendation-systems']
tags: ['subgroup-discovery', 'KL-divergence', 'exceptional-model-mining']
venue: "ICML 2024"
tldr: "An end-to-end method maximizing KL-divergence is proposed to efficiently discover exceptional subgroups in structured datasets for scientific analysis."
---

# Learning Exceptional Subgroups by End-to-End Maximizing KL-Divergence

**Source**: [https://proceedings.mlr.press/v235/xu24w.html](https://proceedings.mlr.press/v235/xu24w.html)

**TLDR**: An end-to-end method maximizing KL-divergence is proposed to efficiently discover exceptional subgroups in structured datasets for scientific analysis.

## Abstract

Finding and describing sub-populations that are exceptional in terms of a target property has important applications in many scientific disciplines, from identifying disadvantaged demographic groups in census data to finding conductive molecules within gold nanoparticles. Current approaches to finding such subgroups require pre-discretized predictive variables, do not permit non-trivial target distributions, do not scale to large datasets, and struggle to find diverse results. To address these limitations, we propose SYFLOW, an end-to-end optimizable approach in which we leverage normalizing flows to model arbitrary target distributions and introduce a novel neural layer that results in easily interpretable subgroup descriptions. We demonstrate on synthetic data, real-world data, and via a case study, that SYFLOW reliably finds highly exceptional subgroups accompanied by insightful descriptions.