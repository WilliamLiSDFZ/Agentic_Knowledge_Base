---
title: "Unsupervised Evaluation of Code LLMs with Round-Trip Correctness"
source: "https://proceedings.mlr.press/v235/allamanis24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/allamanis24a/allamanis24a.pdf"
categories: ['large-language-model-alignment-and-capabilities', 'data-selection-and-active-learning-methods']
tags: ['code-LLMs', 'evaluation', 'round-trip-correctness']
venue: "ICML 2024"
tldr: "This paper proposes round-trip correctness as an unsupervised evaluation method for code LLMs that covers broader real-world software domains."
---

# Unsupervised Evaluation of Code LLMs with Round-Trip Correctness

**Source**: [https://proceedings.mlr.press/v235/allamanis24a.html](https://proceedings.mlr.press/v235/allamanis24a.html)

**TLDR**: This paper proposes round-trip correctness as an unsupervised evaluation method for code LLMs that covers broader real-world software domains.

## Abstract

To evaluate code large language models (LLMs), research has relied on a few small manually curated benchmarks, such as HumanEval and MBPP, which represent a narrow part of the real-world software domains. In this work, we introduce round-trip correctness (RTC) as an alternative evaluation method. RTC allows Code LLM evaluation on a broader spectrum of real-world software domains without the need for costly human curation. RTC rests on the idea that we can ask a model to make a prediction (e.g., describe some code using natural language), feed that prediction back (e.g., synthesize code from the predicted description), and check if this round-trip leads to code that is semantically equivalent to the original input. We show how to employ RTC to evaluate code synthesis and editing. We find that RTC strongly correlates with model performance on existing narrow-domain code synthesis benchmarks while allowing us to expand to a much broader set of domains and tasks which was not previously possible without costly human annotations.