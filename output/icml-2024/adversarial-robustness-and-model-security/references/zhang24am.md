---
title: "Improving Accuracy-robustness Trade-off via Pixel Reweighted Adversarial Training"
source: "https://proceedings.mlr.press/v235/zhang24am.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/zhang24am/zhang24am.pdf"
categories: ['adversarial-robustness-and-model-security', 'learning-with-imperfect-data-and-bias']
tags: ['adversarial-training', 'pixel-reweighting', 'accuracy-robustness-tradeoff']
venue: "ICML 2024"
tldr: "Improves the accuracy-robustness trade-off in adversarial training by reweighting adversarial perturbations across pixels based on importance."
---

# Improving Accuracy-robustness Trade-off via Pixel Reweighted Adversarial Training

**Source**: [https://proceedings.mlr.press/v235/zhang24am.html](https://proceedings.mlr.press/v235/zhang24am.html)

**TLDR**: Improves the accuracy-robustness trade-off in adversarial training by reweighting adversarial perturbations across pixels based on importance.

## Abstract

Adversarial training (AT) trains models using adversarial examples (AEs), which are natural images modified with specific perturbations to mislead the model. These perturbations are constrained by a predefined perturbation budget $\epsilon$ and are equally applied to each pixel within an image. However, in this paper, we discover that not all pixels contribute equally to the accuracy on AEs (i.e., robustness) and accuracy on natural images (i.e., accuracy). Motivated by this finding, we propose Pixel-reweighted AdveRsarial Training (PART), a new framework that partially reduces $\epsilon$ for less influential pixels, guiding the model to focus more on key regions that affect its outputs. Specifically, we first use class activation mapping (CAM) methods to identify important pixel regions, then we keep the perturbation budget for these regions while lowering it for the remaining regions when generating AEs. In the end, we use these pixel-reweighted AEs to train a model. PART achieves a notable improvement in accuracy without compromising robustness on CIFAR-10, SVHN and TinyImagenet-200, justifying the necessity to allocate distinct weights to different pixel regions in robust classification.