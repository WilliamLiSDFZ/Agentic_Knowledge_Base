---
title: "Mitigating Hallucinations in Large Vision-Language Models with Instruction Contrastive Decoding"
source: "https://aclanthology.org/2024.findings-acl.937/"
categories: ['multimodal-language-vision-learning-systems', 'llm-hallucination-detection-and-mitigation']
tags: ['vision-language-models', 'hallucination', 'contrastive-decoding']
venue: "ACL 2024"
tldr: "Instruction Contrastive Decoding reduces hallucinations in large vision-language models by contrasting outputs from standard and distracted instruction prompts."
---

# Mitigating Hallucinations in Large Vision-Language Models with Instruction Contrastive Decoding

**Source**: [https://aclanthology.org/2024.findings-acl.937/](https://aclanthology.org/2024.findings-acl.937/)

**TLDR**: Instruction Contrastive Decoding reduces hallucinations in large vision-language models by contrasting outputs from standard and distracted instruction prompts.

## Abstract

AbstractLarge Vision-Language Models (LVLMs) are increasingly adept at generating contextually detailed and coherent responses from visual inputs. However, their application in multimodal decision-making and open-ended generation is hindered by a notable rate of hallucinations, where generated text inaccurately represents the visual contents. To address this issue, this paper introduces the Instruction Contrastive Decoding (ICD) method, a novel approach designed to reduce hallucinations during LVLM inference. Our method is inspired by our observation that what we call disturbance instructions significantly exacerbate hallucinations in multimodal fusion modules. ICD contrasts distributions from standard and instruction disturbance, thereby increasing alignment uncertainty and effectively subtracting hallucinated concepts from the original distribution. Through comprehensive experiments on discriminative benchmarks (POPE and MME) and a generative benchmark (LLaVa-Bench), we demonstrate that ICD significantly mitigates both object-level and attribute-level hallucinations. Moreover, our method not only addresses hallucinations but also significantly enhances the general perception and recognition capabilities of LVLMs.