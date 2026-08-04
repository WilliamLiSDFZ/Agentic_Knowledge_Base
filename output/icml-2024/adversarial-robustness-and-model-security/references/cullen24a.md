---
title: "Et Tu Certifications: Robustness Certificates Yield Better Adversarial Examples"
source: "https://proceedings.mlr.press/v235/cullen24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/cullen24a/cullen24a.pdf"
categories: ['adversarial-robustness-and-model-security', 'statistical-learning-robustness-uncertainty-quantification']
tags: ['adversarial-examples', 'robustness-certification', 'neural-networks']
venue: "ICML 2024"
tldr: "Shows that robustness certifications can be exploited to generate stronger adversarial examples, undermining the models they aim to protect."
---

# Et Tu Certifications: Robustness Certificates Yield Better Adversarial Examples

**Source**: [https://proceedings.mlr.press/v235/cullen24a.html](https://proceedings.mlr.press/v235/cullen24a.html)

**TLDR**: Shows that robustness certifications can be exploited to generate stronger adversarial examples, undermining the models they aim to protect.

## Abstract

In guaranteeing the absence of adversarial examples in an instance’s neighbourhood, certification mechanisms play an important role in demonstrating neural net robustness. In this paper, we ask if these certifications can compromise the very models they help to protect? Our new Certification Aware Attack exploits certifications to produce computationally efficient norm-minimising adversarial examples $74$% more often than comparable attacks, while reducing the median perturbation norm by more than $10$%. While these attacks can be used to assess the tightness of certification bounds, they also highlight that releasing certifications can paradoxically reduce security.