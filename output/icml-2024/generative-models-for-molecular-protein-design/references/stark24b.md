---
title: "Dirichlet Flow Matching with Applications to DNA Sequence Design"
source: "https://proceedings.mlr.press/v235/stark24b.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/stark24b/stark24b.pdf"
categories: ['generative-models-and-variational-inference', 'generative-models-for-molecular-protein-design']
tags: ['flow-matching', 'discrete-diffusion', 'DNA-sequence-design', 'simplex', 'Dirichlet']
venue: "ICML 2024"
tldr: "Dirichlet flow matching is proposed as a principled approach for discrete sequence generation on the simplex, addressing pathologies of naive linear flow matching for DNA design."
---

# Dirichlet Flow Matching with Applications to DNA Sequence Design

**Source**: [https://proceedings.mlr.press/v235/stark24b.html](https://proceedings.mlr.press/v235/stark24b.html)

**TLDR**: Dirichlet flow matching is proposed as a principled approach for discrete sequence generation on the simplex, addressing pathologies of naive linear flow matching for DNA design.

## Abstract

Discrete diffusion or flow models could enable faster and more controllable sequence generation than autoregressive models. We show that naive linear flow matching on the simplex is insufficient toward this goal since it suffers from discontinuities in the training target and further pathologies. To overcome this, we develop Dirichlet flow matching on the simplex based on mixtures of Dirichlet distributions as probability paths. In this framework, we derive a connection between the mixtures’ scores and the flow’s vector field that allows for classifier and classifier-free guidance. Further, we provide distilled Dirichlet flow matching, which enables one-step sequence generation with minimal performance hits, resulting in $O(L)$ speedups compared to autoregressive models. On complex DNA sequence generation tasks, we demonstrate superior performance compared to all baselines in distributional metrics and in achieving desired design targets for generated sequences. Finally, we show that our classifier-free guidance approach improves unconditional generation and is effective for generating DNA that satisfies design targets.