---
title: "Mitigating Hallucinations in Large Vision-Language Models (LVLMs) via Language-Contrastive Decoding (LCD)"
source: "https://aclanthology.org/2024.findings-acl.359/"
pdf_url: ""
categories: ['multimodal-language-vision-learning-systems', 'llm-hallucination-detection-and-mitigation']
tags: ['vision-language-models', 'hallucination', 'contrastive-decoding', 'object-hallucination', 'LVLM']
venue: "ACL 2024"
tldr: "Introduces Language-Contrastive Decoding to mitigate object hallucinations in Large Vision-Language Models by reducing over-reliance on language priors."
---

# Mitigating Hallucinations in Large Vision-Language Models (LVLMs) via Language-Contrastive Decoding (LCD)

**Source**: [https://aclanthology.org/2024.findings-acl.359/](https://aclanthology.org/2024.findings-acl.359/)

**TLDR**: Introduces Language-Contrastive Decoding to mitigate object hallucinations in Large Vision-Language Models by reducing over-reliance on language priors.

## Abstract

AbstractLarge Vision-Language Models (LVLMs) are an extension of Large Language Models (LLMs) that facilitate processing both image and text inputs, expanding AI capabilities. However, LVLMs struggle with object hallucinations due to their reliance on text cues and learned object co-occurrence biases. While most research quantifies these hallucinations, mitigation strategies are still lacking. Our study introduces a Language Contrastive Decoding (LCD) algorithm that adjusts LVLM outputs based on LLM distribution confidence levels, effectively reducing object hallucinations. We demonstrate the advantages of LCD in leading LVLMs, showing up to %4 improvement in POPE F1 scores and up to %36 reduction in CHAIR scores on the COCO validation set, while also improving captioning quality scores. Our method effectively improves LVLMs without needing complex post-processing or retraining, and is easily applicable to different models. Our findings highlight the potential of further exploration of LVLM-specific decoding algorithms.