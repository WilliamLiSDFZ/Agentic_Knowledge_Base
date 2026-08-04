---
title: "Data Poisoning Attacks against Conformal Prediction"
source: "https://proceedings.mlr.press/v235/li24l.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/li24l/li24l.pdf"
categories: ['adversarial-robustness-and-model-security', 'statistical-learning-robustness-uncertainty-quantification']
tags: ['data-poisoning', 'conformal-prediction', 'adversarial-attacks', 'uncertainty-quantification', 'distribution-free']
venue: "ICML 2024"
tldr: "Investigates data poisoning attacks against conformal prediction methods, revealing vulnerabilities in their distribution-free uncertainty guarantees."
---

# Data Poisoning Attacks against Conformal Prediction

**Source**: [https://proceedings.mlr.press/v235/li24l.html](https://proceedings.mlr.press/v235/li24l.html)

**TLDR**: Investigates data poisoning attacks against conformal prediction methods, revealing vulnerabilities in their distribution-free uncertainty guarantees.

## Abstract

The efficient and theoretically sound uncertainty quantification is crucial for building trust in deep learning models. This has spurred a growing interest in conformal prediction (CP), a powerful technique that provides a model-agnostic and distribution-free method for obtaining conformal prediction sets with theoretical guarantees. However, the vulnerabilities of such CP methods with regard to dedicated data poisoning attacks have not been studied previously. To bridge this gap, for the first time, we in this paper propose a new class of black-box data poisoning attacks against CP, where the adversary aims to cause the desired manipulations of some specific examples’ prediction uncertainty results (instead of misclassifications). Additionally, we design novel optimization frameworks for our proposed attacks. Further, we conduct extensive experiments to validate the effectiveness of our attacks on various settings (e.g., the full and split CP settings). Notably, our extensive experiments show that our attacks are more effective in manipulating uncertainty results than traditional poisoning attacks that aim at inducing misclassifications, and existing defenses against conventional attacks are ineffective against our proposed attacks.