---
title: "SeMOPO: Learning High-quality Model and Policy from Low-quality Offline Visual Datasets"
source: "https://proceedings.mlr.press/v235/wan24b.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/wan24b/wan24b.pdf"
categories: ['online-learning-and-sequential-decision-making', 'generative-models-and-variational-inference']
tags: ['offline-RL', 'model-based-RL', 'visual-observations', 'distribution-shift', 'image-based-control']
venue: "ICML 2024"
tldr: "Proposes SeMOPO, a model-based offline RL method that learns high-quality models and policies from low-quality visual datasets by addressing distribution shift."
---

# SeMOPO: Learning High-quality Model and Policy from Low-quality Offline Visual Datasets

**Source**: [https://proceedings.mlr.press/v235/wan24b.html](https://proceedings.mlr.press/v235/wan24b.html)

**TLDR**: Proposes SeMOPO, a model-based offline RL method that learns high-quality models and policies from low-quality visual datasets by addressing distribution shift.

## Abstract

Model-based offline reinforcement Learning (RL) is a promising approach that leverages existing data effectively in many real-world applications, especially those involving high-dimensional inputs like images and videos. To alleviate the distribution shift issue in offline RL, existing model-based methods heavily rely on the uncertainty of learned dynamics. However, the model uncertainty estimation becomes significantly biased when observations contain complex distractors with non-trivial dynamics. To address this challenge, we propose a new approach - Separated Model-based Offline Policy Optimization (SeMOPO) - decomposing latent states into endogenous and exogenous parts via conservative sampling and estimating model uncertainty on the endogenous states only. We provide a theoretical guarantee of model uncertainty and performance bound of SeMOPO. To assess the efficacy, we construct the Low-Quality Vision Deep Data-Driven Datasets for RL (LQV-D4RL), where the data are collected by non-expert policy and the observations include moving distractors. Experimental results show that our method substantially outperforms all baseline methods, and further analytical experiments validate the critical designs in our method. The project website is https://sites.google.com/view/semopo.