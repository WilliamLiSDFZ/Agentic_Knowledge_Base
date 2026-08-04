---
title: "Unsupervised Domain Adaptation for Anatomical Structure Detection in Ultrasound Images"
source: "https://proceedings.mlr.press/v235/pu24b.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/pu24b/pu24b.pdf"
categories: ['ultrasound-image-domain-adaptation', 'learning-with-imperfect-data-and-bias']
tags: ['domain-adaptation', 'ultrasound-imaging', 'anatomical-detection']
venue: "ICML 2024"
tldr: "An unsupervised domain adaptation method for detecting anatomical structures in ultrasound images across institutions."
---

# Unsupervised Domain Adaptation for Anatomical Structure Detection in Ultrasound Images

**Source**: [https://proceedings.mlr.press/v235/pu24b.html](https://proceedings.mlr.press/v235/pu24b.html)

**TLDR**: An unsupervised domain adaptation method for detecting anatomical structures in ultrasound images across institutions.

## Abstract

Models trained on ultrasound images from one institution typically experience a decline in effectiveness when transferred directly to other institutions. Moreover, unlike natural images, dense and overlapped structures exist in fetus ultrasound images, making the detection of structures more challenging. Thus, to tackle this problem, we propose a new Unsupervised Domain Adaptation (UDA) method named ToMo-UDA for fetus structure detection, which consists of the Topology Knowledge Transfer (TKT) and the Morphology Knowledge Transfer (MKT) module. The TKT leverages prior knowledge of the medical anatomy of fetal as topological information, reconstructing and aligning anatomy features across source and target domains. Then, the MKT formulates a more consistent and independent morphological representation for each substructure of an organ. To evaluate the proposed ToMo-UDA for ultrasound fetal anatomical structure detection, we introduce FUSH$^2$, a new Fetal UltraSound benchmark, comprises Heart and Head images collected from Two health centers, with 16 annotated regions. Our experiments show that utilizing topological and morphological anatomy information in ToMo-UDA can greatly improve organ structure detection. This expands the potential for structure detection tasks in medical image analysis.