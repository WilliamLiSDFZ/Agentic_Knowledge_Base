---
title: "Estimating Heterogeneous Treatment Effects by Combining Weak Instruments and Observational Data"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/d738aefead8500f5aed667f0a7ca7b7c-Abstract-Conference.html"
categories: ['quantile-based-conditional-treatment-effect-estimation']
tags: ['heterogeneous-treatment-effects', 'instrumental-variables', 'observational-data']
venue: "NeurIPS 2024"
tldr: "A method combining weak instruments with observational data is proposed to accurately estimate conditional average treatment effects."
---

# Estimating Heterogeneous Treatment Effects by Combining Weak Instruments and Observational Data

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/d738aefead8500f5aed667f0a7ca7b7c-Abstract-Conference.html](https://papers.nips.cc/paper_files/paper/2024/hash/d738aefead8500f5aed667f0a7ca7b7c-Abstract-Conference.html)

**TLDR**: A method combining weak instruments with observational data is proposed to accurately estimate conditional average treatment effects.

## Abstract

Accurately predicting conditional average treatment effects (CATEs) is crucial in personalized medicine and digital platform analytics. Since the treatments of interest often cannot be directly randomized, observational data is leveraged to learn CATEs, but this approach can incur significant bias from unobserved confounding. One strategy to overcome these limitations is to leverage instrumental variables (IVs) as latent quasi-experiments, such as randomized intent-to-treat assignments or randomized product recommendations. This approach, on the other hand, can suffer from low compliance, i.e., IV weakness. Some subgroups may even exhibit zero compliance, meaning we cannot instrument for their CATEs at all. In this paper, we develop a novel approach to combine IV and observational data to enable reliable CATE estimation in the presence of unobserved confounding in the observational data and low compliance in the IV data, including no compliance for some subgroups. We propose a two-stage framework that first learns \textit{biased} CATEs from the observational data, and then applies a compliance-weighted correction using IV data, effectively leveraging IV strength variability across covariates. We characterize the convergence rates of our method and validate its effectiveness through a simulation study. Additionally, we demonstrate its utility with real data by analyzing the heterogeneous effects of 401(k) plan participation on wealth.