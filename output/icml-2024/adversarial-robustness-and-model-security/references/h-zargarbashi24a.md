---
title: "Robust Yet Efficient Conformal Prediction Sets"
source: "https://proceedings.mlr.press/v235/h-zargarbashi24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/h-zargarbashi24a/h-zargarbashi24a.pdf"
categories: ['statistical-learning-robustness-uncertainty-quantification', 'adversarial-robustness-and-model-security']
tags: ['conformal-prediction', 'adversarial-robustness', 'prediction-sets', 'poisoning', 'evasion']
venue: "ICML 2024"
tldr: "Derives robust and efficient conformal prediction sets that are resistant to both evasion and poisoning adversarial attacks."
---

# Robust Yet Efficient Conformal Prediction Sets

**Source**: [https://proceedings.mlr.press/v235/h-zargarbashi24a.html](https://proceedings.mlr.press/v235/h-zargarbashi24a.html)

**TLDR**: Derives robust and efficient conformal prediction sets that are resistant to both evasion and poisoning adversarial attacks.

## Abstract

Conformal prediction (CP) can convert any model’s output into prediction sets guaranteed to include the true label with any user-specified probability. However, same as the model itself, CP is vulnerable to adversarial test examples (evasion) and perturbed calibration data (poisoning). We derive provably robust sets by bounding the worst-case change in conformity scores. Our tighter bounds lead to more efficient sets. We cover both continuous and discrete (sparse) data and our guarantees work both for evasion and poisoning attacks (on both features and labels).