---
title: "Tackling Prevalent Conditions in Unsupervised Combinatorial Optimization: Cardinality, Minimum, Covering, and More"
source: "https://proceedings.mlr.press/v235/bu24b.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/bu24b/bu24b.pdf"
categories: ['neural-symbolic-combinatorial-optimization-learning', 'submodular-optimization-and-combinatorial-algorithms']
tags: ['combinatorial-optimization', 'probabilistic-method', 'differentiable-optimization', 'unsupervised']
venue: "ICML 2024"
tldr: "Extends probabilistic-method-based differentiable CO framework to handle cardinality, covering, and minimum-type constraints."
---

# Tackling Prevalent Conditions in Unsupervised Combinatorial Optimization: Cardinality, Minimum, Covering, and More

**Source**: [https://proceedings.mlr.press/v235/bu24b.html](https://proceedings.mlr.press/v235/bu24b.html)

**TLDR**: Extends probabilistic-method-based differentiable CO framework to handle cardinality, covering, and minimum-type constraints.

## Abstract

Combinatorial optimization (CO) is naturally discrete, making machine-learning techniques based on differentiable optimization inapplicable. Karalias & Loukas (2020) adapted the probabilistic method by Erdős & Spencer (1974), to incorporate CO into differentiable optimization. Their work ignited the research on unsupervised learning for CO, composed of two main components: probabilistic objectives and derandomization. However, each component confronts unique challenges. First, deriving objectives under complex conditions and constraints is nontrivial. Second, the derandomization process is underexplored, and the existing derandomization methods are either random sampling or naive rounding. In this work, we aim to tackle complex conditions in unsupervised CO. First, we concretize the targets for probabilistic objective construction and derandomization with theoretical justification. Then, for various complex conditions commonly involved in different CO problems, we derive nontrivial objectives and derandomization to meet the targets. Finally, we apply the derivations to various CO problems. Via extensive experiments on synthetic and real-world graphs, we validate the correctness of our derivations and show our empirical superiority w.r.t. both optimization quality and speed.