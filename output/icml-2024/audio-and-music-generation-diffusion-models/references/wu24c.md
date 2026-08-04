---
title: "Adaptive Accompaniment with ReaLchords"
source: "https://proceedings.mlr.press/v235/wu24c.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/wu24c/wu24c.pdf"
categories: ['audio-and-music-generation-diffusion-models', 'online-learning-and-sequential-decision-making']
tags: ['online-music-generation', 'chord-generation', 'reinforcement-learning', 'adaptive-accompaniment']
venue: "ICML 2024"
tldr: "ReaLchords is an online RL-based chord generation model that adapts in real-time to accompany musicians during live performance."
---

# Adaptive Accompaniment with ReaLchords

**Source**: [https://proceedings.mlr.press/v235/wu24c.html](https://proceedings.mlr.press/v235/wu24c.html)

**TLDR**: ReaLchords is an online RL-based chord generation model that adapts in real-time to accompany musicians during live performance.

## Abstract

Jamming requires coordination, anticipation, and collaborative creativity between musicians. Current generative models of music produce expressive output but are not able to generate in an online manner, meaning simultaneously with other musicians (human or otherwise). We propose ReaLchords, an online generative model for improvising chord accompaniment to user melody. We start with an online model pretrained by maximum likelihood, and use reinforcement learning to finetune the model for online use. The finetuning objective leverages both a novel reward model that provides feedback on both harmonic and temporal coherency between melody and chord, and a divergence term that implements a novel type of distillation from a teacher model that can see the future melody. Through quantitative experiments and listening tests, we demonstrate that the resulting model adapts well to unfamiliar input and produce fitting accompaniment. ReaLchords opens the door to live jamming, as well as simultaneous co-creation in other modalities.