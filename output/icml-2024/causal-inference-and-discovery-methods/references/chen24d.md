---
title: "Feature Attribution with Necessity and Sufficiency via Dual-stage Perturbation Test for Causal Explanation"
source: "https://proceedings.mlr.press/v235/chen24d.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/chen24d/chen24d.pdf"
categories: ['ai-explainability-uncertainty-human-decision-making', 'causal-inference-and-discovery-methods']
tags: ['feature-attribution', 'necessity-sufficiency', 'perturbation-test', 'causal-explanation']
venue: "ICML 2024"
tldr: "A dual-stage perturbation test framework that evaluates feature importance via necessity and sufficiency for causally grounded model explanations."
---

# Feature Attribution with Necessity and Sufficiency via Dual-stage Perturbation Test for Causal Explanation

**Source**: [https://proceedings.mlr.press/v235/chen24d.html](https://proceedings.mlr.press/v235/chen24d.html)

**TLDR**: A dual-stage perturbation test framework that evaluates feature importance via necessity and sufficiency for causally grounded model explanations.

## Abstract

We investigate the problem of explainability for machine learning models, focusing on Feature Attribution Methods (FAMs) that evaluate feature importance through perturbation tests. Despite their utility, FAMs struggle to distinguish the contributions of different features, when their prediction changes are similar after perturbation. To enhance FAMs’ discriminative power, we introduce Feature Attribution with Necessity and Sufficiency (FANS), which find a neighborhood of the input such that perturbing samples within this neighborhood have a high Probability of being Necessity and Sufficiency (PNS) cause for the change in predictions, and use this PNS as the importance of the feature. Specifically, FANS compute this PNS via a heuristic strategy for estimating the neighborhood and a perturbation test involving two stages (factual and interventional) for counterfactual reasoning. To generate counterfactual samples, we use a resampling-based approach on the observed samples to approximate the required conditional distribution. We demonstrate that FANS outperforms existing attribution methods on six benchmarks. Please refer to the source code via https://github.com/DMIRLAB-Group/FANS.