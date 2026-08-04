---
title: "Self-Consistency Training for Density-Functional-Theory Hamiltonian Prediction"
source: "https://proceedings.mlr.press/v235/zhang24ak.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/zhang24ak/zhang24ak.pdf"
categories: ['neural-operators-for-pde-solving', 'learning-with-imperfect-data-and-bias']
tags: ['DFT-Hamiltonian', 'self-consistency', 'semi-supervised-learning']
venue: "ICML 2024"
tldr: "Leverages the self-consistency property of DFT Hamiltonians to enable semi-supervised training with unlabeled molecular data."
---

# Self-Consistency Training for Density-Functional-Theory Hamiltonian Prediction

**Source**: [https://proceedings.mlr.press/v235/zhang24ak.html](https://proceedings.mlr.press/v235/zhang24ak.html)

**TLDR**: Leverages the self-consistency property of DFT Hamiltonians to enable semi-supervised training with unlabeled molecular data.

## Abstract

Predicting the mean-field Hamiltonian matrix in density functional theory is a fundamental formulation to leverage machine learning for solving molecular science problems. Yet, its applicability is limited by insufficient labeled data for training. In this work, we highlight that Hamiltonian prediction possesses a self-consistency principle, based on which we propose self-consistency training, an exact training method that does not require labeled data. It distinguishes the task from predicting other molecular properties by the following benefits: (1) it enables the model to be trained on a large amount of unlabeled data, hence addresses the data scarcity challenge and enhances generalization; (2) it is more efficient than running DFT to generate labels for supervised training, since it amortizes DFT calculation over a set of queries. We empirically demonstrate the better generalization in data-scarce and out-of-distribution scenarios, and the better efficiency over DFT labeling. These benefits push forward the applicability of Hamiltonian prediction to an ever-larger scale.