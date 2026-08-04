---
title: "Privacy Profiles for Private Selection"
source: "https://proceedings.mlr.press/v235/koskela24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/koskela24a/koskela24a.pdf"
categories: ['privacy-preserving-federated-and-distributed-learning', 'statistical-learning-robustness-uncertainty-quantification']
tags: ['differential-privacy', 'private-selection', 'privacy-profiles', 'Report-Noisy-Max', 'Sparse-Vector']
venue: "ICML 2024"
tldr: "Improved privacy profile analysis for private selection mechanisms like Report Noisy Max and Sparse Vector Technique."
---

# Privacy Profiles for Private Selection

**Source**: [https://proceedings.mlr.press/v235/koskela24a.html](https://proceedings.mlr.press/v235/koskela24a.html)

**TLDR**: Improved privacy profile analysis for private selection mechanisms like Report Noisy Max and Sparse Vector Technique.

## Abstract

Private selection mechanisms (e.g., Report Noisy Max, Sparse Vector) are fundamental primitives of differentially private (DP) data analysis with wide applications to private query release, voting, and hyperparameter tuning. Recent work (Liu and Talwar, 2019; Papernot and Steinke, 2022) has made significant progress in both generalizing private selection mechanisms and tightening their privacy analysis using modern numerical privacy accounting tools, e.g., Rényi DP. But Rényi DP is known to be lossy when $(\epsilon,\delta)$-DP is ultimately needed, and there is a trend to close the gap by directly handling privacy profiles, i.e., $\delta$ as a function of $\epsilon$ or its equivalent dual form known as $f$-DPs. In this paper, we work out an easy-to-use recipe that bounds the privacy profiles of ReportNoisyMax and PrivateTuning using the privacy profiles of the base algorithms they corral. Numerically, our approach improves over the RDP-based accounting in all regimes of interest and leads to substantial benefits in end-to-end private learning experiments. Our analysis also suggests new distributions, e.g., binomial distribution for randomizing the number of rounds that leads to more substantial improvements in certain regimes.