---
title: "Tuning Large Multimodal Models for Videos using Reinforcement Learning from AI Feedback"
source: "https://aclanthology.org/2024.acl-long.52/"
categories: ['llm-training-alignment-and-evaluation']
tags: ['video-understanding', 'reinforcement-learning', 'multimodal-fine-tuning']
venue: "ACL 2024"
tldr: "Fine-tunes video large multimodal models using reinforcement learning from AI feedback to improve instruction-following."
---

# Tuning Large Multimodal Models for Videos using Reinforcement Learning from AI Feedback

**Source**: [https://aclanthology.org/2024.acl-long.52/](https://aclanthology.org/2024.acl-long.52/)

**TLDR**: Fine-tunes video large multimodal models using reinforcement learning from AI feedback to improve instruction-following.

## Abstract

AbstractRecent advancements in large language models have influenced the development of video large multimodal models (VLMMs). Previous approaches for VLMMs involve Supervised Fine-Tuning (SFT) with instruction-tuned datasets, integrating LLM with visual encoders, and additional learnable parameters. Here, aligning video with text, and vice versa, remains a challenge, primarily due to the insufficient quality and quantity of multimodal instruction-tune data compared to that of text-only. This discrepancy often results in alignments that poorly ground the video content. To address this, we present a novel alignment strategy that employs a multimodal AI system equipped with Reinforcement Learning from AI Feedback (RLAIF), providing self-preference feedback to refine itself and facilitating the alignment of video and text modalities. Our approach uniquely integrates detailed video descriptions as context into a multimodal AI system during the preference feedback generation to enrich the understanding of video content, a process we call context-aware reward modeling. Empirical evaluations on various video benchmarks demonstrate that our VLM-RLAIF outperforms existing approaches, including the SFT model. We commit to open-sourcing our code, models, and datasets to foster further research in this area.