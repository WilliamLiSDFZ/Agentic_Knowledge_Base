---
title: "Prediction-powered Generalization of Causal Inferences"
source: "https://proceedings.mlr.press/v235/demirel24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/demirel24a/demirel24a.pdf"
categories: ['causal-inference-and-discovery-methods', 'statistical-learning-robustness-uncertainty-quantification']
tags: ['causal-inference', 'generalization', 'randomized-controlled-trials', 'prediction-powered-inference', 'target-population']
venue: "ICML 2024"
tldr: "Proposes prediction-powered inference to generalize causal estimates from randomized trials to target populations using unlabeled covariate data."
---

# Prediction-powered Generalization of Causal Inferences

**Source**: [https://proceedings.mlr.press/v235/demirel24a.html](https://proceedings.mlr.press/v235/demirel24a.html)

**TLDR**: Proposes prediction-powered inference to generalize causal estimates from randomized trials to target populations using unlabeled covariate data.

## Abstract

Causal inferences from a randomized controlled trial (RCT) may not pertain to a target population where some effect modifiers have a different distribution. Prior work studies generalizing the results of a trial to a target population with no outcome but covariate data available. We show how the limited size of trials makes generalization a statistically infeasible task, as it requires estimating complex nuisance functions. We develop generalization algorithms that supplement the trial data with a prediction model learned from an additional observational study (OS), without making any assumptions on the OS. We theoretically and empirically show that our methods facilitate better generalization when the OS is "high-quality", and remain robust when it is not, and e.g., have unmeasured confounding.