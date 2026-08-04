---
title: "Reprompting: Automated Chain-of-Thought Prompt Inference Through Gibbs Sampling"
source: "https://proceedings.mlr.press/v235/xu24b.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/xu24b/xu24b.pdf"
categories: ['large-language-model-alignment-and-capabilities']
tags: ['chain-of-thought', 'prompt-optimization', 'Gibbs-sampling']
venue: "ICML 2024"
tldr: "Reprompting uses Gibbs sampling to automatically infer effective Chain-of-Thought prompt recipes for LLMs without human intervention."
---

# Reprompting: Automated Chain-of-Thought Prompt Inference Through Gibbs Sampling

**Source**: [https://proceedings.mlr.press/v235/xu24b.html](https://proceedings.mlr.press/v235/xu24b.html)

**TLDR**: Reprompting uses Gibbs sampling to automatically infer effective Chain-of-Thought prompt recipes for LLMs without human intervention.

## Abstract

We introduce Reprompting, an iterative sampling algorithm that automatically learns the Chain-of-Thought (CoT) recipes for a given task without human intervention. Through Gibbs sampling, Reprompting infers the CoT recipes that work consistently well for a set of training samples by iteratively sampling new recipes using previously sampled recipes as parent prompts to solve other training problems. We conduct extensive experiments on 20 challenging reasoning tasks. Results show that Reprompting outperforms human-written CoT prompts substantially by +9.4 points on average. It also achieves consistently better performance than the state-of-the-art prompt optimization and decoding algorithms.