---
title: "Estimating the Level of Dialectness Predicts Inter-annotator Agreement in Multi-dialect Arabic Datasets"
source: "https://aclanthology.org/2024.acl-short.70/"
pdf_url: ""
categories: ['language-technology-cultural-linguistic-diversity', 'label-noise-robust-annotation-learning']
tags: ['Arabic-dialects', 'inter-annotator-agreement', 'dialectness-level', 'annotation-quality', 'multi-dialect']
venue: "ACL 2024"
tldr: "Shows that estimating the degree of dialectness in Arabic text predicts inter-annotator agreement, improving multi-dialect dataset annotation routing."
---

# Estimating the Level of Dialectness Predicts Inter-annotator Agreement in Multi-dialect Arabic Datasets

**Source**: [https://aclanthology.org/2024.acl-short.70/](https://aclanthology.org/2024.acl-short.70/)

**TLDR**: Shows that estimating the degree of dialectness in Arabic text predicts inter-annotator agreement, improving multi-dialect dataset annotation routing.

## Abstract

AbstractOn annotating multi-dialect Arabic datasets, it is common to randomly assign the samples across a pool of native Arabic speakers. Recent analyses recommended routing dialectal samples to native speakers of their respective dialects to build higher-quality datasets. However, automatically identifying the dialect of samples is hard. Moreover, the pool of annotators who are native speakers of specific Arabic dialects might be scarce. Arabic Level of Dialectness (ALDi) was recently introduced as a quantitative variable that measures how sentences diverge from Standard Arabic. On randomly assigning samples to annotators, we hypothesize that samples of higher ALDi scores are harder to label especially if they are written in dialects that the annotators do not speak. We test this by analyzing the relation between ALDi scores and the annotators’ agreement, on 15 public datasets having raw individual sample annotations for various sentence-classification tasks. We find strong evidence supporting our hypothesis for 11 of them. Consequently, we recommend prioritizing routing samples of high ALDi scores to native speakers of each sample’s dialect, for which the dialect could be automatically identified at higher accuracies.