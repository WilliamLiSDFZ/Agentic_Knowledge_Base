---
title: "Learning Shadow Variable Representation for Treatment Effect Estimation under Collider Bias"
source: "https://proceedings.mlr.press/v235/li24am.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/li24am/li24am.pdf"
categories: ['causal-inference-and-discovery-methods', 'causal-ml-for-clinical-decision-making']
tags: ['shadow-variables', 'collider-bias', 'treatment-effect', 'sample-selection-bias', 'causal']
venue: "ICML 2024"
tldr: "A shadow variable representation learning method addresses collider bias for treatment effect estimation in observational data."
---

# Learning Shadow Variable Representation for Treatment Effect Estimation under Collider Bias

**Source**: [https://proceedings.mlr.press/v235/li24am.html](https://proceedings.mlr.press/v235/li24am.html)

**TLDR**: A shadow variable representation learning method addresses collider bias for treatment effect estimation in observational data.

## Abstract

One of the significant challenges in treatment effect estimation is collider bias, a specific form of sample selection bias induced by the common causes of both the treatment and outcome. Identifying treatment effects under collider bias requires well-defined shadow variables in observational data, which are assumed to be related to the outcome and independent of the sample selection mechanism, conditional on the other observed variables. However, finding a valid shadow variable is not an easy task in real-world scenarios and requires domain-specific knowledge from experts. Therefore, in this paper, we propose a novel method that can automatically learn shadow-variable representations from observational data without prior knowledge. To ensure the learned representations satisfy the assumptions of the shadow variable, we introduce a tester to perform hypothesis testing in the representation learning process. We iteratively generate representations and test whether they satisfy the shadow-variable assumptions until they pass the test. With the help of the learned shadow-variable representations, we propose a novel treatment effect estimator to address collider bias. Experiments show that the proposed methods outperform existing treatment effect estimation methods under collider bias and prove their potential application value.