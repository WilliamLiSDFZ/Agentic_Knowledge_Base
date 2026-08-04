---
title: "Trust Regions for Explanations via Black-Box Probabilistic Certification"
source: "https://proceedings.mlr.press/v235/dhurandhar24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/dhurandhar24a/dhurandhar24a.pdf"
categories: ['ai-explainability-uncertainty-human-decision-making', 'adversarial-robustness-and-model-security']
tags: ['explainability', 'black-box-certification', 'probabilistic-explanation', 'trust-regions', 'robustness']
venue: "ICML 2024"
tldr: "Introduces black-box probabilistic certification of explanations to define trust regions where explanations remain valid for ML model decisions."
---

# Trust Regions for Explanations via Black-Box Probabilistic Certification

**Source**: [https://proceedings.mlr.press/v235/dhurandhar24a.html](https://proceedings.mlr.press/v235/dhurandhar24a.html)

**TLDR**: Introduces black-box probabilistic certification of explanations to define trust regions where explanations remain valid for ML model decisions.

## Abstract

Given the black box nature of machine learning models, a plethora of explainability methods have been developed to decipher the factors behind individual decisions. In this paper, we introduce a novel problem of black box (probabilistic) explanation certification. We ask the question: Given a black box model with only query access, an explanation for an example and a quality metric (viz. fidelity, stability), can we find the largest hypercube (i.e., $\ell_{\infty}$ ball) centered at the example such that when the explanation is applied to all examples within the hypercube, (with high probability) a quality criterion is met (viz. fidelity greater than some value)? Being able to efficiently find such a trust region has multiple benefits: i) insight into model behavior in a region, with a guarantee; ii) ascertained stability of the explanation; iii) explanation reuse, which can save time, energy and money by not having to find explanations for every example; and iv) a possible meta-metric to compare explanation methods. Our contributions include formalizing this problem, proposing solutions, providing theoretical guarantees for these solutions that are computable, and experimentally showing their efficacy on synthetic and real data.