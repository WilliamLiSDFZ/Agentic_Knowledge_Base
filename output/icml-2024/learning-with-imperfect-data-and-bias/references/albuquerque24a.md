---
title: "Evaluating Model Bias Requires Characterizing its Mistakes"
source: "https://proceedings.mlr.press/v235/albuquerque24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/albuquerque24a/albuquerque24a.pdf"
categories: ['learning-with-imperfect-data-and-bias', 'anomaly-and-out-of-distribution-detection']
tags: ['model-bias', 'spurious-correlations', 'subgroup-analysis']
venue: "ICML 2024"
tldr: "This paper argues that properly benchmarking model bias requires characterizing the nature of model mistakes across subgroups, not just quantifying error rates."
---

# Evaluating Model Bias Requires Characterizing its Mistakes

**Source**: [https://proceedings.mlr.press/v235/albuquerque24a.html](https://proceedings.mlr.press/v235/albuquerque24a.html)

**TLDR**: This paper argues that properly benchmarking model bias requires characterizing the nature of model mistakes across subgroups, not just quantifying error rates.

## Abstract

The ability to properly benchmark model performance in the face of spurious correlations is important to both build better predictors and increase confidence that models are operating as intended. We demonstrate that characterizing (as opposed to simply quantifying) model mistakes across subgroups is pivotal to properly reflect model biases, which are ignored by standard metrics such as worst-group accuracy or accuracy gap. Inspired by the hypothesis testing framework, we introduce SkewSize, a principled and flexible metric that captures bias from mistakes in a model’s predictions. It can be used in multi-class settings or generalised to the open vocabulary setting of generative models. SkewSize is an aggregation of the effect size of the interaction between two categorical variables: the spurious variable representing the bias attribute the model’s prediction. We demonstrate the utility of SkewSize in multiple settings including: standard vision models trained on synthetic data, vision models trained on ImageNet, and large scale vision-and-language models from the BLIP-2 family. In each case, the proposed SkewSize is able to highlight biases not captured by other metrics, while also providing insights on the impact of recently proposed techniques, such as instruction tuning.