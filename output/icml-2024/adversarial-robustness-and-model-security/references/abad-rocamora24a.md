---
title: "Revisiting Character-level Adversarial Attacks for Language Models"
source: "https://proceedings.mlr.press/v235/abad-rocamora24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/abad-rocamora24a/abad-rocamora24a.pdf"
categories: ['adversarial-robustness-and-model-security']
tags: ['character-level-attacks', 'adversarial-nlp', 'beam-search']
venue: "ICML 2024"
tldr: "Revisits character-level adversarial attacks on language models, showing they can be competitive with token-level attacks while better preserving semantics."
---

# Revisiting Character-level Adversarial Attacks for Language Models

**Source**: [https://proceedings.mlr.press/v235/abad-rocamora24a.html](https://proceedings.mlr.press/v235/abad-rocamora24a.html)

**TLDR**: Revisits character-level adversarial attacks on language models, showing they can be competitive with token-level attacks while better preserving semantics.

## Abstract

Adversarial attacks in Natural Language Processing apply perturbations in the character or token levels. Token-level attacks, gaining prominence for their use of gradient-based methods, are susceptible to altering sentence semantics, leading to invalid adversarial examples. While character-level attacks easily maintain semantics, they have received less attention as they cannot easily adopt popular gradient-based methods, and are thought to be easy to defend. Challenging these beliefs, we introduce Charmer, an efficient query-based adversarial attack capable of achieving high attack success rate (ASR) while generating highly similar adversarial examples. Our method successfully targets both small (BERT) and large (Llama 2) models. Specifically, on BERT with SST-2, Charmer improves the ASR in $4.84$% points and the USE similarity in $8$% points with respect to the previous art. Our implementation is available in https://github.com/LIONS-EPFL/Charmer.