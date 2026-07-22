---
title: "Are Decoder-Only Language Models Better than Encoder-Only Language Models in Understanding Word Meaning?"
source: "https://aclanthology.org/2024.findings-acl.967/"
categories: ['language-model-representations-and-embedding-spaces', 'language-model-human-cognitive-linguistic-alignment']
tags: ['encoder-decoder', 'word-meaning', 'language-models']
venue: "ACL 2024"
tldr: "This paper compares decoder-only and encoder-only language models on their ability to understand word meaning and semantics."
---

# Are Decoder-Only Language Models Better than Encoder-Only Language Models in Understanding Word Meaning?

**Source**: [https://aclanthology.org/2024.findings-acl.967/](https://aclanthology.org/2024.findings-acl.967/)

**TLDR**: This paper compares decoder-only and encoder-only language models on their ability to understand word meaning and semantics.

## Abstract

AbstractThe natural language processing field has been evolving around language models for the past few years, from the usage of n-gram language models for re-ranking, to transfer learning with encoder-only (BERT-like) language models, and finally to large language models (LLMs) as general solvers. LLMs are dominated by the decoder-only type, and they are popular for their efficacy in numerous tasks. LLMs are regarded as having strong comprehension abilities and strong capabilities to solve new unseen tasks. As such, people may quickly assume that decoder-only LLMs always perform better than the encoder-only ones, especially for understanding word meaning. In this paper, we demonstrate that decoder-only LLMs perform worse on word meaning comprehension than an encoder-only language model that has vastly fewer parameters.