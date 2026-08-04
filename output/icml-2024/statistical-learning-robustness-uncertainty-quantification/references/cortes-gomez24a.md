---
title: "Statistical Inference Under Constrained Selection Bias"
source: "https://proceedings.mlr.press/v235/cortes-gomez24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/cortes-gomez24a/cortes-gomez24a.pdf"
categories: ['statistical-learning-robustness-uncertainty-quantification', 'causal-inference-and-discovery-methods']
tags: ['selection-bias', 'robust-inference', 'distribution-shift']
venue: "ICML 2024"
tldr: "Proposes a framework for statistical inference under constrained selection bias to enable robust decision-making from observational data."
---

# Statistical Inference Under Constrained Selection Bias

**Source**: [https://proceedings.mlr.press/v235/cortes-gomez24a.html](https://proceedings.mlr.press/v235/cortes-gomez24a.html)

**TLDR**: Proposes a framework for statistical inference under constrained selection bias to enable robust decision-making from observational data.

## Abstract

Large-scale datasets are increasingly being used to inform decision making. While this effort aims to ground policy in real-world evidence, challenges have arisen as selection bias and other forms of distribution shifts often plague observational data. Previous attempts to provide robust inference have given guarantees depending on a user-specified amount of possible distribution shift (e.g., the maximum KL divergence between the observed and target distributions). However, decision makers will often have additional knowledge about the target distribution which constrains the kind of possible shifts. To leverage such information, we propose a framework that enables statistical inference in the presence of selection bias which obeys user-specified constraints in the form of functions whose expectation is known under the target distribution. The output is high-probability bounds on the value of an estimand for the target distribution. Hence, our method leverages domain knowledge in order to partially identify a wide class of estimands. We analyze the computational and statistical properties of methods to estimate these bounds and show that our method can produce informative bounds on a variety of simulated and semisynthetic tasks, as well as in a real-world use case.