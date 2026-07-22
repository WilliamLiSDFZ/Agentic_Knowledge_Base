---
title: "TempCompass: Do Video LLMs Really Understand Videos?"
source: "https://aclanthology.org/2024.findings-acl.517/"
pdf_url: ""
categories: ['multimodal-language-vision-learning-systems', 'social-ai-temporal-dynamics-evaluation']
tags: ['video-LLMs', 'temporal-perception', 'benchmark']
venue: "ACL 2024"
tldr: "Presents TempCompass, a benchmark evaluating the temporal perception ability of video large language models."
---

# TempCompass: Do Video LLMs Really Understand Videos?

**Source**: [https://aclanthology.org/2024.findings-acl.517/](https://aclanthology.org/2024.findings-acl.517/)

**TLDR**: Presents TempCompass, a benchmark evaluating the temporal perception ability of video large language models.

## Abstract

AbstractRecently, there is a surge in interest surrounding video large language models (Video LLMs). However, existing benchmarks fail to provide a comprehensive feedback on the temporal perception ability of Video LLMs. On the one hand, most of them are unable to distinguish between different temporal aspects (e.g., speed, direction) and thus cannot reflect the nuanced performance on these specific aspects. On the other hand, they are limited in the diversity of task formats (e.g., only multi-choice QA), which hinders the understanding of how temporal perception performance may vary across different types of tasks. Motivated by these two problems, we propose the TempCompass benchmark, which introduces a diversity of temporal aspects and task formats. To collect high-quality test data, we devise two novel strategies: (1) In video collection, we construct conflicting videos that share the same static content but differ in a specific temporal aspect, which prevents Video LLMs from leveraging single-frame bias or language priors. (2) To collect the task instructions, we propose a paradigm where humans first annotate meta-information for a video and then an LLM generates the instruction. We also design an LLM-based approach to automatically and accurately evaluate the responses from Video LLMs. Based on TempCompass, we comprehensively evaluate 9 state-of-the-art (SOTA) Video LLMs and 3 Image LLMs, and reveal the discerning fact that these models exhibit notably poor temporal perception ability.