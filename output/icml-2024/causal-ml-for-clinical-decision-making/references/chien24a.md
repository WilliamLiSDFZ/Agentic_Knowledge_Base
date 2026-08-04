---
title: "Safe Exploration in Dose Finding Clinical Trials with Heterogeneous Participants"
source: "https://proceedings.mlr.press/v235/chien24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/chien24a/chien24a.pdf"
categories: ['causal-ml-for-clinical-decision-making', 'bayesian-optimization-and-surrogate-methods']
tags: ['dose-finding', 'clinical-trials', 'safe-exploration']
venue: "ICML 2024"
tldr: "A Bayesian optimization framework for dose-finding clinical trials that accounts for participant heterogeneity and safety constraints."
---

# Safe Exploration in Dose Finding Clinical Trials with Heterogeneous Participants

**Source**: [https://proceedings.mlr.press/v235/chien24a.html](https://proceedings.mlr.press/v235/chien24a.html)

**TLDR**: A Bayesian optimization framework for dose-finding clinical trials that accounts for participant heterogeneity and safety constraints.

## Abstract

In drug development, early phase dose-finding clinical trials are carried out to identify an optimal dose to administer to patients in larger confirmatory clinical trials. Standard trial procedures do not optimize for participant benefit and do not consider participant heterogeneity, despite consequences to participants’ health and downstream impacts to under-represented population subgroups. Many novel drugs also do not obey parametric modelling assumptions made in common dose-finding procedures. We present Safe Allocation for Exploration of Treatments SAFE-T, a procedure for adaptive dose-finding that adheres to safety constraints, improves utility for heterogeneous participants, and works well with small sample sizes. SAFE-T flexibly learns non-parametric multi-output Gaussian process models for dose toxicity and efficacy, using Bayesian optimization, and provides accurate final dose recommendations. We provide theoretical guarantees for the satisfaction of safety constraints. Using a comprehensive set of realistic synthetic scenarios, we demonstrate empirically that SAFE-T generally outperforms comparable methods and maintains performance across variations in sample size and subgroup distribution. Finally, we extend SAFE-T to a new adaptive setting, demonstrating its potential to improve traditional clinical trial procedures.