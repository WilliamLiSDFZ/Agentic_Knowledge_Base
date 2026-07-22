---
title: "DiffChat: Learning to Chat with Text-to-Image Synthesis Models for Interactive Image Creation"
source: "https://aclanthology.org/2024.findings-acl.522/"
categories: ['multimodal-language-vision-learning-systems', 'text-diffusion-for-content-generation']
tags: ['text-to-image', 'LLM-alignment', 'interactive-generation', 'prompt-editing', 'diffusion']
venue: "ACL 2024"
tldr: "DiffChat aligns LLMs to interactively refine text-to-image synthesis prompts for iterative image creation."
---

# DiffChat: Learning to Chat with Text-to-Image Synthesis Models for Interactive Image Creation

**Source**: [https://aclanthology.org/2024.findings-acl.522/](https://aclanthology.org/2024.findings-acl.522/)

**TLDR**: DiffChat aligns LLMs to interactively refine text-to-image synthesis prompts for iterative image creation.

## Abstract

AbstractWe present DiffChat, a novel method to align Large Language Models (LLMs) to “chat” with prompt-as-input Text-to-Image Synthesis (TIS)models (e.g., Stable Diffusion) for interactive image creation. Given a raw prompt/image and a user-specified instruction, DiffChat can effectively make appropriate modifications and generate the target prompt, which can be leveraged to create the target image of high quality. To achieve this, we first collect an instruction-following prompt engineering dataset named InstructPE for the supervised training of DiffChat.Next, we propose a reinforcement learning framework with the feedback of three core criteria for image creation, i.e., aesthetics, user preference and content integrity. It involves an action-space dynamic modification technique to obtain more relevant positive samples and harder negative samples during the off-policy sampling. Content integrity is also introduced into the value estimation function for further improvement of produced images. Our method can exhibit superior performance than baseline models and strong competitors based on both automatic and human evaluations, which fully demonstrates its effectiveness.