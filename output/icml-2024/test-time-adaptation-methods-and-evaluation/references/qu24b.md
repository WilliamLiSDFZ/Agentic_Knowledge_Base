---
title: "Connect Later: Improving Fine-tuning for Robustness with Targeted Augmentations"
source: "https://proceedings.mlr.press/v235/qu24b.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/qu24b/qu24b.pdf"
categories: ['test-time-adaptation-methods-and-evaluation', 'uncertainty-calibration-and-distribution-shift-adaptation']
tags: ['domain-adaptation', 'fine-tuning', 'robustness', 'targeted-augmentations', 'distribution-shift']
venue: "ICML 2024"
tldr: "A fine-tuning strategy using targeted augmentations applied later in training to improve OOD robustness."
---

# Connect Later: Improving Fine-tuning for Robustness with Targeted Augmentations

**Source**: [https://proceedings.mlr.press/v235/qu24b.html](https://proceedings.mlr.press/v235/qu24b.html)

**TLDR**: A fine-tuning strategy using targeted augmentations applied later in training to improve OOD robustness.

## Abstract

Models trained on a labeled source domain often generalize poorly when deployed on an out-of-distribution (OOD) target domain. In the domain adaptation setting where unlabeled target data is available, self-supervised pretraining (e.g., contrastive learning or masked autoencoding) is a promising method to mitigate this performance drop. Pretraining depends on generic data augmentations (e.g., cropping or masking) to learn representations that generalize across domains, which may not work for all distribution shifts. In this paper, we show on real-world tasks that standard fine-tuning after pretraining does not consistently improve OOD error over simply training from scratch on labeled source data. To better leverage pretraining for distribution shifts, we propose the Connect Later framework, which fine-tunes the model with targeted augmentations designed with knowledge of the shift. Intuitively, pretraining learns good representations within the source and target domains, while fine-tuning with targeted augmentations improves generalization across domains. Connect Later achieves state-of-the-art OOD accuracy while maintaining comparable or better in-distribution accuracy on 4 real-world tasks in wildlife identification (iWildCam-WILDS), tumor detection (Camelyon17-WILDS), and astronomy (AstroClassification, Redshifts).