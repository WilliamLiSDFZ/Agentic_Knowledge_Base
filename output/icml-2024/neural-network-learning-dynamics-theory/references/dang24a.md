---
title: "Neural Collapse for Cross-entropy Class-Imbalanced Learning with Unconstrained ReLU Features Model"
source: "https://proceedings.mlr.press/v235/dang24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/dang24a/dang24a.pdf"
categories: ['neural-network-learning-dynamics-theory', 'learning-with-imperfect-data-and-bias']
tags: ['neural-collapse', 'class-imbalance', 'cross-entropy', 'ReLU-networks', 'deep-learning-theory']
venue: "ICML 2024"
tldr: "Analyzes neural collapse under class-imbalanced training using an unconstrained ReLU features model with cross-entropy loss."
---

# Neural Collapse for Cross-entropy Class-Imbalanced Learning with Unconstrained ReLU Features Model

**Source**: [https://proceedings.mlr.press/v235/dang24a.html](https://proceedings.mlr.press/v235/dang24a.html)

**TLDR**: Analyzes neural collapse under class-imbalanced training using an unconstrained ReLU features model with cross-entropy loss.

## Abstract

The current paradigm of training deep neural networks for classification tasks includes minimizing the empirical risk, pushing the training loss value towards zero even after the training classification error has vanished. In this terminal phase of training, it has been observed that the last-layer features collapse to their class-means and these class-means converge to the vertices of a simplex Equiangular Tight Frame (ETF). This phenomenon is termed as Neural Collapse ($\mathcal{NC}$). However, this characterization only holds in class-balanced datasets where every class has the same number of training samples. When the training dataset is class-imbalanced, some $\mathcal{NC}$ properties will no longer hold true, for example, the geometry of class-means will skew away from the simplex ETF. In this paper, we generalize $\mathcal{NC}$ to imbalanced regime for cross-entropy loss under the unconstrained ReLU features model. We demonstrate that while the within-class features collapse property still holds in this setting, the class-means will converge to a structure consisting of orthogonal vectors with lengths dependent on the number of training samples. Furthermore, we find that the classifier weights (i.e., the last-layer linear classifier) are aligned to the scaled and centered class-means, with scaling factors dependent on the number of training samples of each class. This generalizes $\mathcal{NC}$ in the class-balanced setting. We empirically validate our results through experiments on practical architectures and dataset.