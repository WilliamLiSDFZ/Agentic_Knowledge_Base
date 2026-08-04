---
title: "Prometheus: Out-of-distribution Fluid Dynamics Modeling with Disentangled Graph ODE"
source: "https://proceedings.mlr.press/v235/wu24aa.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/wu24aa/wu24aa.pdf"
categories: ['neural-operators-for-pde-solving', 'anomaly-and-out-of-distribution-detection']
tags: ['fluid-dynamics', 'graph-neural-networks', 'ODE', 'out-of-distribution', 'disentangled-representations']
venue: "ICML 2024"
tldr: "Proposes Prometheus, an OOD-robust fluid dynamics model using disentangled graph ODEs for generalizing across distribution shifts in physical simulations."
---

# Prometheus: Out-of-distribution Fluid Dynamics Modeling with Disentangled Graph ODE

**Source**: [https://proceedings.mlr.press/v235/wu24aa.html](https://proceedings.mlr.press/v235/wu24aa.html)

**TLDR**: Proposes Prometheus, an OOD-robust fluid dynamics model using disentangled graph ODEs for generalizing across distribution shifts in physical simulations.

## Abstract

Fluid dynamics modeling has received extensive attention in the machine learning community. Although numerous graph neural network (GNN) approaches have been proposed for this problem, the problem of out-of-distribution (OOD) generalization remains underexplored. In this work, we propose a new large-scale dataset Prometheus which simulates tunnel and pool fires across various environmental conditions and builds an extensive benchmark of 12 baselines, which demonstrates that the OOD generalization performance is far from satisfactory. To tackle this, this paper introduces a new approach named Disentangled Graph ODE (DGODE), which learns disentangled representations for continuous interacting dynamics modeling. In particular, we utilize a temporal GNN and a frequency network to extract semantics from historical trajectories into node representations and environment representations respectively. To mitigate the potential distribution shift, we minimize the mutual information between invariant node representations and the discretized environment features using adversarial learning. Then, they are fed into a coupled graph ODE framework, which models the evolution using neighboring nodes and dynamical environmental context. In addition, we enhance the stability of the framework by perturbing the environment features to enhance robustness. Extensive experiments validate the effectiveness of DGODE compared with state-of-the-art approaches.