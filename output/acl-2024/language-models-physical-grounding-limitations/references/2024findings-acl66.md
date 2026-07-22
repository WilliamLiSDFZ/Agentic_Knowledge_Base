---
title: "CoLLaVO: Crayon Large Language and Vision mOdel"
source: "https://aclanthology.org/2024.findings-acl.66/"
categories: ['multimodal-language-vision-learning-systems', 'language-models-physical-grounding-limitations']
tags: ['vision-language-model', 'object-understanding', 'instruction-tuning', 'multimodal', 'image-comprehension']
venue: "ACL 2024"
tldr: "CoLLaVO is a vision-language model that improves object-level image understanding through crayon-based visual instruction tuning."
---

# CoLLaVO: Crayon Large Language and Vision mOdel

**Source**: [https://aclanthology.org/2024.findings-acl.66/](https://aclanthology.org/2024.findings-acl.66/)

**TLDR**: CoLLaVO is a vision-language model that improves object-level image understanding through crayon-based visual instruction tuning.

## Abstract

AbstractThe remarkable success of Large Language Models (LLMs) and instruction tuning drives the evolution of Vision Language Models (VLMs) towards a versatile general-purpose model. Yet, it remains unexplored whether current VLMs genuinely possess quality object-level image understanding capabilities determined from ‘what objects are in the image?’ or ‘which object corresponds to a specified bounding box?’. Our findings reveal that the image understanding capabilities of current VLMs are strongly correlated with their zero-shot performance on vision language (VL) tasks. This suggests that prioritizing basic image understanding is crucial for VLMs to excel at VL tasks. To enhance object-level image understanding, we propose Crayon Large Language and Vision mOdel (CoLLaVO), which incorporates instruction tuning with Crayon Prompt as a new visual prompt tuning scheme based on panoptic color maps. Furthermore, we present a learning strategy of Dual QLoRA to preserve object-level image understanding without forgetting it during visual instruction tuning, thereby achieving a significant leap in numerous VL benchmarks in a zero-shot setting.