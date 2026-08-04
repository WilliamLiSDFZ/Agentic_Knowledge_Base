---
title: "AND: Audio Network Dissection for Interpreting Deep Acoustic Models"
source: "https://proceedings.mlr.press/v235/wu24q.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/wu24q/wu24q.pdf"
categories: ['ai-explainability-uncertainty-human-decision-making', 'probabilistic-generating-circuits-research']
tags: ['network-dissection', 'acoustic-models', 'neuron-interpretability', 'audio-deep-learning', 'explainability']
venue: "ICML 2024"
tldr: "Introduces AND, a framework for neuron-level interpretation of deep acoustic models by identifying neurons responsive to specific audio patterns."
---

# AND: Audio Network Dissection for Interpreting Deep Acoustic Models

**Source**: [https://proceedings.mlr.press/v235/wu24q.html](https://proceedings.mlr.press/v235/wu24q.html)

**TLDR**: Introduces AND, a framework for neuron-level interpretation of deep acoustic models by identifying neurons responsive to specific audio patterns.

## Abstract

Neuron-level interpretations aim to explain network behaviors and properties by investigating neurons responsive to specific perceptual or structural input patterns. Although there is emerging work in the vision and language domains, none is explored for acoustic models. To bridge the gap, we introduce AND, the first Audio Network Dissection framework that automatically establishes natural language explanations of acoustic neurons based on highly responsive audio. AND features the use of LLMs to summarize mutual acoustic features and identities among audio. Extensive experiments are conducted to verify AND’s precise and informative descriptions. In addition, we highlight two acoustic model behaviors with analysis by AND. First, models discriminate audio with a combination of basic acoustic features rather than high-level abstract concepts. Second, training strategies affect neuron behaviors. Supervised training guides neurons to gradually narrow their attention, while self-supervised learning encourages neurons to be polysemantic for exploring high-level features. Finally, we demonstrate a potential use of AND in audio model unlearning by conducting concept-specific pruning based on the descriptions.