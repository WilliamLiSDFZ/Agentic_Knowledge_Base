---
title: "Autoformalizing Euclidean Geometry"
source: "https://proceedings.mlr.press/v235/murphy24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/murphy24a/murphy24a.pdf"
categories: ['neural-symbolic-combinatorial-optimization-learning', 'large-language-model-alignment-and-capabilities']
tags: ['autoformalization', 'Euclidean-geometry', 'neuro-symbolic', 'formal-proofs']
venue: "ICML 2024"
tldr: "A neuro-symbolic framework for automatically translating informal Euclidean geometry into machine-verifiable formal theorems and proofs is introduced."
---

# Autoformalizing Euclidean Geometry

**Source**: [https://proceedings.mlr.press/v235/murphy24a.html](https://proceedings.mlr.press/v235/murphy24a.html)

**TLDR**: A neuro-symbolic framework for automatically translating informal Euclidean geometry into machine-verifiable formal theorems and proofs is introduced.

## Abstract

Autoformalization involves automatically translating informal math into formal theorems and proofs that are machine-verifiable. Euclidean geometry provides an interesting and controllable domain for studying autoformalization. In this paper, we introduce a neuro-symbolic framework for autoformalizing Euclidean geometry, which combines domain knowledge, SMT solvers, and large language models (LLMs). One challenge in Euclidean geometry is that informal proofs rely on diagrams, leaving gaps in texts that are hard to formalize. To address this issue, we use theorem provers to fill in such diagrammatic information automatically, so that the LLM only needs to autoformalize the explicit textual steps, making it easier for the model. We also provide automatic semantic evaluation for autoformalized theorem statements. We construct LeanEuclid, an autoformalization benchmark consisting of problems from Euclid’s Elements and the UniGeo dataset formalized in the Lean proof assistant. Experiments with GPT-4 and GPT-4V show the capability and limitations of state-of-the-art LLMs on autoformalizing geometry problems. The data and code are available at https://github.com/loganrjmurphy/LeanEuclid.