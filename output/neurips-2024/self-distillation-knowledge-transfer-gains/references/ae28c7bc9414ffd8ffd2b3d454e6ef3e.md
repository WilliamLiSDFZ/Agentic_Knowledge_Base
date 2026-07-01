---
title: "Contrastive-Equivariant Self-Supervised Learning Improves Alignment with Primate Visual Area IT"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/ae28c7bc9414ffd8ffd2b3d454e6ef3e-Abstract-Conference.html"
categories: ['disentangled-representation-learning-cognitive-diagnosis', 'self-distillation-knowledge-transfer-gains']
tags: ['self-supervised-learning', 'visual-cortex', 'neural-prediction']
venue: "NeurIPS 2024"
tldr: "Contrastive-equivariant self-supervised learning objectives improve alignment between deep network representations and primate visual area IT neural responses."
---

# Contrastive-Equivariant Self-Supervised Learning Improves Alignment with Primate Visual Area IT

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/ae28c7bc9414ffd8ffd2b3d454e6ef3e-Abstract-Conference.html](https://papers.nips.cc/paper_files/paper/2024/hash/ae28c7bc9414ffd8ffd2b3d454e6ef3e-Abstract-Conference.html)

**TLDR**: Contrastive-equivariant self-supervised learning objectives improve alignment between deep network representations and primate visual area IT neural responses.

## Abstract

Models trained with self-supervised learning objectives have recently matched or surpassed models trained with traditional supervised object recognition in their ability to predict neural responses of object-selective neurons in the primate visual system. A self-supervised learning objective is arguably a more biologically plausible organizing principle, as the optimization does not require a large number of labeled examples. However, typical self-supervised objectives may result in network representations that are overly invariant to changes in the input. Here, we show that a representation with structured variability to the input transformations is better aligned with known features of visual perception and neural computation. We introduce a novel framework for converting standard invariant SSL losses into "contrastive-equivariant" versions that encourage preserving aspects of the input transformation without supervised access to the transformation parameters. We further demonstrate that our proposed method systematically increases models' ability to predict responses in macaque inferior temporal cortex. Our results demonstrate the promise of incorporating known features of neural computation into task-optimization for building better models of visual cortex.