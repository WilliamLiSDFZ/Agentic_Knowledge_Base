---
title: "Stability Evaluation through Distributional Perturbation Analysis"
source: "https://proceedings.mlr.press/v235/blanchet24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/blanchet24a/blanchet24a.pdf"
categories: ['uncertainty-calibration-and-distribution-shift-adaptation', 'statistical-learning-robustness-uncertainty-quantification']
tags: ['distributional-robustness', 'stability-evaluation', 'out-of-distribution', 'perturbation-analysis']
venue: "ICML 2024"
tldr: "This paper proposes a stability evaluation criterion based on minimal distributional perturbations needed to degrade model performance significantly."
---

# Stability Evaluation through Distributional Perturbation Analysis

**Source**: [https://proceedings.mlr.press/v235/blanchet24a.html](https://proceedings.mlr.press/v235/blanchet24a.html)

**TLDR**: This paper proposes a stability evaluation criterion based on minimal distributional perturbations needed to degrade model performance significantly.

## Abstract

The performance of learning models often deteriorates when deployed in out-of-sample environments. To ensure reliable deployment, we propose a stability evaluation criterion based on distributional perturbations. Conceptually, our stability evaluation criterion is defined as the minimal perturbation required on our observed dataset to induce a prescribed deterioration in risk evaluation. In this paper, we utilize the optimal transport (OT) discrepancy with moment constraints on the (sample, density) space to quantify this perturbation. Therefore, our stability evaluation criterion can address both data corruptions and sub-population shifts—the two most common types of distribution shifts in real-world scenarios. To further realize practical benefits, we present a series of tractable convex formulations and computational methods tailored to different classes of loss functions. The key technical tool to achieve this is the strong duality theorem provided in this paper. Empirically, we validate the practical utility of our stability evaluation criterion across a host of real-world applications. These empirical studies showcase the criterion’s ability not only to compare the stability of different learning models and features but also to provide valuable guidelines and strategies to further improve models.