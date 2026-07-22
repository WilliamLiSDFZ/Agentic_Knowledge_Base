---
title: "Enhanced Language Model Truthfulness with Learnable Intervention and Uncertainty Expression"
source: "https://aclanthology.org/2024.findings-acl.737/"
pdf_url: ""
categories: ['llm-hallucination-detection-and-mitigation', 'llm-training-alignment-and-evaluation']
tags: ['hallucination-mitigation', 'truthfulness', 'llm', 'uncertainty', 'inference-time-intervention']
venue: "ACL 2024"
tldr: "This paper proposes learnable intervention and uncertainty expression methods to improve LLM truthfulness and reduce hallucination."
---

# Enhanced Language Model Truthfulness with Learnable Intervention and Uncertainty Expression

**Source**: [https://aclanthology.org/2024.findings-acl.737/](https://aclanthology.org/2024.findings-acl.737/)

**TLDR**: This paper proposes learnable intervention and uncertainty expression methods to improve LLM truthfulness and reduce hallucination.

## Abstract

AbstractLarge language models (LLMs) can generate long-form and coherent text, yet they often hallucinate facts, which undermines their reliability. To mitigate this issue, inference-time methods steer LLM representations toward the “truthful directions” previously learned for truth elicitation. However, applying these truthful directions with the same intensity fails to generalize across different query contexts. We propose LITO, a Learnable Intervention method for Truthfulness Optimization that automatically identifies the optimal intervention intensity tailored to each specific context. LITO explores a sequence of model generations based on increasing levels of intervention intensities. It selects the most accurate response or refuses to answer when the predictions are highly uncertain. Experiments on multiple LLMs and question-answering datasets demonstrate that LITO improves truthfulness while preserving task accuracy. The adaptive nature of LITO counters the limitations of one-size-fits-all intervention methods, maximizing truthfulness by reflecting the model’s internal knowledge only when it is confident. Our code is available at https://github.com/launchnlp/LITO.