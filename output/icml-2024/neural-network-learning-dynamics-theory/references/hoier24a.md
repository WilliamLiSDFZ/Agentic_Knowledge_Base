---
title: "Two Tales of Single-Phase Contrastive Hebbian Learning"
source: "https://proceedings.mlr.press/v235/hoier24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/hoier24a/hoier24a.pdf"
categories: ['neural-network-learning-dynamics-theory', 'neuromorphic-computing-and-neural-dynamics-modeling']
tags: ['contrastive-Hebbian-learning', 'biologically-plausible', 'single-phase', 'backpropagation']
venue: "ICML 2024"
tldr: "Proposes a single-phase contrastive Hebbian learning algorithm that avoids explicit phases while approximating gradient-based learning."
---

# Two Tales of Single-Phase Contrastive Hebbian Learning

**Source**: [https://proceedings.mlr.press/v235/hoier24a.html](https://proceedings.mlr.press/v235/hoier24a.html)

**TLDR**: Proposes a single-phase contrastive Hebbian learning algorithm that avoids explicit phases while approximating gradient-based learning.

## Abstract

The search for "biologically plausible" learning algorithms has converged on the idea of representing gradients as activity differences. However, most approaches require a high degree of synchronization (distinct phases during learning) and introduce substantial computational overhead, which raises doubts regarding their biological plausibility as well as their potential utility for neuromorphic computing. Furthermore, they commonly rely on applying infinitesimal perturbations (nudges) to output units, which is impractical in noisy environments. Recently it has been shown that by modelling artificial neurons as dyads with two oppositely nudged compartments, it is possible for a fully local learning algorithm named “dual propagation” to bridge the performance gap to backpropagation, without requiring separate learning phases or infinitesimal nudging. However, the algorithm has the drawback that its numerical stability relies on symmetric nudging, which may be restrictive in biological and analog implementations. In this work we first provide a solid foundation for the objective underlying the dual propagation method, which also reveals a surpising connection with adversarial robustness. Second, we demonstrate how dual propagation is related to a particular adjoint state method, which is stable regardless of asymmetric nudging.