---
title: "UniCorn: A Unified Contrastive Learning Approach for Multi-view Molecular Representation Learning"
source: "https://proceedings.mlr.press/v235/feng24f.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/feng24f/feng24f.pdf"
categories: ['generative-models-for-molecular-protein-design']
tags: ['molecular-representation', 'contrastive-learning', 'multi-view-pretraining']
venue: "ICML 2024"
tldr: "Proposes a unified contrastive learning framework for multi-view molecular pre-training applicable across diverse molecular tasks."
---

# UniCorn: A Unified Contrastive Learning Approach for Multi-view Molecular Representation Learning

**Source**: [https://proceedings.mlr.press/v235/feng24f.html](https://proceedings.mlr.press/v235/feng24f.html)

**TLDR**: Proposes a unified contrastive learning framework for multi-view molecular pre-training applicable across diverse molecular tasks.

## Abstract

Recently, a noticeable trend has emerged in developing pre-trained foundation models in the domains of CV and NLP. However, for molecular pre-training, there lacks a universal model capable of effectively applying to various categories of molecular tasks, since existing prevalent pre-training methods exhibit effectiveness for specific types of downstream tasks. Furthermore, the lack of profound understanding of existing pre-training methods, including 2D graph masking, 2D-3D contrastive learning, and 3D denoising, hampers the advancement of molecular foundation models. In this work, we provide a unified comprehension of existing pre-training methods through the lens of contrastive learning. Thus their distinctions lie in clustering different views of molecules, which is shown beneficial to specific downstream tasks. To achieve a complete and general-purpose molecular representation, we propose a novel pre-training framework, named UniCorn, that inherits the merits of the three methods, depicting molecular views in three different levels. SOTA performance across quantum, physicochemical, and biological tasks, along with comprehensive ablation study, validate the universality and effectiveness of UniCorn.