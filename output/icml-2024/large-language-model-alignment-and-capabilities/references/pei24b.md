---
title: "Exploiting Code Symmetries for Learning Program Semantics"
source: "https://proceedings.mlr.press/v235/pei24b.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/pei24b/pei24b.pdf"
categories: ['large-language-model-alignment-and-capabilities', 'algebraic-structures-in-machine-learning']
tags: ['code-symmetries', 'program-semantics', 'LLMs', 'group-theory', 'program-analysis']
venue: "ICML 2024"
tldr: "Introduces a group-theoretic framework incorporating semantics-preserving code transformations into LLM architectures to improve program analysis."
---

# Exploiting Code Symmetries for Learning Program Semantics

**Source**: [https://proceedings.mlr.press/v235/pei24b.html](https://proceedings.mlr.press/v235/pei24b.html)

**TLDR**: Introduces a group-theoretic framework incorporating semantics-preserving code transformations into LLM architectures to improve program analysis.

## Abstract

This paper tackles the challenge of teaching code semantics to Large Language Models (LLMs) for program analysis by incorporating code symmetries into the model architecture. We introduce a group-theoretic framework that defines code symmetries as semantics-preserving transformations, where forming a code symmetry group enables precise and efficient reasoning of code semantics. Our solution, SymC, develops a novel variant of self-attention that is provably equivariant to code symmetries from the permutation group defined over the program dependence graph. SymC obtains superior performance on five program analysis tasks, outperforming state-of-the-art code models, including GPT-4, without any pre-training. Our results suggest that code LLMs that encode the code structural prior via the code symmetry group generalize better and faster.