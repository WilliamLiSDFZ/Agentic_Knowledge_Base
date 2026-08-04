---
title: "SuDA: Support-based Domain Adaptation for Sim2Real Hinge Joint Tracking with Flexible Sensors"
source: "https://proceedings.mlr.press/v235/jiawei24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/jiawei24a/jiawei24a.pdf"
categories: ['simulation-scaling-limits-for-robot-manipulation', 'test-time-adaptation-methods-and-evaluation']
tags: ['domain-adaptation', 'sim2real', 'flexible-sensors', 'motion-capture']
venue: "ICML 2024"
tldr: "SuDA uses support-based domain adaptation to transfer models trained on simulated data to real flexible sensor measurements for hinge joint tracking."
---

# SuDA: Support-based Domain Adaptation for Sim2Real Hinge Joint Tracking with Flexible Sensors

**Source**: [https://proceedings.mlr.press/v235/jiawei24a.html](https://proceedings.mlr.press/v235/jiawei24a.html)

**TLDR**: SuDA uses support-based domain adaptation to transfer models trained on simulated data to real flexible sensor measurements for hinge joint tracking.

## Abstract

Flexible sensors hold promise for human motion capture (MoCap), offering advantages such as wearability, privacy preservation, and minimal constraints on natural movement. However, existing flexible sensor-based MoCap methods rely on deep learning and necessitate large and diverse labeled datasets for training. These data typically need to be collected in MoCap studios with specialized equipment and substantial manual labor, making them difficult and expensive to obtain at scale. Thanks to the high-linearity of flexible sensors, we address this challenge by proposing a novel Sim2Real solution for hinge joint tracking based on domain adaptation, eliminating the need for labeled data yet achieving comparable accuracy to supervised learning. Our solution relies on a novel Support-based Domain Adaptation method, namely SuDA, which aligns the supports of the predictive functions rather than the instance-dependent distributions between the source and target domains. Extensive experimental results demonstrate the effectiveness of our method and its superiority overstate-of-the-art distribution-based domain adaptation methods in our task.