---
title: "SSL4Q: Semi-Supervised Learning of Quantum Data with Application to Quantum State Classification"
source: "https://proceedings.mlr.press/v235/tang24i.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/tang24i/tang24i.pdf"
categories: ['quantum-algorithms-for-machine-learning-optimization', 'learning-with-imperfect-data-and-bias']
tags: ['quantum-state-classification', 'semi-supervised-learning', 'quantum-measurements']
venue: "ICML 2024"
tldr: "A semi-supervised learning framework for classifying quantum states from measurement statistics, reducing reliance on extensive labeled quantum data."
---

# SSL4Q: Semi-Supervised Learning of Quantum Data with Application to Quantum State Classification

**Source**: [https://proceedings.mlr.press/v235/tang24i.html](https://proceedings.mlr.press/v235/tang24i.html)

**TLDR**: A semi-supervised learning framework for classifying quantum states from measurement statistics, reducing reliance on extensive labeled quantum data.

## Abstract

The accurate classification of quantum states is crucial for advancing quantum computing, as it allows for the effective analysis and correct functioning of quantum devices by analyzing the statistics of the data from quantum measurements. Traditional supervised methods, which rely on extensive labeled measurement outcomes, are used to categorize unknown quantum states with different properties. However, the labeling process demands computational and memory resources that increase exponentially with the number of qubits. We propose SSL4Q, manage to achieve (for the first time) semi-supervised learning specifically designed for quantum state classification. SSL4Q’s architecture is tailored to ensure permutation invariance for unordered quantum measurements and maintain robustness in the face of measurement uncertainties. Our empirical studies encompass simulations on two types of quantum systems: the Heisenberg Model and the Variational Quantum Circuit (VQC) Model, with system size reaching up to 50 qubits. The numerical results demonstrate SSL4Q’s superiority over traditional supervised models in scenarios with limited labels, highlighting its potential in efficiently classifying quantum states with reduced computational and resource overhead.