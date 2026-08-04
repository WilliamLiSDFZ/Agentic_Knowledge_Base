---
title: "Creative Text-to-Audio Generation via Synthesizer Programming"
source: "https://proceedings.mlr.press/v235/cherep24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/cherep24a/cherep24a.pdf"
categories: ['audio-and-music-generation-diffusion-models', 'llm-driven-automated-system-optimization']
tags: ['text-to-audio', 'synthesizer-programming', 'interpretable-audio-generation']
venue: "ICML 2024"
tldr: "A text-to-audio generation method uses synthesizer programming to produce interpretable and editable audio outputs from natural language descriptions."
---

# Creative Text-to-Audio Generation via Synthesizer Programming

**Source**: [https://proceedings.mlr.press/v235/cherep24a.html](https://proceedings.mlr.press/v235/cherep24a.html)

**TLDR**: A text-to-audio generation method uses synthesizer programming to produce interpretable and editable audio outputs from natural language descriptions.

## Abstract

Neural audio synthesis methods now allow specifying ideas in natural language. However, these methods produce results that cannot be easily tweaked, as they are based on large latent spaces and up to billions of uninterpretable parameters. We propose a text-to-audio generation method that leverages a virtual modular sound synthesizer with only 78 parameters. Synthesizers have long been used by skilled sound designers for media like music and film due to their flexibility and intuitive controls. Our method, CTAG, iteratively updates a synthesizer’s parameters to produce high-quality audio renderings of text prompts that can be easily inspected and tweaked. Sounds produced this way are also more abstract, capturing essential conceptual features over fine-grained acoustic details, akin to how simple sketches can vividly convey visual concepts. Our results show how CTAG produces sounds that are distinctive, perceived as artistic, and yet similarly identifiable to recent neural audio synthesis models, positioning it as a valuable and complementary tool.