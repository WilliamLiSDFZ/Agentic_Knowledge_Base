---
title: "MusicRL: Aligning Music Generation to Human Preferences"
source: "https://proceedings.mlr.press/v235/cideron24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/cideron24a/cideron24a.pdf"
categories: ['audio-and-music-generation-diffusion-models', 'large-language-model-alignment-and-capabilities']
tags: ['music-generation', 'reinforcement-learning-from-human-feedback', 'text-to-music']
venue: "ICML 2024"
tldr: "MusicRL fine-tunes a music generation model from human feedback to better align outputs with subjective user preferences."
---

# MusicRL: Aligning Music Generation to Human Preferences

**Source**: [https://proceedings.mlr.press/v235/cideron24a.html](https://proceedings.mlr.press/v235/cideron24a.html)

**TLDR**: MusicRL fine-tunes a music generation model from human feedback to better align outputs with subjective user preferences.

## Abstract

We propose MusicRL, the first music generation system finetuned from human feedback. Appreciation of text-to-music models is particularly subjective since the concept of musicality as well as the specific intention behind a caption are user-dependent (e.g. a caption such as “upbeat workout music” can map to a retro guitar solo or a technopop beat). Not only this makes supervised training of such models challenging, but it also calls for integrating continuous human feedback in their post-deployment finetuning. MusicRL is a pretrained autoregressive MusicLM model of discrete audio tokens finetuned with reinforcement learning to maximize sequence-level rewards. We design reward functions related specifically to text-adherence and audio quality with the help from selected raters, and use those to finetune MusicLM into MusicRL-R. We deploy MusicLM to users and collect a substantial dataset comprising 300,000 pairwise preferences. Using Reinforcement Learning from Human Feedback (RLHF), we train MusicRL-U, the first text-to-music model that incorporates human feedback at scale. Human evaluations show that both MusicRL-R and MusicRL-U are preferred to the baseline. Ultimately, MusicRL-RU combines the two approaches and results in the best model according to human raters. Ablation studies shed light on the musical attributes influencing human preferences, indicating that text adherence and quality only account for a part of it. This underscores the prevalence of subjectivity in musical appreciation and calls for further involvement of human listeners in the finetuning of music generation models. Samples can be found at google-research.github.io/seanet/musiclm/rlhf/.