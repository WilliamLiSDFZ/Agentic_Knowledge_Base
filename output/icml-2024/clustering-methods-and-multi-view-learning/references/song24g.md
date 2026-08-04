---
title: "Unveiling the Dynamics of Information Interplay in Supervised Learning"
source: "https://proceedings.mlr.press/v235/song24g.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/song24g/song24g.pdf"
categories: ['neural-network-learning-dynamics-theory', 'clustering-methods-and-multi-view-learning']
tags: ['matrix-information-theory', 'neural-collapse', 'supervised-learning', 'representation-dynamics']
venue: "ICML 2024"
tldr: "Matrix mutual information is used to analyze the dynamics of information interplay between data representations and classification heads during supervised learning."
---

# Unveiling the Dynamics of Information Interplay in Supervised Learning

**Source**: [https://proceedings.mlr.press/v235/song24g.html](https://proceedings.mlr.press/v235/song24g.html)

**TLDR**: Matrix mutual information is used to analyze the dynamics of information interplay between data representations and classification heads during supervised learning.

## Abstract

In this paper, we use matrix information theory as an analytical tool to analyze the dynamics of the information interplay between data representations and classification head vectors in the supervised learning process. Specifically, inspired by the theory of Neural Collapse, we introduce matrix mutual information ratio (MIR) and matrix entropy difference ratio (HDR) to assess the interactions of data representation and class classification heads in supervised learning, and we determine the theoretical optimal values for MIR and HDR when Neural Collapse happens. Our experiments show that MIR and HDR can effectively explain many phenomena occurring in neural networks, for example, the standard supervised training dynamics, linear mode connectivity, and the performance of label smoothing and pruning. Additionally, we use MIR and HDR to gain insights into the dynamics of grokking, which is an intriguing phenomenon observed in supervised training, where the model demonstrates generalization capabilities long after it has learned to fit the training data. Furthermore, we introduce MIR and HDR as loss terms in supervised and semi-supervised learning to optimize the information interactions among samples and classification heads. The empirical results provide evidence of the method’s effectiveness, demonstrating that the utilization of MIR and HDR not only aids in comprehending the dynamics throughout the training process but can also enhances the training procedure itself.