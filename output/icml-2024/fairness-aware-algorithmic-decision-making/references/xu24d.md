---
title: "Intersectional Unfairness Discovery"
source: "https://proceedings.mlr.press/v235/xu24d.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/xu24d/xu24d.pdf"
categories: ['fairness-aware-algorithmic-decision-making']
tags: ['intersectional-fairness', 'subgroup-discovery', 'bias-detection']
venue: "ICML 2024"
tldr: "This work addresses intersectional unfairness by discovering biased subgroups defined by combinations of multiple sensitive attributes in AI systems."
---

# Intersectional Unfairness Discovery

**Source**: [https://proceedings.mlr.press/v235/xu24d.html](https://proceedings.mlr.press/v235/xu24d.html)

**TLDR**: This work addresses intersectional unfairness by discovering biased subgroups defined by combinations of multiple sensitive attributes in AI systems.

## Abstract

AI systems have been shown to produce unfair results for certain subgroups of population, highlighting the need to understand bias on certain sensitive attributes. Current research often falls short, primarily focusing on the subgroups characterized by a single sensitive attribute, while neglecting the nature of intersectional fairness of multiple sensitive attributes. This paper focuses on its one fundamental aspect by discovering diverse high-bias intersectional sensitive attributes. Specifically, we propose a Bias-Guided Generative Network (BGGN). By treating each bias value as a reward, BGGN efficiently generates high-bias intersectional sensitive attributes. Experiments on real-world text and image datasets demonstrate a diverse and efficient discovery of BGGN. To further evaluate the generated unseen but possible unfair intersectional sensitive attributes, we formulate them as prompts and use modern generative AI to produce new text and images. The results of frequently generating biased data provides new insights of discovering potential unfairness in popular modern generative AI systems. Warning: This paper contains examples that are offensive in nature.