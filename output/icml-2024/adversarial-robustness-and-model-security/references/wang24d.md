---
title: "Adversarially Robust Hypothesis Transfer Learning"
source: "https://proceedings.mlr.press/v235/wang24d.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/wang24d/wang24d.pdf"
categories: ['adversarial-robustness-and-model-security', 'learning-with-imperfect-data-and-bias']
tags: ['adversarial-robustness', 'transfer-learning', 'hypothesis-transfer', 'distribution-shift', 'minimax']
venue: "ICML 2024"
tldr: "This work studies hypothesis transfer learning under adversarial attacks, deriving robust transfer learning bounds with auxiliary hypotheses."
---

# Adversarially Robust Hypothesis Transfer Learning

**Source**: [https://proceedings.mlr.press/v235/wang24d.html](https://proceedings.mlr.press/v235/wang24d.html)

**TLDR**: This work studies hypothesis transfer learning under adversarial attacks, deriving robust transfer learning bounds with auxiliary hypotheses.

## Abstract

In this work, we explore Hypothesis Transfer Learning (HTL) under adversarial attacks. In this setting, a learner has access to a training dataset of size $n$ from an underlying distribution $\mathcal{D}$ and a set of auxiliary hypotheses. These auxiliary hypotheses, which can be viewed as prior information originating either from expert knowledge or as pre-trained foundation models, are employed as an initialization for the learning process. Our goal is to develop an adversarially robust model for $\mathcal{D}$. We begin by examining an adversarial variant of the regularized empirical risk minimization learning rule that we term A-RERM. Assuming a non-negative smooth loss function with a strongly convex regularizer, we establish a bound on the robust generalization error of the hypothesis returned by A-RERM in terms of the robust empirical loss and the quality of the initialization. If the initialization is good, i.e., there exists a weighted combination of auxiliary hypotheses with a small robust population loss, the bound exhibits a fast rate of $\mathcal{O}(1/n)$. Otherwise, we get the standard rate of $\mathcal{O}(1/\sqrt{n})$. Additionally, we provide a bound on the robust excess risk which is similar in nature, albeit with a slightly worse rate. We also consider solving the problem using a practical variant, namely proximal stochastic adversarial training, and present a bound that depends on the initialization. This bound has the same dependence on the sample size as the ARERM bound, except for an additional term that depends on the size of the adversarial perturbation.