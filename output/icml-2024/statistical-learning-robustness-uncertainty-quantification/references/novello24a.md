---
title: "$f$-Divergence Based Classification: Beyond the Use of Cross-Entropy"
source: "https://proceedings.mlr.press/v235/novello24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/novello24a/novello24a.pdf"
categories: ['optimization-algorithms-convergence-theory', 'statistical-learning-robustness-uncertainty-quantification']
tags: ['f-divergence', 'classification', 'cross-entropy']
venue: "ICML 2024"
tldr: "Generalizes deep learning classification objectives beyond cross-entropy using f-divergence formulations for improved optimization."
---

# $f$-Divergence Based Classification: Beyond the Use of Cross-Entropy

**Source**: [https://proceedings.mlr.press/v235/novello24a.html](https://proceedings.mlr.press/v235/novello24a.html)

**TLDR**: Generalizes deep learning classification objectives beyond cross-entropy using f-divergence formulations for improved optimization.

## Abstract

In deep learning, classification tasks are formalized as optimization problems often solved via the minimization of the cross-entropy. However, recent advancements in the design of objective functions allow the usage of the $f$-divergence to generalize the formulation of the optimization problem for classification. We adopt a Bayesian perspective and formulate the classification task as a maximum a posteriori probability problem. We propose a class of objective functions based on the variational representation of the $f$-divergence. Furthermore, driven by the challenge of improving the state-of-the-art approach, we propose a bottom-up method that leads us to the formulation of an objective function corresponding to a novel $f$-divergence referred to as shifted log (SL). We theoretically analyze the objective functions proposed and numerically test them in three application scenarios: toy examples, image datasets, and signal detection/decoding problems. The analyzed scenarios demonstrate the effectiveness of the proposed approach and that the SL divergence achieves the highest classification accuracy in almost all the considered cases.