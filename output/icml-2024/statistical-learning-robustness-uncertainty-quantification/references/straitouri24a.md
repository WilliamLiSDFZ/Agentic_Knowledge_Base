---
title: "Designing Decision Support Systems using Counterfactual Prediction Sets"
source: "https://proceedings.mlr.press/v235/straitouri24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/straitouri24a/straitouri24a.pdf"
categories: ['ai-explainability-uncertainty-human-decision-making', 'statistical-learning-robustness-uncertainty-quantification']
tags: ['decision-support', 'counterfactual-prediction-sets', 'conformal-prediction', 'human-AI', 'classification']
venue: "ICML 2024"
tldr: "Decision support systems are designed using counterfactual prediction sets to help human experts understand when and how to update their decisions."
---

# Designing Decision Support Systems using Counterfactual Prediction Sets

**Source**: [https://proceedings.mlr.press/v235/straitouri24a.html](https://proceedings.mlr.press/v235/straitouri24a.html)

**TLDR**: Decision support systems are designed using counterfactual prediction sets to help human experts understand when and how to update their decisions.

## Abstract

Decision support systems for classification tasks are predominantly designed to predict the value of the ground truth labels. However, since their predictions are not perfect, these systems also need to make human experts understand when and how to use these predictions to update their own predictions. Unfortunately, this has been proven challenging. In this context, it has been recently argued that an alternative type of decision support systems may circumvent this challenge. Rather than providing a single label prediction, these systems provide a set of label prediction values constructed using a conformal predictor, namely a prediction set, and forcefully ask experts to predict a label value from the prediction set. However, the design and evaluation of these systems have so far relied on stylized expert models, questioning their promise. In this paper, we revisit the design of this type of systems from the perspective of online learning and develop a methodology that does not require, nor assumes, an expert model. Our methodology leverages the nested structure of the prediction sets provided by any conformal predictor and a natural counterfactual monotonicity assumption to achieve an exponential improvement in regret in comparison to vanilla bandit algorithms. We conduct a large-scale human subject study ($n = 2{,}751$) to compare our methodology to several competitive baselines. The results show that, for decision support systems based on prediction sets, limiting experts’ level of agency leads to greater performance than allowing experts to always exercise their own agency.