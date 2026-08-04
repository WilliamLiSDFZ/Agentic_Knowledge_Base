---
title: "MS-TIP: Imputation Aware Pedestrian Trajectory Prediction"
source: "https://proceedings.mlr.press/v235/chib24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/chib24a/chib24a.pdf"
categories: ['time-series-modeling-and-forecasting-methods', 'learning-with-imperfect-data-and-bias']
tags: ['trajectory-prediction', 'missing-data', 'imputation']
venue: "ICML 2024"
tldr: "A trajectory prediction framework that explicitly models and handles missing observations in pedestrian trajectory sequences."
---

# MS-TIP: Imputation Aware Pedestrian Trajectory Prediction

**Source**: [https://proceedings.mlr.press/v235/chib24a.html](https://proceedings.mlr.press/v235/chib24a.html)

**TLDR**: A trajectory prediction framework that explicitly models and handles missing observations in pedestrian trajectory sequences.

## Abstract

Pedestrian trajectory prediction aims to predict future trajectories based on observed trajectories. Current state-of-the-art methods often assume that the observed sequences of agents are complete, which is a strong assumption that overlooks inherent uncertainties. Understanding pedestrian behavior when dealing with missing values in the observed sequence is crucial for enhancing the performance of predictive models. In this work, we propose the MultiScale hypergraph for Trajectory Imputation and Prediction (MS-TIP), a novel approach that simultaneously addresses the imputation of missing observations and the prediction of future trajectories. Specifically, we leverage transformers with diagonal masked self-attention to impute incomplete observations. Further, our approach promotes complex interaction modeling through multi-scale hypergraphs, optimizing our trajectory prediction module to capture different types of interactions. With the inclusion of scenic attention, we learn contextual scene information, instead of sole reliance on coordinates. Additionally, our approach utilizes an intermediate control point and refinement module to infer future trajectories accurately. Extensive experiments validate the efficacy of MS-TIP in precisely predicting pedestrian future trajectories. Code is publicly available at https://github.com/Pranav-chib/MS-TIP.