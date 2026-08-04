---
title: "Fool Your (Vision and) Language Model with Embarrassingly Simple Permutations"
source: "https://proceedings.mlr.press/v235/zong24b.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/zong24b/zong24b.pdf"
categories: ['adversarial-robustness-and-model-security', 'large-language-model-alignment-and-capabilities']
tags: ['adversarial-robustness', 'permutations', 'vision-language-models', 'LLMs', 'in-context-learning']
venue: "ICML 2024"
tldr: "This paper demonstrates that simple input permutations can fool both language and vision-language models, revealing surprising robustness failures."
---

# Fool Your (Vision and) Language Model with Embarrassingly Simple Permutations

**Source**: [https://proceedings.mlr.press/v235/zong24b.html](https://proceedings.mlr.press/v235/zong24b.html)

**TLDR**: This paper demonstrates that simple input permutations can fool both language and vision-language models, revealing surprising robustness failures.

## Abstract

Large language and vision-language models are rapidly being deployed in practice thanks to their impressive capabilities in instruction following, in-context learning, and so on. This raises an urgent need to carefully analyse their robustness so that stakeholders can understand if and when such models are trustworthy enough to be relied upon in any given application. In this paper, we highlight a specific vulnerability in popular models, namely permutation sensitivity in multiple-choice question answering (MCQA). Specifically, we show empirically that popular models are vulnerable to adversarial permutation in answer sets for multiple-choice prompting, which is surprising as models should ideally be as invariant to prompt permutation as humans are. These vulnerabilities persist across various model sizes, and exist in very recent language and vision-language models. Code to reproduce all experiments is provided in supplementary materials.