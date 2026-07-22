---
title: "LANS: A Layout-Aware Neural Solver for Plane Geometry Problem"
source: "https://aclanthology.org/2024.findings-acl.153/"
categories: ['multimodal-language-vision-learning-systems', 'llm-reasoning-and-knowledge-graph-benchmarks']
tags: ['geometry-problem-solving', 'layout-awareness', 'multimodal-reasoning']
venue: "ACL 2024"
tldr: "Proposes a layout-aware neural solver for plane geometry problems that better represents spatial relationships in diagrams."
---

# LANS: A Layout-Aware Neural Solver for Plane Geometry Problem

**Source**: [https://aclanthology.org/2024.findings-acl.153/](https://aclanthology.org/2024.findings-acl.153/)

**TLDR**: Proposes a layout-aware neural solver for plane geometry problems that better represents spatial relationships in diagrams.

## Abstract

AbstractGeometry problem solving (GPS) is a challenging mathematical reasoning task requiring multi-modal understanding, fusion, and reasoning. Existing neural solvers take GPS as a vision-language task but are short in the representation of geometry diagrams that carry rich and complex layout information. In this paper, we propose a layout-aware neural solver named LANS, integrated with two new modules: multimodal layout-aware pre-trained language module (MLA-PLM) and layout-aware fusion attention (LA-FA). MLA-PLM adopts structural-semantic pre-training (SSP) to implement global relationship modeling, and point-match pre-training (PMP) to achieve alignment between visual points and textual points. LA-FA employs a layout-aware attention mask to realize point-guided cross-modal fusion for further boosting layout awareness of LANS. Extensive experiments on datasets Geometry3K and PGPS9K validate the effectiveness of the layout-aware modules and superior problem-solving performance of our LANS solver, over existing symbolic and neural solvers. We have made our code and data publicly available.