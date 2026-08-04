---
title: "A Language Model’s Guide Through Latent Space"
source: "https://proceedings.mlr.press/v235/von-rutte24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/von-rutte24a/von-rutte24a.pdf"
categories: ['llm-geometry-and-interpretability-research', 'large-language-model-alignment-and-capabilities']
tags: ['concept-guidance', 'language-models', 'latent-space', 'interpretability', 'activation-steering']
venue: "ICML 2024"
tldr: "Explores concept guidance in language models by probing hidden representations for concept vectors to steer model behavior beyond truthfulness."
---

# A Language Model’s Guide Through Latent Space

**Source**: [https://proceedings.mlr.press/v235/von-rutte24a.html](https://proceedings.mlr.press/v235/von-rutte24a.html)

**TLDR**: Explores concept guidance in language models by probing hidden representations for concept vectors to steer model behavior beyond truthfulness.

## Abstract

Concept guidance has emerged as a cheap and simple way to control the behavior of language models by probing their hidden representations for concept vectors and using them to perturb activations at inference time. While the focus of previous work has largely been on truthfulness, in this paper we extend this framework to a richer set of concepts such as appropriateness, humor, creativity and quality, and explore to what degree current detection and guidance strategies work in these challenging settings. To facilitate evaluation, we develop a novel metric for concept guidance that takes into account both the success of concept elicitation as well as the potential degradation in fluency of the guided model. Our extensive experiments reveal that while some concepts such as truthfulness more easily allow for guidance with current techniques, novel concepts such as appropriateness or humor either remain difficult to elicit, need extensive tuning to work, or even experience confusion. Moreover, we find that probes with optimal detection accuracies do not necessarily make for the optimal guides, contradicting previous observations for truthfulness. Our work warrants a deeper investigation into the interplay between detectability, guidability, and the nature of the concept, and we hope that our rich experimental test-bed for guidance research inspires stronger follow-up approaches.