---
title: "Transformers, parallel computation, and logarithmic depth"
source: "https://proceedings.mlr.press/v235/sanford24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/sanford24a/sanford24a.pdf"
categories: ['transformer-architecture-efficiency-and-scaling', 'dynamic-algorithms-and-complexity-theory']
tags: ['transformers', 'parallel-computation', 'logarithmic-depth', 'circuit-complexity', 'massively-parallel']
venue: "ICML 2024"
tldr: "Constant-depth self-attention layers are shown to simulate constant rounds of Massively Parallel Computation, implying logarithmic depth suffices for basic computational tasks."
---

# Transformers, parallel computation, and logarithmic depth

**Source**: [https://proceedings.mlr.press/v235/sanford24a.html](https://proceedings.mlr.press/v235/sanford24a.html)

**TLDR**: Constant-depth self-attention layers are shown to simulate constant rounds of Massively Parallel Computation, implying logarithmic depth suffices for basic computational tasks.

## Abstract

We show that a constant number of self-attention layers can efficiently simulate—and be simulated by—a constant number of communication rounds of Massively Parallel Computation. As a consequence, we show that logarithmic-depth is sufficient for transformers to solve basic computational tasks that cannot be efficiently solved by several other neural sequence models and sub-quadratic transformer approximations. We thus establish parallelism as a key distinguishing property of transformers.