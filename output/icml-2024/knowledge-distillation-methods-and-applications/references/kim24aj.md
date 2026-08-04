---
title: "Do Topological Characteristics Help in Knowledge Distillation?"
source: "https://proceedings.mlr.press/v235/kim24aj.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/kim24aj/kim24aj.pdf"
categories: ['knowledge-distillation-methods-and-applications', 'topological-deep-learning-persistent-homology']
tags: ['knowledge-distillation', 'topological-features', 'persistent-homology']
venue: "ICML 2024"
tldr: "Investigates whether topological characteristics of embedding spaces can improve knowledge transfer in knowledge distillation."
---

# Do Topological Characteristics Help in Knowledge Distillation?

**Source**: [https://proceedings.mlr.press/v235/kim24aj.html](https://proceedings.mlr.press/v235/kim24aj.html)

**TLDR**: Investigates whether topological characteristics of embedding spaces can improve knowledge transfer in knowledge distillation.

## Abstract

Knowledge distillation (KD) aims to transfer knowledge from larger (teacher) to smaller (student) networks. Previous studies focus on point-to-point or pairwise relationships in embedding features as knowledge and struggle to efficiently transfer relationships of complex latent spaces. To tackle this issue, we propose a novel KD method called TopKD, which considers the global topology of the latent spaces. We define global topology knowledge using the persistence diagram (PD) that captures comprehensive geometric structures such as shape of distribution, multiscale structure and connectivity, and the topology distillation loss for teaching this knowledge. To make the PD transferable within reasonable computational time, we employ approximated persistence images of PDs. Through experiments, we support the benefits of using global topology as knowledge and demonstrate the potential of TopKD. Code is available at https://github.com/jekim5418/TopKD