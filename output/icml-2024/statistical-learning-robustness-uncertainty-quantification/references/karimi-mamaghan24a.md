---
title: "Challenges and Considerations in the Evaluation of Bayesian Causal Discovery"
source: "https://proceedings.mlr.press/v235/karimi-mamaghan24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/karimi-mamaghan24a/karimi-mamaghan24a.pdf"
categories: ['causal-inference-and-discovery-methods', 'statistical-learning-robustness-uncertainty-quantification']
tags: ['Bayesian-causal-discovery', 'uncertainty-quantification', 'evaluation-challenges']
venue: "ICML 2024"
tldr: "Identifies key challenges and considerations in evaluating Bayesian causal discovery methods that represent uncertainty over causal structures."
---

# Challenges and Considerations in the Evaluation of Bayesian Causal Discovery

**Source**: [https://proceedings.mlr.press/v235/karimi-mamaghan24a.html](https://proceedings.mlr.press/v235/karimi-mamaghan24a.html)

**TLDR**: Identifies key challenges and considerations in evaluating Bayesian causal discovery methods that represent uncertainty over causal structures.

## Abstract

Representing uncertainty in causal discovery is a crucial component for experimental design, and more broadly, for safe and reliable causal decision making. Bayesian Causal Discovery (BCD) offers a principled approach to encapsulating this uncertainty. Unlike non-Bayesian causal discovery, which relies on a single estimated causal graph and model parameters for assessment, evaluating BCD presents challenges due to the nature of its inferred quantity – the posterior distribution. As a result, the research community has proposed various metrics to assess the quality of the approximate posterior. However, there is, to date, no consensus on the most suitable metric(s) for evaluation. In this work, we reexamine this question by dissecting various metrics and understanding their limitations. Through extensive empirical evaluation, we find that many existing metrics fail to exhibit a strong correlation with the quality of approximation to the true posterior, especially in scenarios with low sample sizes where BCD is most desirable. We highlight the suitability (or lack thereof) of these metrics under two distinct factors: the identifiability of the underlying causal model and the quantity of available data. Both factors affect the entropy of the true posterior, indicating that the current metrics are less fitting in settings of higher entropy. Our findings underline the importance of a more nuanced evaluation of new methods by taking into account the nature of the true posterior, as well as guide and motivate the development of new evaluation procedures for this challenge.