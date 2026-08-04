---
title: "Enhancing Implicit Shape Generators Using Topological Regularizations"
source: "https://proceedings.mlr.press/v235/chen24bk.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/chen24bk/chen24bk.pdf"
categories: ['topological-deep-learning-persistent-homology', '3d-vision-and-scene-understanding']
tags: ['3D-shape-generation', 'topological-regularization', 'implicit-shape-models']
venue: "ICML 2024"
tldr: "Topological regularizations are applied to implicit shape generators to reduce artifacts in learned 3D generative models."
---

# Enhancing Implicit Shape Generators Using Topological Regularizations

**Source**: [https://proceedings.mlr.press/v235/chen24bk.html](https://proceedings.mlr.press/v235/chen24bk.html)

**TLDR**: Topological regularizations are applied to implicit shape generators to reduce artifacts in learned 3D generative models.

## Abstract

A fundamental problem in learning 3D shapes generative models is that when the generative model is simply fitted to the training data, the resulting synthetic 3D models can present various artifacts. Many of these artifacts are topological in nature, e.g., broken legs, unrealistic thin structures, and small holes. In this paper, we introduce a principled approach that utilizes topological regularization losses on an implicit shape generator to rectify topological artifacts. The objectives are two-fold. The first is to align the persistent diagram (PD) distribution of the training shapes with that of synthetic shapes. The second ensures that the PDs are smooth among adjacent synthetic shapes. We show how to achieve these two objectives using two simple but effective formulations. Specifically, distribution alignment is achieved to learn a generative model of PDs and align this generator with PDs of synthetic shapes. We show how to handle discrete and continuous variabilities of PDs by using a shape-regularization term when performing PD alignment. Moreover, we enforce the smoothness of the PDs using a smoothness loss on the PD generator, which further improves the behavior of PD distribution alignment. Experimental results on ShapeNet show that our approach leads to much better generalization behavior than state-of-the-art implicit shape generators.