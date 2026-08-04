---
title: "Performative Prediction with Bandit Feedback: Learning through Reparameterization"
source: "https://proceedings.mlr.press/v235/chen24al.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/chen24al/chen24al.pdf"
categories: ['online-learning-and-sequential-decision-making', 'strategic-information-manipulation-and-classification']
tags: ['performative-prediction', 'bandit-feedback', 'distribution-shift', 'reparameterization']
venue: "ICML 2024"
tldr: "Extends performative prediction to settings with bandit feedback and unknown distribution maps via reparameterization-based learning."
---

# Performative Prediction with Bandit Feedback: Learning through Reparameterization

**Source**: [https://proceedings.mlr.press/v235/chen24al.html](https://proceedings.mlr.press/v235/chen24al.html)

**TLDR**: Extends performative prediction to settings with bandit feedback and unknown distribution maps via reparameterization-based learning.

## Abstract

Performative prediction, as introduced by Perdomo et al., is a framework for studying social prediction in which the data distribution itself changes in response to the deployment of a model. Existing work in this field usually hinges on three assumptions that are easily violated in practice: that the performative risk is convex over the deployed model, that the mapping from the model to the data distribution is known to the model designer in advance, and the first-order information of the performative risk is available. In this paper, we initiate the study of performative prediction problems that do not require these assumptions. Specifically, we develop a parameterization framework that parametrizes the performative prediction objective as a function of the induced data distribution. We also develop a two-level zeroth-order optimization procedure, where the first level performs iterative optimization on the distribution parameter space, and the second level learns the model that induced a particular target distribution parameter at each iteration. Under mild conditions, this reparameterization allows us to transform the non-convex objective into a convex one and achieve provable regret guarantees. In particular, we provide a regret bound that is sublinear in the total number of performative samples taken and is only polynomial in the dimension of the model parameter.