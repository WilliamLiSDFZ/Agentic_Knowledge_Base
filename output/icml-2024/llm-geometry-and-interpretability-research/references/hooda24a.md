---
title: "Do Large Code Models Understand Programming Concepts? Counterfactual Analysis for Code Predicates"
source: "https://proceedings.mlr.press/v235/hooda24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/hooda24a/hooda24a.pdf"
categories: ['large-language-model-alignment-and-capabilities', 'llm-geometry-and-interpretability-research']
tags: ['llm', 'code-generation', 'counterfactual-analysis', 'interpretability', 'programming-concepts']
venue: "ICML 2024"
tldr: "Uses counterfactual analysis to investigate whether large code models truly understand programming concepts underlying their code generation performance."
---

# Do Large Code Models Understand Programming Concepts? Counterfactual Analysis for Code Predicates

**Source**: [https://proceedings.mlr.press/v235/hooda24a.html](https://proceedings.mlr.press/v235/hooda24a.html)

**TLDR**: Uses counterfactual analysis to investigate whether large code models truly understand programming concepts underlying their code generation performance.

## Abstract

Large Language Models’ success in text generation has also made them better at code generation and coding tasks. While a lot of work has demonstrated their remarkable performance on tasks such as code completion and editing, it is still unclear as to why. We help bridge this gap by exploring to what degree auto-regressive models understand the logical constructs of the underlying programs. We propose Counterfactual Analysis for Programming Concept Predicates (CACP) as a counterfactual testing framework to evaluate whether Large Code Models understand programming concepts. With only black-box access to the model, we use CACP to evaluate ten popular Large Code Models for four different programming concepts. Our findings suggest that current models lack understanding of concepts such as data flow and control flow.