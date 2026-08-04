---
title: "Unifying Image Processing as Visual Prompting Question Answering"
source: "https://proceedings.mlr.press/v235/liu24k.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/liu24k/liu24k.pdf"
categories: ['image-quality-assessment-and-super-resolution']
tags: ['image-processing', 'visual-prompting', 'question-answering']
venue: "ICML 2024"
tldr: "A unified framework is proposed that treats diverse image processing tasks as visual prompting question answering using a single model."
---

# Unifying Image Processing as Visual Prompting Question Answering

**Source**: [https://proceedings.mlr.press/v235/liu24k.html](https://proceedings.mlr.press/v235/liu24k.html)

**TLDR**: A unified framework is proposed that treats diverse image processing tasks as visual prompting question answering using a single model.

## Abstract

Image processing is a fundamental task in computer vision, which aims at enhancing image quality and extracting essential features for subsequent vision applications. Traditionally, task-specific models are developed for individual tasks and designing such models requires distinct expertise. Building upon the success of large language models (LLMs) in natural language processing (NLP), there is a similar trend in computer vision, which focuses on developing large-scale models through pretraining and in-context learning. This paradigm shift reduces the reliance on task-specific models, yielding a powerful unified model to deal with various tasks. However, these advances have predominantly concentrated on high-level vision tasks, with less attention paid to low-level vision tasks. To address this issue, we propose a universal model for general image processing that covers image restoration, image enhancement, image feature extraction tasks, etc. Our proposed framework, named PromptGIP, unifies these diverse image processing tasks within a universal framework. Inspired by NLP question answering (QA) techniques, we employ a visual prompting question answering paradigm. Specifically, we treat the input-output image pair as a structured question-answer sentence, thereby reprogramming the image processing task as a prompting QA problem. PromptGIP can undertake diverse cross-domain tasks using provided visual prompts, eliminating the need for task-specific finetuning. Capable of handling up to 15 different image processing tasks, PromptGIP represents a versatile and adaptive approach to general image processing. While PromptGIP has demonstrated a certain degree of out-of-domain task generalization capability, further research is expected to fully explore its more powerful emergent generalization. Codes will be available at https://github.com/lyh-18/PromptGIP.