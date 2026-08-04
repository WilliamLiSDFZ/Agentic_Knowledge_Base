---
title: "Quantum Theory and Application of Contextual Optimal Transport"
source: "https://proceedings.mlr.press/v235/mariella24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/mariella24a/mariella24a.pdf"
categories: ['quantum-algorithms-for-machine-learning-optimization']
tags: ['quantum-optimal-transport', 'contextual-OT', 'conditional-distribution']
venue: "ICML 2024"
tldr: "A quantum-theoretic framework for contextual optimal transport that learns conditional transport maps parameterized by covariates."
---

# Quantum Theory and Application of Contextual Optimal Transport

**Source**: [https://proceedings.mlr.press/v235/mariella24a.html](https://proceedings.mlr.press/v235/mariella24a.html)

**TLDR**: A quantum-theoretic framework for contextual optimal transport that learns conditional transport maps parameterized by covariates.

## Abstract

Optimal Transport (OT) has fueled machine learning (ML) across many domains. When paired data measurements $(\boldsymbol{\mu}, \boldsymbol{\nu})$ are coupled to covariates, a challenging conditional distribution learning setting arises. Existing approaches for learning a global transport map parameterized through a potentially unseen context utilize Neural OT and largely rely on Brenier’s theorem. Here, we propose a first-of-its-kind quantum computing formulation for amortized optimization of contextualized transportation plans. We exploit a direct link between doubly stochastic matrices and unitary operators thus unravelling a natural connection between OT and quantum computation. We verify our method (QontOT) on synthetic and real data by predicting variations in cell type distributions conditioned on drug dosage. Importantly we conduct a 24-qubit hardware experiment on a task challenging for classical computers and report a performance that cannot be matched with our classical neural OT approach. In sum, this is a first step toward learning to predict contextualized transportation plans through quantum computing.