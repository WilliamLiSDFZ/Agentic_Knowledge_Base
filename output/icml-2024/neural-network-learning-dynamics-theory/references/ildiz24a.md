---
title: "From Self-Attention to Markov Models: Unveiling the Dynamics of Generative Transformers"
source: "https://proceedings.mlr.press/v235/ildiz24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/ildiz24a/ildiz24a.pdf"
categories: ['neural-network-learning-dynamics-theory', 'llm-geometry-and-interpretability-research']
tags: ['self-attention', 'transformers', 'markov-models', 'learning-dynamics', 'generative-models']
venue: "ICML 2024"
tldr: "This work analyzes the learning dynamics of a 1-layer self-attention model and establishes connections between self-attention and Markov models for text generation."
---

# From Self-Attention to Markov Models: Unveiling the Dynamics of Generative Transformers

**Source**: [https://proceedings.mlr.press/v235/ildiz24a.html](https://proceedings.mlr.press/v235/ildiz24a.html)

**TLDR**: This work analyzes the learning dynamics of a 1-layer self-attention model and establishes connections between self-attention and Markov models for text generation.

## Abstract

Modern language models rely on the transformer architecture and attention mechanism to perform language understanding and text generation. In this work, we study learning a 1-layer self-attention model from a set of prompts and the associated outputs sampled from the model. We first establish a formal link between the self-attention mechanism and Markov models under suitable conditions: Inputting a prompt to the self-attention model samples the output token according to a context-conditioned Markov chain (CCMC). CCMC is obtained by weighing the transition matrix of a standard Markov chain according to the sufficient statistics of the prompt/context. Building on this formalism, we develop identifiability/coverage conditions for the data distribution that guarantee consistent estimation of the latent model under a teacher-student setting and establish sample complexity guarantees under IID data. Finally, we study the problem of learning from a single output trajectory generated in response to an initial prompt. We characterize a winner-takes-all phenomenon where the generative process of self-attention evolves to sampling from a small set of winner tokens that dominate the context window. This provides a mathematical explanation to the tendency of modern LLMs to generate repetitive text.