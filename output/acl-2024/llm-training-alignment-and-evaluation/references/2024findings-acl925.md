---
title: "Hire a Linguist!: Learning Endangered Languages in LLMs with In-Context Linguistic Descriptions"
source: "https://aclanthology.org/2024.findings-acl.925/"
categories: ['language-technology-cultural-linguistic-diversity', 'llm-training-alignment-and-evaluation']
tags: ['endangered-languages', 'in-context-learning', 'linguistic-descriptions']
venue: "ACL 2024"
tldr: "Shows that providing in-context linguistic descriptions enables LLMs to process and translate endangered low-resource languages with minimal data."
---

# Hire a Linguist!: Learning Endangered Languages in LLMs with In-Context Linguistic Descriptions

**Source**: [https://aclanthology.org/2024.findings-acl.925/](https://aclanthology.org/2024.findings-acl.925/)

**TLDR**: Shows that providing in-context linguistic descriptions enables LLMs to process and translate endangered low-resource languages with minimal data.

## Abstract

AbstractHow can large language models (LLMs) process and translate endangered languages? Many languages lack a large corpus to train a decent LLM; therefore existing LLMs rarely perform well in unseen, endangered languages. On the contrary, we observe that 2000 endangered languages, though without a large corpus, have a grammar book or a dictionary. We propose LingoLLM, a training-free approach to enable an LLM to process unseen languages that hardly occur in its pre-training. Our key insight is to demonstrate linguistic knowledge of an unseen language in an LLM’s prompt, including a dictionary, a grammar book, and morphologically analyzed input text. We implement LingoLLM on top of two models, GPT-4 and Mixtral, and evaluate their performance on 5 tasks across 8 endangered or low-resource languages. Our results show that LingoLLM elevates translation capability from GPT-4’s 0 to 10.5 BLEU for 10 language directions. Our findings demonstrate the tremendous value of linguistic knowledge in the age of LLMs for endangered languages. Our data, code, and model generations will be released to the public. Our data, code, and model generations can be found at https://github.com/LLiLab/llm4endangeredlang.