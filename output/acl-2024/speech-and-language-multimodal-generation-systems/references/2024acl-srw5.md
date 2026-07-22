---
title: "Speech-to-Speech Translation with Discrete-Unit-Based Style Transfer"
source: "https://aclanthology.org/2024.acl-srw.5/"
pdf_url: ""
categories: ['speech-and-language-multimodal-generation-systems']
tags: ['speech-to-speech-translation', 'style-transfer', 'discrete-units']
venue: "ACL 2024"
tldr: "Proposes a discrete-unit-based style transfer method to preserve speaker timbre in direct speech-to-speech translation."
---

# Speech-to-Speech Translation with Discrete-Unit-Based Style Transfer

**Source**: [https://aclanthology.org/2024.acl-srw.5/](https://aclanthology.org/2024.acl-srw.5/)

**TLDR**: Proposes a discrete-unit-based style transfer method to preserve speaker timbre in direct speech-to-speech translation.

## Abstract

AbstractDirect speech-to-speech translation (S2ST) with discrete self-supervised representations has achieved remarkable accuracy, but is unable to preserve the speaker timbre of the source speech. Meanwhile, the scarcity of high-quality speaker-parallel data poses a challenge for learning style transfer during translation. We design an S2ST pipeline with style-transfer capability on the basis of discrete self-supervised speech representations and codec units. The acoustic language model we introduce for style transfer leverages self-supervised in-context learning, acquiring style transfer ability without relying on any speaker-parallel data, thereby overcoming data scarcity. By using extensive training data, our model achieves zero-shot cross-lingual style transfer on previously unseen source languages. Experiments show that our model generates translated speeches with high fidelity and speaker similarity. Audio samples are available at http://stylelm.github.io/ .