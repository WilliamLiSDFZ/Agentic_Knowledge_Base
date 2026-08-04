---
title: "Enhancing Trajectory Prediction through Self-Supervised Waypoint Distortion Prediction"
source: "https://proceedings.mlr.press/v235/chib24b.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/chib24b/chib24b.pdf"
categories: ['time-series-modeling-and-forecasting-methods', 'knowledge-distillation-methods-and-applications']
tags: ['trajectory-prediction', 'self-supervised-learning', 'knowledge-distillation']
venue: "ICML 2024"
tldr: "A self-supervised waypoint distortion prediction auxiliary task is proposed to improve trajectory prediction through better motion representation learning."
---

# Enhancing Trajectory Prediction through Self-Supervised Waypoint Distortion Prediction

**Source**: [https://proceedings.mlr.press/v235/chib24b.html](https://proceedings.mlr.press/v235/chib24b.html)

**TLDR**: A self-supervised waypoint distortion prediction auxiliary task is proposed to improve trajectory prediction through better motion representation learning.

## Abstract

Trajectory prediction is an important task that involves modeling the indeterminate nature of agents to forecast future trajectories given the observed trajectory sequences. The task of predicting trajectories poses significant challenges, as agents not only move individually through time but also interact spatially. The learning of complex spatio-temporal representations stands as a fundamental challenge in trajectory prediction. To this end, we propose a novel approach called SSWDP (Self-Supervised Waypoint Distortion Prediction). We propose a simple yet highly effective self-supervised task of predicting distortion present in the observed trajectories to improve the representation learning of the model. Our approach can complement existing trajectory prediction methods. The experimental results highlight a significant improvement with relative percentage differences of 22.7%/38.9%, 33.8%/36.4%, and 16.60%/23.20% in ADE/FDE for the NBA, TrajNet++, and ETH-UCY datasets, respectively, compared to the baseline methods. Our approach also demonstrates a significant improvement over baseline methods with relative percentage differences of 76.8%/82.5% and 61.0%/36.1% in ADE/FDE for TrajNet++ and NBA datasets in distorted environments, respectively.