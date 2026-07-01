---
title: "Retrieval-Retro: Retrieval-based Inorganic Retrosynthesis with Expert Knowledge"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/2cfa9b0d9be8a5c01cf3eb7f21b4f2b8-Abstract-Conference.html"
categories: ['machine-learning-for-molecular-biology', 'scientific-document-retrieval-and-citation']
tags: ['inorganic-retrosynthesis', 'retrieval-augmented-planning', 'expert-knowledge']
venue: "NeurIPS 2024"
tldr: "Retrieval-Retro leverages retrieval-based methods with expert chemical knowledge to improve inorganic retrosynthesis planning using machine learning."
---

# Retrieval-Retro: Retrieval-based Inorganic Retrosynthesis with Expert Knowledge

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/2cfa9b0d9be8a5c01cf3eb7f21b4f2b8-Abstract-Conference.html](https://papers.nips.cc/paper_files/paper/2024/hash/2cfa9b0d9be8a5c01cf3eb7f21b4f2b8-Abstract-Conference.html)

**TLDR**: Retrieval-Retro leverages retrieval-based methods with expert chemical knowledge to improve inorganic retrosynthesis planning using machine learning.

## Abstract

While inorganic retrosynthesis planning is essential in the field of chemical science, the application of machine learning in this area has been notably less explored compared to organic retrosynthesis planning. In this paper, we propose Retrieval-Retro for inorganic retrosynthesis planning, which implicitly extracts the precursor information of reference materials that are retrieved from the knowledge base regarding domain expertise in the field. Specifically, instead of directly employing the precursor information of reference materials, we propose implicitly extracting it with various attention layers, which enables the model to learn novel synthesis recipes more effectively.Moreover, during retrieval, we consider the thermodynamic relationship between target material and precursors, which is essential domain expertise in identifying the most probable precursor set among various options. Extensive experiments demonstrate the superiority of Retrieval-Retro in retrosynthesis planning, especially in discovering novel synthesis recipes, which is crucial for materials discovery.The source code for Retrieval-Retro is available at https://github.com/HeewoongNoh/Retrieval-Retro.