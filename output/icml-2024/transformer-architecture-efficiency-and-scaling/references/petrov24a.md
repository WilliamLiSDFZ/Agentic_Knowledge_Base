---
title: "Prompting a Pretrained Transformer Can Be a Universal Approximator"
source: "https://proceedings.mlr.press/v235/petrov24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/petrov24a/petrov24a.pdf"
categories: ['transformer-architecture-efficiency-and-scaling', 'neural-network-learning-dynamics-theory']
tags: ['prompting', 'prefix-tuning', 'universal-approximation', 'transformers', 'fine-tuning-theory']
venue: "ICML 2024"
tldr: "Proves that prompting and prefix-tuning of pretrained transformers can universally approximate arbitrary modifications to model behavior."
---

# Prompting a Pretrained Transformer Can Be a Universal Approximator

**Source**: [https://proceedings.mlr.press/v235/petrov24a.html](https://proceedings.mlr.press/v235/petrov24a.html)

**TLDR**: Proves that prompting and prefix-tuning of pretrained transformers can universally approximate arbitrary modifications to model behavior.

## Abstract

Despite the widespread adoption of prompting, prompt tuning and prefix-tuning of transformer models, our theoretical understanding of these fine-tuning methods remains limited. A key question is whether one can arbitrarily modify the behavior of a pretrained model by prompting or prefix-tuning it. Formally, whether prompting and prefix-tuning a pretrained model can universally approximate sequence-to-sequence functions. This paper answers in the affirmative and demonstrates that much smaller pretrained models than previously thought can be universal approximators when prefixed. In fact, prefix-tuning a single attention head is sufficient to approximate any continuous function making the attention mechanism uniquely suited for universal approximation. Moreover, any sequence-to-sequence function can be approximated by prefixing a transformer with depth linear in the sequence length. Beyond these density-type results, we also offer Jackson-type bounds on the length of the prefix needed to approximate a function to a desired precision.