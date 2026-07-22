---
title: "Evaluating Robustness of Generative Search Engine on Adversarial Factoid Questions"
source: "https://aclanthology.org/2024.findings-acl.633/"
categories: ['llm-security-robustness-and-detection', 'llm-hallucination-detection-and-mitigation']
tags: ['generative-search', 'adversarial-robustness', 'retrieval-augmented-generation']
venue: "ACL 2024"
tldr: "Evaluates the robustness of generative search engines against adversarial factoid questions that can mislead LLM responses."
---

# Evaluating Robustness of Generative Search Engine on Adversarial Factoid Questions

**Source**: [https://aclanthology.org/2024.findings-acl.633/](https://aclanthology.org/2024.findings-acl.633/)

**TLDR**: Evaluates the robustness of generative search engines against adversarial factoid questions that can mislead LLM responses.

## Abstract

AbstractGenerative search engines have the potential to transform how people seek information online, but generated responses from existing large language models (LLMs)-backed generative search engines may not always be accurate. Nonetheless, retrieval-augmented generation exacerbates safety concerns, since adversaries may successfully evade the entire system by subtly manipulating the most vulnerable part of a claim. To this end, we propose evaluating the robustness of generative search engines in the realistic and high-risk setting, where adversaries have only black-box system access and seek to deceive the model into returning incorrect responses. Through a comprehensive human evaluation of various generative search engines, such as Bing Chat, PerplexityAI, and YouChat across diverse queries, we demonstrate the effectiveness of adversarial factual questions in inducing incorrect responses. Moreover, retrieval-augmented generation exhibits a higher susceptibility to factual errors compared to LLMs without retrieval. These findings highlight the potential security risks of these systems and emphasize the need for rigorous evaluation before deployment. The dataset and code will be publicly available.