---
title: "Private Truly-Everlasting Robust-Prediction"
source: "https://proceedings.mlr.press/v235/stemmer24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/stemmer24a/stemmer24a.pdf"
categories: ['privacy-preserving-federated-and-distributed-learning', 'online-learning-and-sequential-decision-making']
tags: ['differential-privacy', 'everlasting-prediction', 'robust-prediction', 'online-learning', 'private-learning']
venue: "ICML 2024"
tldr: "A model for differentially private everlasting robust prediction is proposed where a prediction oracle labels an endless stream without releasing a hypothesis."
---

# Private Truly-Everlasting Robust-Prediction

**Source**: [https://proceedings.mlr.press/v235/stemmer24a.html](https://proceedings.mlr.press/v235/stemmer24a.html)

**TLDR**: A model for differentially private everlasting robust prediction is proposed where a prediction oracle labels an endless stream without releasing a hypothesis.

## Abstract

Private everlasting prediction (PEP), recently introduced by Naor et al. [2023], is a model for differentially private learning in which the learner never publicly releases a hypothesis. Instead, it provides black-box access to a "prediction oracle" that can predict the labels of an endless stream of unlabeled examples drawn from the underlying distribution. Importantly, PEP provides privacy both for the initial training set and for the endless stream of classification queries. We present two conceptual modifications to the definition of PEP, as well as new constructions exhibiting significant improvements over prior work. Specifically, we incorporate robustness against poisoning attacks into the definition of PEP; we present a relaxed privacy definition, suitable for PEP, that allows us to disconnect the privacy parameter $\delta$ from the number of total time steps $T$; and we present new constructions for axis-aligned rectangles and decision-stumps exhibiting improved sample complexity and runtime.