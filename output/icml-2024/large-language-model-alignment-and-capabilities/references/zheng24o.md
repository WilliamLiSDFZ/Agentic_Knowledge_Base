---
title: "Self-Infilling Code Generation"
source: "https://proceedings.mlr.press/v235/zheng24o.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/zheng24o/zheng24o.pdf"
categories: ['large-language-model-alignment-and-capabilities']
tags: ['code-generation', 'infilling', 'auto-regressive-decoding', 'code-language-models']
venue: "ICML 2024"
tldr: "Self-infilling integrates infilling operations into auto-regressive code generation to improve coherence and completeness of generated code."
---

# Self-Infilling Code Generation

**Source**: [https://proceedings.mlr.press/v235/zheng24o.html](https://proceedings.mlr.press/v235/zheng24o.html)

**TLDR**: Self-infilling integrates infilling operations into auto-regressive code generation to improve coherence and completeness of generated code.

## Abstract

In this work, we introduce self-infilling code generation, a general framework that incorporates infilling operations into auto-regressive decoding. Our approach capitalizes on the observation that recent infilling-capable code language models can perform self-infilling: whereas conventional infilling is designed to fill in the middle based on a predefined prefix and suffix, self-infilling sequentially generates both such surrounding context and the infilled content. We utilize self-infilling to introduce novel interruption and looping mechanisms in conventional decoding, evolving it into a non-monotonic process. Interruptions allow for postponing the generation of specific code until a definitive suffix is established, enhancing control during decoding. Meanwhile, the looping mechanism, which leverages the complementary nature of self-infilling and left-to-right decoding, can iteratively update and synchronize each piece of generation cyclically. Extensive experiments across a variety of code generation benchmarks demonstrate that decoding with self-infilling not only improves the output quality but also regularizes the overall generation, which effectively mitigates potential degeneration and scaffolds code to be more consistent with intended functionality.