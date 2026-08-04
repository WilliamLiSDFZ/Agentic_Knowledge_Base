---
title: "StrokeNUWA—Tokenizing Strokes for Vector Graphic Synthesis"
source: "https://proceedings.mlr.press/v235/tang24h.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/tang24h/tang24h.pdf"
categories: ['large-language-model-alignment-and-capabilities', 'llm-geometry-and-interpretability-research']
tags: ['vector-graphics', 'LLM-tokenization', 'stroke-representation']
venue: "ICML 2024"
tldr: "StrokeNUWA tokenizes vector graphics as strokes rather than raster grid tokens to enable LLMs to better capture semantic visual representations."
---

# StrokeNUWA—Tokenizing Strokes for Vector Graphic Synthesis

**Source**: [https://proceedings.mlr.press/v235/tang24h.html](https://proceedings.mlr.press/v235/tang24h.html)

**TLDR**: StrokeNUWA tokenizes vector graphics as strokes rather than raster grid tokens to enable LLMs to better capture semantic visual representations.

## Abstract

To leverage LLMs for visual synthesis, traditional methods convert raster image information into discrete grid tokens through specialized visual modules, while disrupting the model’s ability to capture the true semantic representation of visual scenes. This paper posits that an alternative representation of images, vector graphics, can effectively surmount this limitation by enabling a more natural and semantically coherent segmentation of the image information. Thus, we introduce StrokeNUWA, a pioneering work exploring a better visual representation "stroke" tokens on vector graphics, which is inherently visual semantics rich, naturally compatible with LLMs, and highly compressed. Equipped with stroke tokens, StrokeNUWA can significantly surpass traditional LLM-based and optimization-based methods across various metrics in the vector graphic generation task. Besides, StrokeNUWA achieves up to a $94\times$ speedup in inference over the speed of prior methods with an exceptional SVG code compression ratio of 6.9%.