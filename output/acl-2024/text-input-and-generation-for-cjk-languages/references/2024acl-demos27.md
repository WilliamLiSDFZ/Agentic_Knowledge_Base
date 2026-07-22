---
title: "Proofread: Fixes All Errors with One Tap"
source: "https://aclanthology.org/2024.acl-demos.27/"
pdf_url: ""
categories: ['text-input-and-generation-for-cjk-languages', 'multimodal-language-vision-learning-systems']
tags: ['GBoard', 'proofreading', 'LLM', 'mobile-keyboard', 'text-correction']
venue: "ACL 2024"
tldr: "Proofread is a Gboard feature using LLMs to fix sentence- and paragraph-level errors with a single tap on mobile."
---

# Proofread: Fixes All Errors with One Tap

**Source**: [https://aclanthology.org/2024.acl-demos.27/](https://aclanthology.org/2024.acl-demos.27/)

**TLDR**: Proofread is a Gboard feature using LLMs to fix sentence- and paragraph-level errors with a single tap on mobile.

## Abstract

AbstractThe impressive capabilities in Large Language Models (LLMs) provide a powerful approach to reimagine users’ typing experience. This paper demonstrates the Proofread feature in Gboard, a virtual keyboard running on mobile phones. Proofread enables seamless sentence-level and paragraph-level corrections with a single tap. We describe the complete system in this paper, from data generation, metrics design to model tuning and deployment. To obtain models with sufficient quality, we implement a careful data synthetic pipeline tailored to online use cases, design multifaceted metrics, employ a two-stage tuning approach to acquire the dedicated LLM for the feature: the Supervised Fine Tuning (SFT) for foundational quality, followed by the Reinforcement Learning (RL) tuning approach for targeted refinement. Specifically, we find sequential tuning on Rewrite and proofread tasks yields the best quality in SFT stage, and propose global and direct rewards in the RL tuning stage to seek further improvement. Extensive experiments on a human-labeled golden set showed our tuned PaLM2-XS model achieved 85.56% good ratio. We launched the feature to Pixel 8 devices by serving the model on TPU v5 in Google Cloud, with thousands of daily active users. Serving latency was significantly reduced by quantization, bucket inference, text segmentation, and speculative decoding. Our demo could be seen in Youtube.