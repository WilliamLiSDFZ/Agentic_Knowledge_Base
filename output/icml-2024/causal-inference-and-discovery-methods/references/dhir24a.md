---
title: "Bivariate Causal Discovery using Bayesian Model Selection"
source: "https://proceedings.mlr.press/v235/dhir24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/dhir24a/dhir24a.pdf"
categories: ['causal-inference-and-discovery-methods', 'statistical-learning-robustness-uncertainty-quantification']
tags: ['causal-discovery', 'Bayesian-model-selection', 'bivariate', 'identifiability', 'causal-direction']
venue: "ICML 2024"
tldr: "Uses Bayesian model selection for bivariate causal discovery without relying on strong identifiability assumptions, improving applicability to real-world data."
---

# Bivariate Causal Discovery using Bayesian Model Selection

**Source**: [https://proceedings.mlr.press/v235/dhir24a.html](https://proceedings.mlr.press/v235/dhir24a.html)

**TLDR**: Uses Bayesian model selection for bivariate causal discovery without relying on strong identifiability assumptions, improving applicability to real-world data.

## Abstract

Much of the causal discovery literature prioritises guaranteeing the identifiability of causal direction in statistical models. For structures within a Markov equivalence class, this requires strong assumptions which may not hold in real-world datasets, ultimately limiting the usability of these methods. Building on previous attempts, we show how to incorporate causal assumptions within the Bayesian framework. Identifying causal direction then becomes a Bayesian model selection problem. This enables us to construct models with realistic assumptions, and consequently allows for the differentiation between Markov equivalent causal structures. We analyse why Bayesian model selection works in situations where methods based on maximum likelihood fail. To demonstrate our approach, we construct a Bayesian non-parametric model that can flexibly model the joint distribution. We then outperform previous methods on a wide range of benchmark datasets with varying data generating assumptions.