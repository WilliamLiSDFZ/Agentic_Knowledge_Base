---
title: "How Far Can Fairness Constraints Help Recover From Biased Data?"
source: "https://proceedings.mlr.press/v235/sharma24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/sharma24a/sharma24a.pdf"
categories: ['fairness-aware-algorithmic-decision-making', 'learning-with-imperfect-data-and-bias']
tags: ['fairness-constraints', 'biased-data', 'equal-opportunity']
venue: "ICML 2024"
tldr: "This paper analyzes how fairness constraints with equal opportunity can recover near-optimal accuracy even from extremely biased data under certain conditions."
---

# How Far Can Fairness Constraints Help Recover From Biased Data?

**Source**: [https://proceedings.mlr.press/v235/sharma24a.html](https://proceedings.mlr.press/v235/sharma24a.html)

**TLDR**: This paper analyzes how fairness constraints with equal opportunity can recover near-optimal accuracy even from extremely biased data under certain conditions.

## Abstract

A general belief in fair classification is that fairness constraints incur a trade-off with accuracy, which biased data may worsen. Contrary to this belief, Blum & Stangl (2019) show that fair classification with equal opportunity constraints even on extremely biased data can recover optimally accurate and fair classifiers on the original data distribution. Their result is interesting because it demonstrates that fairness constraints can implicitly rectify data bias and simultaneously overcome a perceived fairness-accuracy trade-off. Their data bias model simulates under-representation and label bias in underprivileged population, and they show the above result on a stylized data distribution with i.i.d. label noise, under simple conditions on the data distribution and bias parameters. We propose a general approach to extend the result of Blum & Stangl (2019) to different fairness constraints, data bias models, data distributions, and hypothesis classes. We strengthen their result, and extend it to the case when their stylized distribution has labels with Massart noise instead of i.i.d. noise. We prove a similar recovery result for arbitrary data distributions using fair reject option classifiers. We further generalize it to arbitrary data distributions and arbitrary hypothesis classes, i.e., we prove that for any data distribution, if the optimally accurate classifier in a given hypothesis class is fair and robust, then it can be recovered through fair classification with equal opportunity constraints on the biased distribution whenever the bias parameters satisfy certain simple conditions. Finally, we show applications of our technique to time-varying data bias in classification and fair machine learning pipelines.