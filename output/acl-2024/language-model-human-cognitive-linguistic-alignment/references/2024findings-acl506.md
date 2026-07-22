---
title: "Simplifying Translations for Children: Iterative Simplification Considering Age of Acquisition with LLMs"
source: "https://aclanthology.org/2024.findings-acl.506/"
categories: ['text-simplification-evaluation-and-methods', 'language-model-human-cognitive-linguistic-alignment']
tags: ['text-simplification', 'machine-translation', 'age-of-acquisition']
venue: "ACL 2024"
tldr: "Proposes an iterative LLM-based method to simplify translations for children by incorporating age-of-acquisition vocabulary constraints."
---

# Simplifying Translations for Children: Iterative Simplification Considering Age of Acquisition with LLMs

**Source**: [https://aclanthology.org/2024.findings-acl.506/](https://aclanthology.org/2024.findings-acl.506/)

**TLDR**: Proposes an iterative LLM-based method to simplify translations for children by incorporating age-of-acquisition vocabulary constraints.

## Abstract

AbstractIn recent years, neural machine translation (NMT) has become widely used in everyday life. However, the current NMT lacks a mechanism to adjust the difficulty level of translations to match the user’s language level. Additionally, due to the bias in the training data for NMT, translations of simple source sentences are often produced with complex words. In particular, this could pose a problem for children, who may not be able to understand the meaning of the translations correctly. In this study, we propose a method that replaces high Age of Acquisitions (AoA) words in translations with simpler words to match the translations to the user’s level. We achieve this by using large language models (LLMs), providing a triple of a source sentence, a translation, and a target word to be replaced. We create a benchmark dataset using back-translation on Simple English Wikipedia. The experimental results obtained from the dataset show that our method effectively replaces high-AoA words with lower-AoA words and, moreover, can iteratively replace most of the high-AoA words while still maintaining high BLEU and COMET scores.