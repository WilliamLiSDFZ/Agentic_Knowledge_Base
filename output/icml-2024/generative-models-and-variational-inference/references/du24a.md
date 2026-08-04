---
title: "Principled Gradient-Based MCMC for Conditional Sampling of Text"
source: "https://proceedings.mlr.press/v235/du24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/du24a/du24a.pdf"
categories: ['generative-models-and-variational-inference', 'large-language-model-alignment-and-capabilities']
tags: ['MCMC', 'energy-based-models', 'text-sampling', 'discrete-diffusion']
venue: "ICML 2024"
tldr: "A principled gradient-based MCMC method is proposed for conditional text sampling from energy-based language models by leveraging continuous internal representations."
---

# Principled Gradient-Based MCMC for Conditional Sampling of Text

**Source**: [https://proceedings.mlr.press/v235/du24a.html](https://proceedings.mlr.press/v235/du24a.html)

**TLDR**: A principled gradient-based MCMC method is proposed for conditional text sampling from energy-based language models by leveraging continuous internal representations.

## Abstract

We consider the problem of sampling text from an energy-based model. This arises, for example, when sampling text from a neural language model subject to soft constraints. Although the target distribution is discrete, the internal computations of the energy function (given by the language model) are differentiable, so one would like to exploit gradient information within a method such as MCMC. Alas, all previous attempts to generalize gradient-based MCMC to text sampling fail to sample correctly from the target distribution. We propose a solution, along with variants, and study its theoretical properties. Through experiments on various forms of text generation, we demonstrate that our unbiased samplers are able to generate more fluent text while better adhering to the control objectives. The same methods could be used to sample from discrete energy-based models unrelated to text.