---
title: "Mimicking Better by Matching the Approximate Action Distribution"
source: "https://proceedings.mlr.press/v235/candido-ramos24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/candido-ramos24a/candido-ramos24a.pdf"
categories: ['online-learning-and-sequential-decision-making', 'learning-with-imperfect-data-and-bias']
tags: ['imitation-learning', 'action-distribution-matching', 'on-policy', 'observations']
venue: "ICML 2024"
tldr: "Proposes MAAD, a sample-efficient imitation learning algorithm that matches approximate action distributions from observations without requiring expert actions."
---

# Mimicking Better by Matching the Approximate Action Distribution

**Source**: [https://proceedings.mlr.press/v235/candido-ramos24a.html](https://proceedings.mlr.press/v235/candido-ramos24a.html)

**TLDR**: Proposes MAAD, a sample-efficient imitation learning algorithm that matches approximate action distributions from observations without requiring expert actions.

## Abstract

In this paper, we introduce MAAD, a novel, sample-efficient on-policy algorithm for Imitation Learning from Observations. MAAD utilizes a surrogate reward signal, which can be derived from various sources such as adversarial games, trajectory matching objectives, or optimal transport criteria. To compensate for the non-availability of expert actions, we rely on an inverse dynamics model that infers plausible actions distribution given the expert’s state-state transitions; we regularize the imitator’s policy by aligning it to the inferred action distribution. MAAD leads to significantly improved sample efficiency and stability. We demonstrate its effectiveness in a number of MuJoCo environments, both int the OpenAI Gym and the DeepMind Control Suite. We show that it requires considerable fewer interactions to achieve expert performance, outperforming current state-of-the-art on-policy methods. Remarkably, MAAD often stands out as the sole method capable of attaining expert performance levels, underscoring its simplicity and efficacy.