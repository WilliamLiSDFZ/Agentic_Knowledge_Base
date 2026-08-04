---
title: "Log Neural Controlled Differential Equations: The Lie Brackets Make A Difference"
source: "https://proceedings.mlr.press/v235/walker24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/walker24a/walker24a.pdf"
categories: ['time-series-modeling-and-forecasting-methods', 'sequence-models-for-memory-and-state']
tags: ['neural-CDEs', 'Lie-brackets', 'log-signature', 'time-series', 'controlled-differential-equations']
venue: "ICML 2024"
tldr: "Introduces Log Neural Controlled Differential Equations incorporating Lie bracket terms from log-signatures to improve time series modeling with neural CDEs."
---

# Log Neural Controlled Differential Equations: The Lie Brackets Make A Difference

**Source**: [https://proceedings.mlr.press/v235/walker24a.html](https://proceedings.mlr.press/v235/walker24a.html)

**TLDR**: Introduces Log Neural Controlled Differential Equations incorporating Lie bracket terms from log-signatures to improve time series modeling with neural CDEs.

## Abstract

The vector field of a controlled differential equation (CDE) describes the relationship between a control path and the evolution of a solution path. Neural CDEs (NCDEs) treat time series data as observations from a control path, parameterise a CDE’s vector field using a neural network, and use the solution path as a continuously evolving hidden state. As their formulation makes them robust to irregular sampling rates, NCDEs are a powerful approach for modelling real-world data. Building on neural rough differential equations (NRDEs), we introduce Log-NCDEs, a novel, effective, and efficient method for training NCDEs. The core component of Log-NCDEs is the Log-ODE method, a tool from the study of rough paths for approximating a CDE’s solution. Log-NCDEs are shown to outperform NCDEs, NRDEs, the linear recurrent unit, S5, and MAMBA on a range of multivariate time series datasets with up to $50{,}000$ observations.