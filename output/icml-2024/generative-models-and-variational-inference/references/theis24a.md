---
title: "Position: What makes an image realistic?"
source: "https://proceedings.mlr.press/v235/theis24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/theis24a/theis24a.pdf"
categories: ['position-papers-on-ml-research-directions', 'generative-models-and-variational-inference']
tags: ['image-realism', 'generative-evaluation', 'perceptual-metrics']
venue: "ICML 2024"
tldr: "This position paper discusses the problem of quantifying image realism and proposes principles for designing reliable functions that distinguish realistic from unrealistic data."
---

# Position: What makes an image realistic?

**Source**: [https://proceedings.mlr.press/v235/theis24a.html](https://proceedings.mlr.press/v235/theis24a.html)

**TLDR**: This position paper discusses the problem of quantifying image realism and proposes principles for designing reliable functions that distinguish realistic from unrealistic data.

## Abstract

The last decade has seen tremendous progress in our ability to generate realistic-looking data, be it images, text, audio, or video. Here, we discuss the closely related problem of quantifying realism, that is, designing functions that can reliably tell realistic data from unrealistic data. This problem turns out to be significantly harder to solve and remains poorly understood, despite its prevalence in machine learning and recent breakthroughs in generative AI. Drawing on insights from algorithmic information theory, we discuss why this problem is challenging, why a good generative model alone is insufficient to solve it, and what a good solution would look like. In particular, we introduce the notion of a universal critic, which unlike adversarial critics does not require adversarial training. While universal critics are not immediately practical, they can serve both as a North Star for guiding practical implementations and as a tool for analyzing existing attempts to capture realism.