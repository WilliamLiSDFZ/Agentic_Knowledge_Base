---
title: "Multilingual Instruction Tuning With Just a Pinch of Multilinguality"
source: "https://aclanthology.org/2024.findings-acl.136/"
pdf_url: ""
categories: ['language-technology-cultural-linguistic-diversity', 'llm-training-alignment-and-evaluation']
tags: ['multilingual', 'instruction-tuning', 'cross-lingual-transfer']
venue: "ACL 2024"
tldr: "A small amount of multilingual data during instruction tuning suffices to enable strong multilingual instruction-following in LLMs."
---

# Multilingual Instruction Tuning With Just a Pinch of Multilinguality

**Source**: [https://aclanthology.org/2024.findings-acl.136/](https://aclanthology.org/2024.findings-acl.136/)

**TLDR**: A small amount of multilingual data during instruction tuning suffices to enable strong multilingual instruction-following in LLMs.

## Abstract

AbstractAs instruction-tuned large language models (LLMs) gain global adoption, their ability to follow instructions in multiple languages becomes increasingly crucial. In this work, we investigate how multilinguality during instruction tuning of a multilingual LLM affects instruction-following across languages from the pre-training corpus. We first show that many languages transfer some instruction-following capabilities to other languages from even monolingual tuning. Furthermore, we find that only 40 multilingual examples integrated in an English tuning set substantially improve multilingual instruction-following, both in seen and unseen languages during tuning. In general, we observe that models tuned on multilingual mixtures exhibit comparable or superior performance in multiple languages compared to monolingually tuned models, despite training on 10x fewer examples in those languages. Finally, we find that diversifying the instruction tuning set with even just 2-4 languages significantly improves cross-lingual generalization. Our results suggest that building massively multilingual instruction-tuned models can be done with only a very small set of multilingual instruction-responses.