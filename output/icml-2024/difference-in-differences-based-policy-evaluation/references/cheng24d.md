---
title: "Causal Inference out of Control: Estimating Performativity without Treatment Randomization"
source: "https://proceedings.mlr.press/v235/cheng24d.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/cheng24d/cheng24d.pdf"
categories: ['causal-inference-and-discovery-methods', 'difference-in-differences-based-policy-evaluation']
tags: ['performativity', 'causal-identification', 'algorithmic-interventions']
venue: "ICML 2024"
tldr: "A causal framework identifies the performative effects of algorithmic platform actions on user behavior from observational data without treatment randomization."
---

# Causal Inference out of Control: Estimating Performativity without Treatment Randomization

**Source**: [https://proceedings.mlr.press/v235/cheng24d.html](https://proceedings.mlr.press/v235/cheng24d.html)

**TLDR**: A causal framework identifies the performative effects of algorithmic platform actions on user behavior from observational data without treatment randomization.

## Abstract

Regulators and academics are increasingly interested in the causal effect that algorithmic actions of a digital platform have on user consumption. In pursuit of estimating this effect from observational data, we identify a set of assumptions that permit causal identifiability without assuming randomized platform actions. Our results are applicable to platforms that rely on machine-learning-powered predictions and leverage knowledge from historical data. The key novelty of our approach is to explicitly model the dynamics of consumption over time, exploiting the repeated interaction of digital platforms with their participants to prove our identifiability results. By viewing the platform as a controller acting on a dynamical system, we can show that exogenous variation in consumption and appropriately responsive algorithmic control actions are sufficient for identifying the causal effect of interest. We complement our claims with an analysis of ready-to-use finite sample estimators and empirical investigations. More broadly, our results deriving identifiability conditions tailored to digital platform settings illustrate a fruitful interplay of control theory and causal inference.