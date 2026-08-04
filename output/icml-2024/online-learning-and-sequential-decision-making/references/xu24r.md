---
title: "Robust Inverse Constrained Reinforcement Learning under Model Misspecification"
source: "https://proceedings.mlr.press/v235/xu24r.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/xu24r/xu24r.pdf"
categories: ['online-learning-and-sequential-decision-making']
tags: ['inverse-constrained-RL', 'model-misspecification', 'safe-RL']
venue: "ICML 2024"
tldr: "This paper develops a robust inverse constrained RL framework that infers safety constraints from expert demonstrations under model misspecification."
---

# Robust Inverse Constrained Reinforcement Learning under Model Misspecification

**Source**: [https://proceedings.mlr.press/v235/xu24r.html](https://proceedings.mlr.press/v235/xu24r.html)

**TLDR**: This paper develops a robust inverse constrained RL framework that infers safety constraints from expert demonstrations under model misspecification.

## Abstract

To solve safety-critical decision-making problems, Inverse Constrained Reinforcement Learning (ICRL) infers constraints from expert demonstrations and seeks to imitate expert preference by utilizing these constraints. While prior ICRL research commonly overlooks the discrepancy between the training and deploying environments, we demonstrate that such a discrepancy can significantly compromise the reliability of the inferred constraints and thus induce unsafe movements. Motivated by this finding, we propose the Robust Constraint Inference (RCI) problem and an Adaptively Robust ICRL (AR-ICRL) algorithm to solve RCI efficiently. Specifically, we model the impact of misspecified dynamics with an opponent policy and learn a robust policy to facilitate safe control in a Markov Game. Subsequently, we adjust our constraint model to align the learned policies to expert demonstrations, accommodating both soft and hard optimality in our behavioral models. Empirical results demonstrate the significance of robust constraints and the effectiveness of the proposed AR-ICRL algorithm under continuous and discrete domains. The code is available at https://github.com/Jasonxu1225/AR-ICRL.