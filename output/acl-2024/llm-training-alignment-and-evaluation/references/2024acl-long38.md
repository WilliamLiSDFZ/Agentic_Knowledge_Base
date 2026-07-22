---
title: "Multimodal Instruction Tuning with Conditional Mixture of LoRA"
source: "https://aclanthology.org/2024.acl-long.38/"
categories: ['multimodal-language-vision-learning-systems', 'llm-training-alignment-and-evaluation']
tags: ['multimodal-instruction-tuning', 'mixture-of-lora', 'zero-shot-generalization']
venue: "ACL 2024"
tldr: "Proposes conditional mixture of LoRA for multimodal instruction tuning to improve zero-shot generalization in MLLMs."
---

# Multimodal Instruction Tuning with Conditional Mixture of LoRA

**Source**: [https://aclanthology.org/2024.acl-long.38/](https://aclanthology.org/2024.acl-long.38/)

**TLDR**: Proposes conditional mixture of LoRA for multimodal instruction tuning to improve zero-shot generalization in MLLMs.

## Abstract

AbstractMultimodal Large Language Models (MLLMs) have demonstrated remarkable proficiency in diverse tasks across different domains, with an increasing focus on improving their zero-shot generalization capabilities for unseen multimodal tasks. Multimodal instruction tuning has emerged as a successful strategy for achieving zero-shot generalization by fine-tuning pre-trained models on diverse multimodal tasks through instructions. As MLLMs grow in complexity and size, the need for parameter-efficient fine-tuning methods like Low-Rank Adaption (LoRA), which fine-tunes with a minimal set of parameters, becomes essential. However, applying LoRA in multimodal instruction tuning presents the challenge of task interference, which leads to performance degradation, especially when dealing with a broad array of multimodal tasks. To address this, this paper introduces a novel approach that integrates multimodal instruction tuning with Conditional Mixture-of-LoRA (MixLoRA). It innovates upon LoRA by dynamically constructing low-rank adaptation matrices tailored to the unique demands of each input instance, aiming to mitigate task interference. Experimental results on various multimodal evaluation datasets indicate that MixLoRA not only outperforms the conventional LoRA with the same or even higher ranks, demonstrating its efficacy and adaptability in diverse multimodal tasks.