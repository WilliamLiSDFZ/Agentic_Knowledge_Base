---
title: "Toward Availability Attacks in 3D Point Clouds"
source: "https://proceedings.mlr.press/v235/zhu24i.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/zhu24i/zhu24i.pdf"
categories: ['adversarial-robustness-and-model-security', '3d-vision-and-scene-understanding']
tags: ['availability-attacks', '3D-point-clouds', 'adversarial', 'data-poisoning', '3D-vision']
venue: "ICML 2024"
tldr: "This paper systematically explores availability attacks against 3D point cloud deep learning models to protect data from unauthorized use."
---

# Toward Availability Attacks in 3D Point Clouds

**Source**: [https://proceedings.mlr.press/v235/zhu24i.html](https://proceedings.mlr.press/v235/zhu24i.html)

**TLDR**: This paper systematically explores availability attacks against 3D point cloud deep learning models to protect data from unauthorized use.

## Abstract

Despite the great progress of 3D vision, data privacy and security issues in 3D deep learning are not explored systematically. In the domain of 2D images, many availability attacks have been proposed to prevent data from being illicitly learned by unauthorized deep models. However, unlike images represented on a fixed dimensional grid, point clouds are characterized as unordered and unstructured sets, posing a significant challenge in designing an effective availability attack for 3D deep learning. In this paper, we theoretically show that extending 2D availability attacks directly to 3D point clouds under distance regularization is susceptible to the degeneracy, rendering the generated poisons weaker or even ineffective. This is because in bi-level optimization, introducing regularization term can result in update directions out of control. To address this issue, we propose a novel Feature Collision Error-Minimization (FC-EM) method, which creates additional shortcuts in the feature space, inducing different update directions to prevent the degeneracy of bi-level optimization. Moreover, we provide a theoretical analysis that demonstrates the effectiveness of the FC-EM attack. Extensive experiments on typical point cloud datasets, 3D intracranial aneurysm medical dataset, and 3D face dataset verify the superiority and practicality of our approach.