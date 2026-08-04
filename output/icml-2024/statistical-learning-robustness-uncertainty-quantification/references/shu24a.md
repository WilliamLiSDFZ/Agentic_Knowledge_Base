---
title: "Effects of Exponential Gaussian Distribution on (Double Sampling) Randomized Smoothing"
source: "https://proceedings.mlr.press/v235/shu24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/shu24a/shu24a.pdf"
categories: ['adversarial-robustness-and-model-security', 'statistical-learning-robustness-uncertainty-quantification']
tags: ['randomized-smoothing', 'certified-robustness', 'adversarial-defense']
venue: "ICML 2024"
tldr: "Studies the effect of exponential Gaussian smoothing distributions on randomized smoothing certification, including double sampling variants."
---

# Effects of Exponential Gaussian Distribution on (Double Sampling) Randomized Smoothing

**Source**: [https://proceedings.mlr.press/v235/shu24a.html](https://proceedings.mlr.press/v235/shu24a.html)

**TLDR**: Studies the effect of exponential Gaussian smoothing distributions on randomized smoothing certification, including double sampling variants.

## Abstract

Randomized Smoothing (RS) is currently a scalable certified defense method providing robustness certification against adversarial examples. Although significant progress has been achieved in providing defenses against $\ell_p$ adversaries, the interaction between the smoothing distribution and the robustness certification still remains vague. In this work, we comprehensively study the effect of two families of distributions, named Exponential Standard Gaussian (ESG) and Exponential General Gaussian (EGG) distributions, on Randomized Smoothing and Double Sampling Randomized Smoothing (DSRS). We derive an analytic formula for ESG’s certified radius, which converges to the origin formula of RS as the dimension $d$ increases. Additionally, we prove that EGG can provide tighter constant factors than DSRS in providing $\Omega(\sqrt{d})$ lower bounds of $\ell_2$ certified radius, and thus further addresses the curse of dimensionality in RS. Our experiments on real-world datasets confirm our theoretical analysis of the ESG distributions, that they provide almost the same certification under different exponents $\eta$ for both RS and DSRS. In addition, EGG brings a significant improvement to the DSRS certification, but the mechanism can be different when the classifier properties are different. Compared to the primitive DSRS, the increase in certified accuracy provided by EGG is prominent, up to 6.4% on ImageNet.