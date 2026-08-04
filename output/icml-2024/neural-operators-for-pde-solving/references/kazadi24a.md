---
title: "Pluvial Flood Emulation with Hydraulics-informed Message Passing"
source: "https://proceedings.mlr.press/v235/kazadi24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/kazadi24a/kazadi24a.pdf"
categories: ['neural-operators-for-pde-solving', 'graph-neural-networks-and-topology']
tags: ['flood-emulation', 'physics-informed-ML', 'message-passing']
venue: "ICML 2024"
tldr: "Develops a hydraulics-informed message passing neural network for efficient pluvial flood simulation as an alternative to numerical methods."
---

# Pluvial Flood Emulation with Hydraulics-informed Message Passing

**Source**: [https://proceedings.mlr.press/v235/kazadi24a.html](https://proceedings.mlr.press/v235/kazadi24a.html)

**TLDR**: Develops a hydraulics-informed message passing neural network for efficient pluvial flood simulation as an alternative to numerical methods.

## Abstract

Machine Learning (ML) has emerged as a promising alternative to numerical methods for physics-based simulation due to its flexibility and efficiency. Flood modeling is a key case study for ML-based simulation due to its relevance as a tool for supporting preventive and emergency measures to mitigate flood risks. However, the complexity of the topography or domain (ground elevation) and the sparsity of the time-evolving precipitations (external forcing) can be challenging for most existing ML approaches for simulating flooding processes in space and time. Another critical challenge is incorporating physics domain knowledge (hydraulics) into these data-driven models. This paper addresses these challenges by introducing a hydraulics-informed graph neural network for flood simulation. Given a (geographical) region and precipitation data, our model predicts water depths in an auto-regressive fashion. We propose a message-passing framework inspired by the conservation of momentum and mass expressed in the shallow-water equations, which describe the physical process of a flooding event. Empirical results on a dataset covering 9 regions and 7 historical precipitation events demonstrate that our model outperforms the best baseline, and can capture the propagation of water flow more effectively, especially at the very early stage of the flooding event when the amount of water in the domain is scarce. Differently from some of the most recent methods for ML-based simulation, which tend to work well only when the domain is a smooth surface (e.g., flat terrain), we show that our solution achieves accurate results for real ground elevation data.