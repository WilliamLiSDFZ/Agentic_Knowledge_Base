---
title: "Amortizing Pragmatic Program Synthesis with Rankings"
source: "https://proceedings.mlr.press/v235/pu24c.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/pu24c/pu24c.pdf"
categories: ['neural-symbolic-combinatorial-optimization-learning', 'large-language-model-alignment-and-capabilities']
tags: ['program-synthesis', 'rational-speech-acts', 'amortization']
venue: "ICML 2024"
tldr: "An amortized pragmatic program synthesizer using RSA rankings to efficiently generate informative programs."
---

# Amortizing Pragmatic Program Synthesis with Rankings

**Source**: [https://proceedings.mlr.press/v235/pu24c.html](https://proceedings.mlr.press/v235/pu24c.html)

**TLDR**: An amortized pragmatic program synthesizer using RSA rankings to efficiently generate informative programs.

## Abstract

The usage of Rational Speech Acts (RSA) framework has been successful in building pragmatic program synthesizers that return programs which, in addition to being logically consistent with user-generated examples, account for the fact that a user chooses their examples informatively. We present a general method of amortizing the slow, exact RSA synthesizer. Our method first compiles a communication dataset of partially ranked programs by querying the exact RSA synthesizer. It then distills a global ranking – a single, total ordering of all programs, to approximate the partial rankings from this dataset. This global ranking is then used at inference time to rank multiple logically consistent candidate programs generated from a fast, non-pragmatic synthesizer. Experiments on two program synthesis domains using our ranking method resulted in orders of magnitudes of speed ups compared to the exact RSA synthesizer, while being more accurate than a non-pragmatic synthesizer. Finally, we prove that in the special case of synthesis from a single example, this approximation is exact.