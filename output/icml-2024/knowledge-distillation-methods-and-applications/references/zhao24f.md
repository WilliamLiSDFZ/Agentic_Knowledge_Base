---
title: "VideoPrism: A Foundational Visual Encoder for Video Understanding"
source: "https://proceedings.mlr.press/v235/zhao24f.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/zhao24f/zhao24f.pdf"
categories: ['transformer-architecture-efficiency-and-scaling', 'knowledge-distillation-methods-and-applications']
tags: ['video-understanding', 'visual-encoder', 'pretraining']
venue: "ICML 2024"
tldr: "Introduces VideoPrism, a general-purpose video encoder pretrained on heterogeneous video-caption data for diverse video understanding tasks."
---

# VideoPrism: A Foundational Visual Encoder for Video Understanding

**Source**: [https://proceedings.mlr.press/v235/zhao24f.html](https://proceedings.mlr.press/v235/zhao24f.html)

**TLDR**: Introduces VideoPrism, a general-purpose video encoder pretrained on heterogeneous video-caption data for diverse video understanding tasks.

## Abstract

We introduce VideoPrism, a general-purpose video encoder that tackles diverse video understanding tasks with a single frozen model. We pretrain VideoPrism on a heterogeneous corpus containing 36M high-quality video-caption pairs and 582M video clips with noisy parallel text (e.g., ASR transcripts). The pretraining approach improves upon masked autoencoding by global-local distillation of semantic video embeddings and a token shuffling scheme, enabling VideoPrism to focus primarily on the video modality while leveraging the invaluable text associated with videos. We extensively test VideoPrism on four broad groups of video understanding tasks, from web video question answering to CV for science, achieving state-of-the-art performance on 31 out of 33 video understanding benchmarks.