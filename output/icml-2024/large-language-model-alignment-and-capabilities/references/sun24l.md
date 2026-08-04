---
title: "video-SALMONN: Speech-Enhanced Audio-Visual Large Language Models"
source: "https://proceedings.mlr.press/v235/sun24l.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/sun24l/sun24l.pdf"
categories: ['large-language-model-alignment-and-capabilities']
tags: ['audio-visual', 'speech-understanding', 'multimodal-llm']
venue: "ICML 2024"
tldr: "video-SALMONN is an end-to-end audio-visual LLM that integrates speech understanding into video comprehension for unified multimodal processing."
---

# video-SALMONN: Speech-Enhanced Audio-Visual Large Language Models

**Source**: [https://proceedings.mlr.press/v235/sun24l.html](https://proceedings.mlr.press/v235/sun24l.html)

**TLDR**: video-SALMONN is an end-to-end audio-visual LLM that integrates speech understanding into video comprehension for unified multimodal processing.

## Abstract

Speech understanding as an element of the more generic video understanding using audio-visual large language models (av-LLMs) is a crucial yet understudied aspect. This paper proposes video-SALMONN, a single end-to-end av-LLM for video processing, which can understand not only visual frame sequences, audio events and music, but speech as well. To obtain fine-grained temporal information required by speech understanding, while keeping efficient for other video elements, this paper proposes a novel multi-resolution causal Q-Former (MRC Q-Former) structure to connect pre-trained audio-visual encoders and the backbone large language model. Moreover, dedicated training approaches including the diversity loss and the unpaired audio-visual mixed training scheme are proposed to avoid frames or modality dominance. On the introduced audio-visual evaluation benchmark, video-SALMONN achieves more than 25% absolute accuracy improvements on the video-QA task and over 30% absolute accuracy improvements on audio-visual QA tasks with human speech. In addition, video-SALMONN demonstrates remarkable video comprehension and reasoning abilities on tasks that are unprecedented by other av-LLMs. Our training code and model checkpoints are available at https://github.com/bytedance/SALMONN/