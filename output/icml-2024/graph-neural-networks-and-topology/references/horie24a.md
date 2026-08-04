---
title: "Graph Neural PDE Solvers with Conservation and Similarity-Equivariance"
source: "https://proceedings.mlr.press/v235/horie24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/horie24a/horie24a.pdf"
categories: ['neural-operators-for-pde-solving', 'graph-neural-networks-and-topology']
tags: ['graph-neural-networks', 'pde-solver', 'conservation-laws', 'equivariance', 'physics-informed']
venue: "ICML 2024"
tldr: "Develops graph neural PDE solvers that incorporate physical conservation laws and similarity-equivariance for improved generalization across spatial domains."
---

# Graph Neural PDE Solvers with Conservation and Similarity-Equivariance

**Source**: [https://proceedings.mlr.press/v235/horie24a.html](https://proceedings.mlr.press/v235/horie24a.html)

**TLDR**: Develops graph neural PDE solvers that incorporate physical conservation laws and similarity-equivariance for improved generalization across spatial domains.

## Abstract

Utilizing machine learning to address partial differential equations (PDEs) presents significant challenges due to the diversity of spatial domains and their corresponding state configurations, which complicates the task of encompassing all potential scenarios through data-driven methodologies alone. Moreover, there are legitimate concerns regarding the generalization and reliability of such approaches, as they often overlook inherent physical constraints. In response to these challenges, this study introduces a novel machine-learning architecture that is highly generalizable and adheres to conservation laws and physical symmetries, thereby ensuring greater reliability. The foundation of this architecture is graph neural networks (GNNs), which are adept at accommodating a variety of shapes and forms. Additionally, we explore the parallels between GNNs and traditional numerical solvers, facilitating a seamless integration of conservative principles and symmetries into machine learning models. Our findings from experiments demonstrate that the model’s inclusion of physical laws significantly enhances its generalizability, i.e., no significant accuracy degradation for unseen spatial domains while other models degrade. The code is available at https://github.com/yellowshippo/fluxgnn-icml2024.