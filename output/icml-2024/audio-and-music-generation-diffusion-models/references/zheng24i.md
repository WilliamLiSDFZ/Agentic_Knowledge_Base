---
title: "BAT: Learning to Reason about Spatial Sounds with Large Language Models"
source: "https://proceedings.mlr.press/v235/zheng24i.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/zheng24i/zheng24i.pdf"
categories: ['audio-and-music-generation-diffusion-models']
tags: ['spatial-sound', 'binaural-audio', 'large-language-models', 'acoustic-reasoning']
venue: "ICML 2024"
tldr: "BAT combines binaural acoustic scene analysis with large language model reasoning to enable spatial sound understanding and reasoning."
---

# BAT: Learning to Reason about Spatial Sounds with Large Language Models

**Source**: [https://proceedings.mlr.press/v235/zheng24i.html](https://proceedings.mlr.press/v235/zheng24i.html)

**TLDR**: BAT combines binaural acoustic scene analysis with large language model reasoning to enable spatial sound understanding and reasoning.

## Abstract

Spatial sound reasoning is a fundamental human skill, enabling us to navigate and interpret our surroundings based on sound. In this paper we present BAT, which combines the spatial sound perception ability of a binaural acoustic scene analysis model with the natural language reasoning capabilities of a large language model (LLM) to replicate this innate ability. To address the lack of existing datasets of in-the-wild spatial sounds, we synthesized a binaural audio dataset using AudioSet and SoundSpaces 2.0. Next, we developed SpatialSoundQA, a spatial sound-based question-answering dataset, offering a range of QA tasks that train BAT in various aspects of spatial sound perception and reasoning. The acoustic front end encoder of BAT is a novel spatial audio encoder named Spatial Audio Spectrogram Transformer, or Spatial-AST, which by itself achieves strong performance across sound event detection, spatial localization, and distance estimation. By integrating Spatial-AST with LLaMA-2 7B model, BAT transcends standard Sound Event Localization and Detection (SELD) tasks, enabling the model to reason about the relationships between the sounds in its environment. Our experiments demonstrate BAT’s superior performance on both spatial sound perception and reasoning, showcasing the immense potential of LLMs in navigating and interpreting complex spatial audio environments.