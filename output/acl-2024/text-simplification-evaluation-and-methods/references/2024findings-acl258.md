---
title: "Evaluating the Smooth Control of Attribute Intensity in Text Generation with LLMs"
source: "https://aclanthology.org/2024.findings-acl.258/"
pdf_url: ""
categories: ['text-simplification-evaluation-and-methods', 'llm-training-alignment-and-evaluation']
tags: ['text-generation', 'attribute-control', 'intensity', 'LLM', 'evaluation']
venue: "ACL 2024"
tldr: "Evaluates LLMs' ability to smoothly control attribute intensity in text generation across diverse writing scenarios."
---

# Evaluating the Smooth Control of Attribute Intensity in Text Generation with LLMs

**Source**: [https://aclanthology.org/2024.findings-acl.258/](https://aclanthology.org/2024.findings-acl.258/)

**TLDR**: Evaluates LLMs' ability to smoothly control attribute intensity in text generation across diverse writing scenarios.

## Abstract

AbstractControlling the attribute intensity of text generation is crucial across scenarios (e.g., writing conciseness, chatting emotion, and explanation clarity). The remarkable capabilities of large language models (LLMs) have revolutionized text generation, prompting us to explore such smooth control of LLM generation. Specifically, we propose metrics to assess the range, calibration, and consistency of the generated text’s attribute intensity in response to varying control values, as well as its relevance to the intended context. To quantify the attribute intensity and context relevance, we leverage an Elo rating system and GPT4, respectively, both renowned for their robust alignment with human judgment. We look into two viable training-free methods for achieving smooth control of LLMs: (1) Prompting with semantic shifters, and (2) Modifying internal model representations. The evaluations of these two methods are conducted on 5 different attributes with various models.