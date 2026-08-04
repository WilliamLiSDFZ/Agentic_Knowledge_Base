---
title: "Rethinking DP-SGD in Discrete Domain: Exploring Logistic Distribution in the Realm of signSGD"
source: "https://proceedings.mlr.press/v235/jang24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/jang24a/jang24a.pdf"
categories: ['privacy-preserving-federated-and-distributed-learning', 'adversarial-robustness-and-model-security']
tags: ['differential-privacy', 'DP-SGD', 'signSGD', 'logistic-distribution', 'membership-inference']
venue: "ICML 2024"
tldr: "This paper proposes replacing Gaussian noise in DP-SGD with logistic distribution noise tailored for signSGD to improve privacy-utility tradeoffs in discrete domains."
---

# Rethinking DP-SGD in Discrete Domain: Exploring Logistic Distribution in the Realm of signSGD

**Source**: [https://proceedings.mlr.press/v235/jang24a.html](https://proceedings.mlr.press/v235/jang24a.html)

**TLDR**: This paper proposes replacing Gaussian noise in DP-SGD with logistic distribution noise tailored for signSGD to improve privacy-utility tradeoffs in discrete domains.

## Abstract

Deep neural networks (DNNs) have a risk of remembering sensitive data from their training datasets, inadvertently leading to substantial information leakage through privacy attacks like membership inference attacks. DP-SGD is a simple but effective defense method, incorporating Gaussian noise into gradient updates to safeguard sensitive information. With the prevalence of large neural networks, DP-signSGD, a variant of DP-SGD, has emerged, aiming to curtail memory usage while maintaining security. However, it is noteworthy that most DP-signSGD algorithms default to Gaussian noise, suitable only for DP-SGD, without scant discussion of its appropriateness for signSGD. Our study delves into an intriguing question: "Can we find a more efficient substitute for Gaussian noise to secure privacy in DP-signSGD?" We propose an answer with a Logistic mechanism, which conforms to signSGD principles and is interestingly evolved from an exponential mechanism. In this paper, we provide both theoretical and experimental evidence showing that our method surpasses DP-signSGD.