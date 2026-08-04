---
title: "The Pitfalls and Promise of Conformal Inference Under Adversarial Attacks"
source: "https://proceedings.mlr.press/v235/liu24m.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/liu24m/liu24m.pdf"
categories: ['statistical-learning-robustness-uncertainty-quantification']
tags: ['conformal-inference', 'adversarial-robustness', 'uncertainty-quantification']
venue: "ICML 2024"
tldr: "This paper analyzes the pitfalls and potential of conformal prediction under adversarial attacks in safety-critical applications."
---

# The Pitfalls and Promise of Conformal Inference Under Adversarial Attacks

**Source**: [https://proceedings.mlr.press/v235/liu24m.html](https://proceedings.mlr.press/v235/liu24m.html)

**TLDR**: This paper analyzes the pitfalls and potential of conformal prediction under adversarial attacks in safety-critical applications.

## Abstract

In safety-critical applications such as medical imaging and autonomous driving, where decisions have profound implications for patient health and road safety, it is imperative to maintain both high adversarial robustness to protect against potential adversarial attacks and reliable uncertainty quantification in decision-making. With extensive research focused on enhancing adversarial robustness through various forms of adversarial training (AT), a notable knowledge gap remains concerning the uncertainty inherent in adversarially trained models. To address this gap, this study investigates the uncertainty of deep learning models by examining the performance of conformal prediction (CP) in the context of standard adversarial attacks within the adversarial defense community. It is first unveiled that existing CP methods do not produce informative prediction sets under the commonly used $l_{\infty}$-norm bounded attack if the model is not adversarially trained, which underpins the importance of adversarial training for CP. Our paper next demonstrates that the prediction set size (PSS) of CP using adversarially trained models with AT variants is often worse than using standard AT, inspiring us to research into CP-efficient AT for improved PSS. We propose to optimize a Beta-weighting loss with an entropy minimization regularizer during AT to improve CP-efficiency, where the Beta-weighting loss is shown to be an upper bound of PSS at the population level by our theoretical analysis. Moreover, our empirical study on four image classification datasets across three popular AT baselines validates the effectiveness of the proposed Uncertainty-Reducing AT (AT-UR).