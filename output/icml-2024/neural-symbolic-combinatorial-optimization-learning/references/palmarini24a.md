---
title: "Bayesian Program Learning by Decompiling Amortized Knowledge"
source: "https://proceedings.mlr.press/v235/palmarini24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/palmarini24a/palmarini24a.pdf"
categories: ['neural-symbolic-combinatorial-optimization-learning']
tags: ['program-synthesis', 'amortized-inference', 'Bayesian-program-learning', 'decompilation']
venue: "ICML 2024"
tldr: "Improves DreamCoder's program synthesis by decompiling amortized knowledge to enhance search efficiency."
---

# Bayesian Program Learning by Decompiling Amortized Knowledge

**Source**: [https://proceedings.mlr.press/v235/palmarini24a.html](https://proceedings.mlr.press/v235/palmarini24a.html)

**TLDR**: Improves DreamCoder's program synthesis by decompiling amortized knowledge to enhance search efficiency.

## Abstract

DreamCoder is an inductive program synthesis system that, whilst solving problems, learns to simplify search in an iterative wake-sleep procedure. The cost of search is amortized by training a neural search policy, reducing search breadth and effectively "compiling" useful information to compose program solutions across tasks. Additionally, a library of program components is learnt to compress and express discovered solutions in fewer components, reducing search depth. We present a novel approach for library learning that directly leverages the neural search policy, effectively "decompiling" its amortized knowledge to extract relevant program components. This provides stronger amortized inference: the amortized knowledge learnt to reduce search breadth is now also used to reduce search depth. We integrate our approach with DreamCoder and demonstrate faster domain proficiency with improved generalization on a range of domains, particularly when fewer example solutions are available.