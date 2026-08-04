---
title: "Improving Open-Ended Text Generation via Adaptive Decoding"
source: "https://proceedings.mlr.press/v235/zhu24d.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/zhu24d/zhu24d.pdf"
categories: ['large-language-model-alignment-and-capabilities', 'neural-network-learning-dynamics-theory']
tags: ['decoding', 'text-generation', 'language-models', 'adaptive-decoding', 'token-selection']
venue: "ICML 2024"
tldr: "This paper proposes adaptive decoding, a mechanism that dynamically determines the candidate token set during language model generation to improve open-ended text quality."
---

# Improving Open-Ended Text Generation via Adaptive Decoding

**Source**: [https://proceedings.mlr.press/v235/zhu24d.html](https://proceedings.mlr.press/v235/zhu24d.html)

**TLDR**: This paper proposes adaptive decoding, a mechanism that dynamically determines the candidate token set during language model generation to improve open-ended text quality.

## Abstract

Current language models decode text token by token according to probabilistic distribution, and determining the appropriate candidates for the next token is crucial to ensure generation quality. This study introduces adaptive decoding, a mechanism that dynamically empowers language models to ascertain a sensible candidate set during generation. Specifically, we introduce an entropy-based metric called confidence and conceptualize determining the optimal candidate set as a confidence-increasing process. The rationality of including a token in the candidate set is assessed by leveraging the increment of confidence. Experimental results reveal that our method balances diversity and coherence well. The human evaluation shows that our method can generate human-preferred text. Additionally, our method can potentially improve the reasoning ability of language models.