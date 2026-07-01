---
title: "Enhancing Robustness of Last Layer Two-Stage Fair Model Corrections"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/fba9133d7fa896ab9414ddd1a6b1ecbf-Abstract-Conference.html"
categories: ['fairness-aware-machine-learning-methods', 'machine-learning-theory-and-evaluation-methods']
tags: ['last-layer-retraining', 'subgroup-fairness', 'robustness']
venue: "NeurIPS 2024"
tldr: "A more robust two-stage last-layer correction framework for improving subgroup fairness in pre-trained models with and without group membership information."
---

# Enhancing Robustness of Last Layer Two-Stage Fair Model Corrections

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/fba9133d7fa896ab9414ddd1a6b1ecbf-Abstract-Conference.html](https://papers.nips.cc/paper_files/paper/2024/hash/fba9133d7fa896ab9414ddd1a6b1ecbf-Abstract-Conference.html)

**TLDR**: A more robust two-stage last-layer correction framework for improving subgroup fairness in pre-trained models with and without group membership information.

## Abstract

Last-layer retraining methods have emerged as an efficient framework for correcting existing base models. Within this framework, several methods have been proposed to deal with correcting models for subgroup fairness with and without group membership information. Importantly, prior work has demonstrated that many methods are susceptible to noisy labels. To this end, we propose a drop-in correction for label noise in last-layer retraining, and demonstrate that it achieves state-of-the-art worst-group accuracy for a broad range of symmetric label noise and across a wide variety of datasets exhibiting spurious correlations. Our proposed approach uses label spreading on a latent nearest neighbors graph and has minimal computational overhead compared to existing methods.