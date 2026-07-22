---
title: "Demonstrations Are All You Need: Advancing Offensive Content Paraphrasing using In-Context Learning"
source: "https://aclanthology.org/2024.findings-acl.749/"
categories: ['hate-speech-and-toxic-content-detection', 'llm-training-alignment-and-evaluation']
tags: ['offensive-content', 'paraphrasing', 'in-context-learning']
venue: "ACL 2024"
tldr: "In-context learning with demonstrations effectively paraphrases offensive content without requiring large labeled datasets."
---

# Demonstrations Are All You Need: Advancing Offensive Content Paraphrasing using In-Context Learning

**Source**: [https://aclanthology.org/2024.findings-acl.749/](https://aclanthology.org/2024.findings-acl.749/)

**TLDR**: In-context learning with demonstrations effectively paraphrases offensive content without requiring large labeled datasets.

## Abstract

AbstractParaphrasing of offensive content is a better alternative to content removal and helps improve civility in a communication environment. Supervised paraphrasers; however, rely heavily on large quantities of labelled data to help preserve meaning and intent. They also often retain a large portion of the offensiveness of the original content, which raises questions on their overall usability. In this paper we aim to assist practitioners in developing usable paraphrasers by exploring In-Context Learning (ICL) with large language models (LLMs), i.e., using a limited number of input-label demonstration pairs to guide the model in generating desired outputs for specific queries. Our study focuses on key factors such as - number and order of demonstrations, exclusion of prompt instruction, and reduction in measured toxicity. We perform principled evaluation on three datasets, including our proposed Context-Aware Polite Paraphrase (CAPP) dataset, comprising of dialogue-style rude utterances, polite paraphrases, and additional dialogue context. We evaluate our approach using four closed source and one open source LLM. Our results reveal that ICL is comparable to supervised methods in generation quality, while being qualitatively better by 25% on human evaluation and attaining lower toxicity by 76%. Also, ICL-based paraphrasers only show a slight reduction in performance even with just 10% training data.