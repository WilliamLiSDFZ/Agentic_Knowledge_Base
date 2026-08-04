---
title: "UniAudio: Towards Universal Audio Generation with Large Language Models"
source: "https://proceedings.mlr.press/v235/yang24x.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/yang24x/yang24x.pdf"
categories: ['audio-and-music-generation-diffusion-models', 'large-language-model-alignment-and-capabilities']
tags: ['audio-generation', 'large-language-models', 'universal-model']
venue: "ICML 2024"
tldr: "UniAudio is a universal audio generation model leveraging large language models to handle diverse audio generation tasks in a unified framework."
---

# UniAudio: Towards Universal Audio Generation with Large Language Models

**Source**: [https://proceedings.mlr.press/v235/yang24x.html](https://proceedings.mlr.press/v235/yang24x.html)

**TLDR**: UniAudio is a universal audio generation model leveraging large language models to handle diverse audio generation tasks in a unified framework.

## Abstract

Audio generation is a major branch of generative AI research. Compared with prior works in this area that are commonly task-specific with heavy domain knowledge, this paper advocates building universal audio generation models that can handle various tasks in a unified manner. As recent research on large language models (LLMs) has demonstrated their strong ability to handle multiple tasks, this work presents UniAudio, an LLM-based audio generation model that supports a wide range of audio generation tasks. Based on various input conditions, such as phoneme, text description, or audio itself, UniAudio can generate speech, sound, music, and singing voice. The proposed UniAudio is built with 100k hours of multi-source open-available audio data and is scaled to 1B parameters. The audio tokenization method and language model architecture are also specifically designed for both performance and efficiency. Experimentally, UniAuido supports 11 audio generation tasks and achieves competitive results on all tasks consistently. We also show that UniAudio can support new tasks seamlessly via simple fine-tuning.