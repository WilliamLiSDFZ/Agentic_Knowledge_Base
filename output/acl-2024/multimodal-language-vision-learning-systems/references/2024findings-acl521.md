---
title: "GAOKAO-MM: A Chinese Human-Level Benchmark for Multimodal Models Evaluation"
source: "https://aclanthology.org/2024.findings-acl.521/"
pdf_url: ""
categories: ['multimodal-language-vision-learning-systems', 'nlp-benchmark-design-and-interpretability']
tags: ['multimodal-benchmark', 'vision-language-models', 'chinese', 'gaokao', 'evaluation']
venue: "ACL 2024"
tldr: "GAOKAO-MM is a challenging Chinese human-level multimodal benchmark derived from the national college entrance exam to evaluate large vision-language models."
---

# GAOKAO-MM: A Chinese Human-Level Benchmark for Multimodal Models Evaluation

**Source**: [https://aclanthology.org/2024.findings-acl.521/](https://aclanthology.org/2024.findings-acl.521/)

**TLDR**: GAOKAO-MM is a challenging Chinese human-level multimodal benchmark derived from the national college entrance exam to evaluate large vision-language models.

## Abstract

AbstractThe Large Vision-Language Models (LVLMs) have demonstrated great abilities in image perception and language understanding. However, existing datasets either focus solely on primary perception abilities and commonsense knowledge, or have a low level of text comprehension difficulty, which are insufficient to reflect the comprehensive capabilities of LVLMs, particularly in terms of Chinese language proficiency. We propose GAOKAO-MM, a multimodal benchmark based on the Chinese College Entrance Examination (GAOKAO), comprising of 8 subjects and 12 types of images, such as diagrams, function graphs, maps and photos. GAOKAO-MM derives from native Chinese context and sets human-level requirements for the model’s abilities, including perception, understanding, knowledge and reasoning. We evaluate 10 LVLMs and find that the accuracies of all of them are lower than 50%, with GPT-4-Vision (48.1%), Qwen-VL-Plus (41.2%) and Gemini-Pro-Vision (35.1%) ranking in the top three positions. The results of our multi-dimension analysis indicate that LVLMs have moderate distance towards Artificial General Intelligence (AGI) and provide insights facilitating the development of multilingual LVLMs. The dataset and evaluation code are available through: https://github.com/OpenMOSS/GAOKAO-MM