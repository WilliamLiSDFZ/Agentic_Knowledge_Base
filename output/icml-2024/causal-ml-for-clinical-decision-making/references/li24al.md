---
title: "A Generative Approach for Treatment Effect Estimation under Collider Bias: From an Out-of-Distribution Perspective"
source: "https://proceedings.mlr.press/v235/li24al.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/li24al/li24al.pdf"
categories: ['causal-inference-and-discovery-methods', 'causal-ml-for-clinical-decision-making']
tags: ['treatment-effect', 'collider-bias', 'generative-model', 'out-of-distribution', 'causal-inference']
venue: "ICML 2024"
tldr: "A generative approach reframes collider bias as an OOD problem to improve treatment effect estimation from observational data."
---

# A Generative Approach for Treatment Effect Estimation under Collider Bias: From an Out-of-Distribution Perspective

**Source**: [https://proceedings.mlr.press/v235/li24al.html](https://proceedings.mlr.press/v235/li24al.html)

**TLDR**: A generative approach reframes collider bias as an OOD problem to improve treatment effect estimation from observational data.

## Abstract

Resulting from non-random sample selection caused by both the treatment and outcome, collider bias poses a unique challenge to treatment effect estimation using observational data whose distribution differs from that of the target population. In this paper, we rethink collider bias from an out-of-distribution (OOD) perspective, considering that the entire data space of the target population consists of two different environments: The observational data selected from the target population belongs to a seen environment labeled with $S=1$ and the missing unselected data belongs to another unseen environment labeled with $S=0$. Based on this OOD formulation, we utilize small-scale representative data from the entire data space with no environmental labels and propose a novel method, i.e., Coupled Counterfactual Generative Adversarial Model (C$^2$GAM), to simultaneously generate the missing $S=0$ samples in observational data and the missing $S$ labels in the small-scale representative data. With the help of C$^2$GAM, collider bias can be addressed by combining the generated $S=0$ samples and the observational data to estimate treatment effects. Extensive experiments on synthetic and real-world data demonstrate that plugging C$^2$GAM into existing treatment effect estimators achieves significant performance improvements.