---
title: "Drug Discovery with Dynamic Goal-aware Fragments"
source: "https://proceedings.mlr.press/v235/lee24o.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/lee24o/lee24o.pdf"
categories: ['generative-models-for-molecular-protein-design', 'neural-symbolic-combinatorial-optimization-learning']
tags: ['drug-discovery', 'fragment-based', 'molecular-generation', 'goal-aware']
venue: "ICML 2024"
tldr: "Proposes a dynamic goal-aware fragment extraction method for fragment-based drug discovery that accounts for target chemical properties."
---

# Drug Discovery with Dynamic Goal-aware Fragments

**Source**: [https://proceedings.mlr.press/v235/lee24o.html](https://proceedings.mlr.press/v235/lee24o.html)

**TLDR**: Proposes a dynamic goal-aware fragment extraction method for fragment-based drug discovery that accounts for target chemical properties.

## Abstract

Fragment-based drug discovery is an effective strategy for discovering drug candidates in the vast chemical space, and has been widely employed in molecular generative models. However, many existing fragment extraction methods in such models do not take the target chemical properties into account or rely on heuristic rules. Additionally, the existing fragment-based generative models cannot update the fragment vocabulary with goal-aware fragments newly discovered during the generation. To this end, we propose a molecular generative framework for drug discovery, named Goal-aware fragment Extraction, Assembly, and Modification (GEAM). GEAM consists of three modules, each responsible for goal-aware fragment extraction, fragment assembly, and fragment modification. The fragment extraction module identifies important fragments contributing to the desired target properties with the information bottleneck principle, thereby constructing an effective goal-aware fragment vocabulary. Moreover, GEAM can explore beyond the initial vocabulary with the fragment modification module, and the exploration is further enhanced through the dynamic goal-aware vocabulary update. We experimentally demonstrate that GEAM effectively discovers drug candidates through the generative cycle of the three modules in various drug discovery tasks. Our code is available at https://github.com/SeulLee05/GEAM.