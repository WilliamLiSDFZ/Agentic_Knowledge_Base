---
title: "Layer-Aware Analysis of Catastrophic Overfitting: Revealing the Pseudo-Robust Shortcut Dependency"
source: "https://proceedings.mlr.press/v235/lin24v.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/lin24v/lin24v.pdf"
categories: ['adversarial-robustness-and-model-security', 'neural-network-learning-dynamics-theory']
tags: ['catastrophic-overfitting', 'adversarial-training', 'shortcut-learning']
venue: "ICML 2024"
tldr: "A layer-aware analysis of catastrophic overfitting in single-step adversarial training revealing pseudo-robust shortcut dependencies."
---

# Layer-Aware Analysis of Catastrophic Overfitting: Revealing the Pseudo-Robust Shortcut Dependency

**Source**: [https://proceedings.mlr.press/v235/lin24v.html](https://proceedings.mlr.press/v235/lin24v.html)

**TLDR**: A layer-aware analysis of catastrophic overfitting in single-step adversarial training revealing pseudo-robust shortcut dependencies.

## Abstract

Catastrophic overfitting (CO) presents a significant challenge in single-step adversarial training (AT), manifesting as highly distorted deep neural networks (DNNs) that are vulnerable to multi-step adversarial attacks. However, the underlying factors that lead to the distortion of decision boundaries remain unclear. In this work, we delve into the specific changes within different DNN layers and discover that during CO, the former layers are more susceptible, experiencing earlier and greater distortion, while the latter layers show relative insensitivity. Our analysis further reveals that this increased sensitivity in former layers stems from the formation of $\textit{pseudo-robust shortcuts}$, which alone can impeccably defend against single-step adversarial attacks but bypass genuine-robust learning, resulting in distorted decision boundaries. Eliminating these shortcuts can partially restore robustness in DNNs from the CO state, thereby verifying that dependence on them triggers the occurrence of CO. This understanding motivates us to implement adaptive weight perturbations across different layers to hinder the generation of $\textit{pseudo-robust shortcuts}$, consequently mitigating CO. Extensive experiments demonstrate that our proposed method, $\textbf{L}$ayer-$\textbf{A}$ware Adversarial Weight $\textbf{P}$erturbation (LAP), can effectively prevent CO and further enhance robustness.