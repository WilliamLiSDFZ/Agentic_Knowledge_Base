---
title: "Tight Partial Identification of Causal Effects with Marginal Distribution of Unmeasured Confounders"
source: "https://proceedings.mlr.press/v235/zhang24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/zhang24a/zhang24a.pdf"
categories: ['causal-inference-and-discovery-methods', 'statistical-learning-robustness-uncertainty-quantification']
tags: ['partial-identification', 'causal-effects', 'unmeasured-confounders']
venue: "ICML 2024"
tldr: "A tight partial identification framework for causal effects using only the marginal distribution of unmeasured confounders without requiring auxiliary variables."
---

# Tight Partial Identification of Causal Effects with Marginal Distribution of Unmeasured Confounders

**Source**: [https://proceedings.mlr.press/v235/zhang24a.html](https://proceedings.mlr.press/v235/zhang24a.html)

**TLDR**: A tight partial identification framework for causal effects using only the marginal distribution of unmeasured confounders without requiring auxiliary variables.

## Abstract

Partial identification (PI) presents a significant challenge in causal inference due to the incomplete measurement of confounders. Given that obtaining auxiliary variables of confounders is not always feasible and relies on untestable assumptions, researchers are encouraged to explore the internal information of latent confounders without external assistance. However, these prevailing PI results often lack precise mathematical measurement from observational data or assume that the information pertaining to confounders falls within extreme scenarios. In our paper, we reassess the significance of the marginal confounder distribution in PI. We refrain from imposing additional restrictions on the marginal confounder distribution, such as entropy or mutual information. Instead, we establish the closed-form tight PI for any possible P(U) in the discrete case. Furthermore, we establish the if and only if criterion for discerning whether the marginal confounder information leads to non-vanilla PI regions. This reveals a fundamental negative result wherein the marginal confounder information minimally contributes to PI as the confounder’s cardinality increases. Our theoretical findings are supported by experiments.