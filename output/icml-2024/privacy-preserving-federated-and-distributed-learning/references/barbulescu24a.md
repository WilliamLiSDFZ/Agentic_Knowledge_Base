---
title: "To Each (Textual Sequence) Its Own: Improving Memorized-Data Unlearning in Large Language Models"
source: "https://proceedings.mlr.press/v235/barbulescu24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/barbulescu24a/barbulescu24a.pdf"
categories: ['large-language-model-alignment-and-capabilities', 'privacy-preserving-federated-and-distributed-learning']
tags: ['unlearning', 'memorization', 'privacy', 'LLM', 'copyright']
venue: "ICML 2024"
tldr: "Proposes improved algorithms for unlearning memorized textual sequences in large language models to address privacy and copyright concerns."
---

# To Each (Textual Sequence) Its Own: Improving Memorized-Data Unlearning in Large Language Models

**Source**: [https://proceedings.mlr.press/v235/barbulescu24a.html](https://proceedings.mlr.press/v235/barbulescu24a.html)

**TLDR**: Proposes improved algorithms for unlearning memorized textual sequences in large language models to address privacy and copyright concerns.

## Abstract

LLMs have been found to memorize training textual sequences and regurgitate verbatim said sequences during text generation time. This fact is known to be the cause of privacy and related (e.g., copyright) problems. Unlearning in LLMs then takes the form of devising new algorithms that will properly deal with these side-effects of memorized data, while not hurting the model’s utility. We offer a fresh perspective towards this goal, namely, that each textual sequence to be forgotten should be treated differently when being unlearned based on its degree of memorization within the LLM. We contribute a new metric for measuring unlearning quality, an adversarial attack showing that SOTA algorithms lacking this perspective fail for privacy, and two new unlearning methods based on Gradient Ascent and Task Arithmetic, respectively. A comprehensive performance evaluation across an extensive suite of NLP tasks then mapped the solution space, identifying the best solutions under different scales in model capacities and forget set sizes and quantified the gains of the new approaches.