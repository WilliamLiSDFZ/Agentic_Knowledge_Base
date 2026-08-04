---
title: "Limited Preference Aided Imitation Learning from Imperfect Demonstrations"
source: "https://proceedings.mlr.press/v235/cao24b.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/cao24b/cao24b.pdf"
categories: ['learning-with-imperfect-data-and-bias', 'online-learning-and-sequential-decision-making']
tags: ['imitation-learning', 'imperfect-demonstrations', 'preference-learning', 'sequential-decision-making']
venue: "ICML 2024"
tldr: "Combines limited human preference feedback with imperfect demonstrations to improve imitation learning in the absence of optimal expert data."
---

# Limited Preference Aided Imitation Learning from Imperfect Demonstrations

**Source**: [https://proceedings.mlr.press/v235/cao24b.html](https://proceedings.mlr.press/v235/cao24b.html)

**TLDR**: Combines limited human preference feedback with imperfect demonstrations to improve imitation learning in the absence of optimal expert data.

## Abstract

Imitation learning mimics high-quality policies from expert data for sequential decision-making tasks. However, its efficacy is hindered in scenarios where optimal demonstrations are unavailable, and only imperfect demonstrations are present. To address this issue, introducing additional limited human preferences is a suitable approach as it can be obtained in a human-friendly manner, offering a promising way to learn the policy that exceeds the performance of imperfect demonstrations. In this paper, we propose a novel imitation learning (IL) algorithm, Preference Aided Imitation Learning from imperfect demonstrations (PAIL). Specifically, PAIL learns a preference reward by querying experts for limited preferences from imperfect demonstrations. This serves two purposes during training: 1) Reweighting imperfect demonstrations with the preference reward for higher quality. 2) Selecting explored trajectories with high cumulative preference rewards to augment imperfect demonstrations. The dataset with continuously improving quality empowers the performance of PAIL to transcend the initial demonstrations. Comprehensive empirical results across a synthetic task and two locomotion benchmarks show that PAIL surpasses baselines by 73.2% and breaks through the performance bottleneck of imperfect demonstrations.