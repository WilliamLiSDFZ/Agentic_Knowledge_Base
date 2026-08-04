---
title: "On the Duality Between Sharpness-Aware Minimization and Adversarial Training"
source: "https://proceedings.mlr.press/v235/zhang24w.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/zhang24w/zhang24w.pdf"
categories: ['adversarial-robustness-and-model-security', 'optimization-algorithms-convergence-theory']
tags: ['adversarial-training', 'sharpness-aware-minimization', 'duality']
venue: "ICML 2024"
tldr: "Establishes a formal duality between Sharpness-Aware Minimization and Adversarial Training, revealing their shared geometry and trade-offs."
---

# On the Duality Between Sharpness-Aware Minimization and Adversarial Training

**Source**: [https://proceedings.mlr.press/v235/zhang24w.html](https://proceedings.mlr.press/v235/zhang24w.html)

**TLDR**: Establishes a formal duality between Sharpness-Aware Minimization and Adversarial Training, revealing their shared geometry and trade-offs.

## Abstract

Adversarial Training (AT), which adversarially perturb the input samples during training, has been acknowledged as one of the most effective defenses against adversarial attacks, yet suffers from inevitably decreased clean accuracy. Instead of perturbing the samples, Sharpness-Aware Minimization (SAM) perturbs the model weights during training to find a more flat loss landscape and improve generalization. However, as SAM is designed for better clean accuracy, its effectiveness in enhancing adversarial robustness remains unexplored. In this work, considering the duality between SAM and AT, we investigate the adversarial robustness derived from SAM. Intriguingly, we find that using SAM alone can improve adversarial robustness. To understand this unexpected property of SAM, we first provide empirical and theoretical insights into how SAM can implicitly learn more robust features, and conduct comprehensive experiments to show that SAM can improve adversarial robustness notably without sacrificing any clean accuracy, shedding light on the potential of SAM to be a substitute for AT when accuracy comes at a higher priority. Code is available at https://github.com/weizeming/SAM_AT.