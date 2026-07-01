---
title: "Learning Superconductivity from Ordered and Disordered Material Structures"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/c4e3b55ed4ac9ba52d7df11f8bddbbf4-Abstract-Datasets_and_Benchmarks_Track.html"
categories: ['machine-learning-for-molecular-biology', 'graph-neural-networks-and-representation-learning']
tags: ['superconductivity', 'graph-neural-networks', 'materials-science', 'disordered-structures', 'data-driven']
venue: "NeurIPS 2024"
tldr: "Applies data-driven machine learning to learn superconducting properties from both ordered and disordered material structures."
---

# Learning Superconductivity from Ordered and Disordered Material Structures

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/c4e3b55ed4ac9ba52d7df11f8bddbbf4-Abstract-Datasets_and_Benchmarks_Track.html](https://papers.nips.cc/paper_files/paper/2024/hash/c4e3b55ed4ac9ba52d7df11f8bddbbf4-Abstract-Datasets_and_Benchmarks_Track.html)

**TLDR**: Applies data-driven machine learning to learn superconducting properties from both ordered and disordered material structures.

## Abstract

Superconductivity is a fascinating phenomenon observed in certain materials under certain conditions. However, some critical aspects of it, such as the relationship between superconductivity and materials' chemical/structural features, still need to be understood. Recent successes of data-driven approaches in material science strongly inspire researchers to study this relationship with them, but a corresponding dataset is still lacking. Hence, we present a new dataset for data-driven approaches, namely SuperCon3D, containing both 3D crystal structures and experimental superconducting transition temperature (Tc) for the first time. Based on SuperCon3D, we propose two deep learning methods for designing high Tc superconductors. The first is SODNet, a novel equivariant graph attention model for screening known structures, which differs from existing models in incorporating both ordered and disordered geometric content. The second is a diffusion generative model DiffCSP-SC for creating new structures, which enables high Tc-targeted generation. Extensive experiments demonstrate that both our proposed dataset and models are advantageous for designing new high Tc superconducting candidates.