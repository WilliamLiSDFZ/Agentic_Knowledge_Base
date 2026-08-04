---
title: "On Computational Limits of Modern Hopfield Models: A Fine-Grained Complexity Analysis"
source: "https://proceedings.mlr.press/v235/hu24j.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/hu24j/hu24j.pdf"
categories: ['transformer-architecture-efficiency-and-scaling', 'dynamic-algorithms-and-complexity-theory']
tags: ['hopfield-models', 'fine-grained-complexity', 'phase-transition', 'memory-retrieval', 'computational-limits']
venue: "ICML 2024"
tldr: "Characterizes phase transition behavior in the computational efficiency of modern Hopfield models via fine-grained complexity analysis based on pattern norms."
---

# On Computational Limits of Modern Hopfield Models: A Fine-Grained Complexity Analysis

**Source**: [https://proceedings.mlr.press/v235/hu24j.html](https://proceedings.mlr.press/v235/hu24j.html)

**TLDR**: Characterizes phase transition behavior in the computational efficiency of modern Hopfield models via fine-grained complexity analysis based on pattern norms.

## Abstract

We investigate the computational limits of the memory retrieval dynamics of modern Hopfield models from the fine-grained complexity analysis. Our key contribution is the characterization of a phase transition behavior in the efficiency of all possible modern Hopfield models based on the norm of patterns. Specifically, we establish an upper bound criterion for the norm of input query patterns and memory patterns. Only below this criterion, sub-quadratic (efficient) variants of the modern Hopfield model exist, assuming the Strong Exponential Time Hypothesis (SETH). To showcase our theory, we provide a formal example of efficient constructions of modern Hopfield models using low-rank approximation when the efficient criterion holds. This includes a derivation of a lower bound on the computational time, scaling linearly with $\max$$\{$ # of stored memory patterns, length of input query sequence$\}$. In addition, we prove its memory retrieval error bound and exponential memory capacity.