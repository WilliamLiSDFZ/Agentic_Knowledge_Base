---
title: "TransFace: Unit-Based Audio-Visual Speech Synthesizer for Talking Head Translation"
source: "https://aclanthology.org/2024.findings-acl.593/"
pdf_url: ""
categories: ['speech-and-language-multimodal-generation-systems']
tags: ['talking-head-translation', 'discrete-units', 'audio-visual-speech']
venue: "ACL 2024"
tldr: "Introduces TransFace, a unit-based audio-visual speech synthesizer enabling high-quality talking head video translation across languages."
---

# TransFace: Unit-Based Audio-Visual Speech Synthesizer for Talking Head Translation

**Source**: [https://aclanthology.org/2024.findings-acl.593/](https://aclanthology.org/2024.findings-acl.593/)

**TLDR**: Introduces TransFace, a unit-based audio-visual speech synthesizer enabling high-quality talking head video translation across languages.

## Abstract

AbstractDirect speech-to-speech translation achieves high-quality results through the introduction of discrete units obtained from self-supervised learning. However, talking head translation, converting audio-visual speech (i.e., talking head video) from one language into another, still confronts several challenges compared to audio speech: (1) Existing methods invariably rely on cascading, synthesizing via both audio and text, resulting in delays and cascading errors. (2) Talking head translation has a limited set of reference frames. If the generated translation exceeds the length of the original speech, the video sequence needs to be supplemented by repeating frames, leading to jarring video transitions. In this work, we propose a model for talking head translation, TransFace, which can directly translate audio-visual speech into audio-visual speech in other languages. It consists of a speech-to-unit translation model to convert audio speech into discrete units and a unit-based audio-visual speech synthesizer, Unit2Lip, to re-synthesize synchronized audio-visual speech from discrete units in parallel. Furthermore, we introduce a Bounded Duration Predictor, ensuring isometric talking head translation and preventing duplicate reference frames. Experiments demonstrate that Unit2Lip significantly improves synchronization and boosts inference speed by a factor of 4.35 on LRS2. Additionally, TransFace achieves impressive BLEU scores of 61.93 and 47.55 for Es-En and Fr-En on LRS3-T and 100% isochronous translations. The samples are available at https://transface-demo.github.io .