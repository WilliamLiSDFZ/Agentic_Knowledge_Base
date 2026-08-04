---
title: "Explaining Probabilistic Models with Distributional Values"
source: "https://proceedings.mlr.press/v235/franceschi24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/franceschi24a/franceschi24a.pdf"
categories: ['ai-explainability-uncertainty-human-decision-making', 'generative-models-and-variational-inference']
tags: ['shapley-values', 'explainability', 'distributional-explanations']
venue: "ICML 2024"
tldr: "Distributional values are proposed as game-theoretic explanations that account for the full output distribution rather than just expectations."
---

# Explaining Probabilistic Models with Distributional Values

**Source**: [https://proceedings.mlr.press/v235/franceschi24a.html](https://proceedings.mlr.press/v235/franceschi24a.html)

**TLDR**: Distributional values are proposed as game-theoretic explanations that account for the full output distribution rather than just expectations.

## Abstract

A large branch of explainable machine learning is grounded in cooperative game theory. However, research indicates that game-theoretic explanations may mislead or be hard to interpret. We argue that often there is a critical mismatch between what one wishes to explain (e.g. the output of a classifier) and what current methods such as SHAP explain (e.g. the scalar probability of a class). This paper addresses such gap for probabilistic models by generalising cooperative games and value operators. We introduce the distributional values, random variables that track changes in the model output (e.g. flipping of the predicted class) and derive their analytic expressions for games with Gaussian, Bernoulli and Categorical payoffs. We further establish several characterising properties, and show that our framework provides fine-grained and insightful explanations with case studies on vision and language models.