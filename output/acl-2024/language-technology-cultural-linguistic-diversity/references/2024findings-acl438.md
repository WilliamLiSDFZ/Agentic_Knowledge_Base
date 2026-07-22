---
title: "The Impact of Demonstrations on Multilingual In-Context Learning: A Multidimensional Analysis"
source: "https://aclanthology.org/2024.findings-acl.438/"
categories: ['multilingual-text-classification-and-sentiment-analysis', 'language-technology-cultural-linguistic-diversity']
tags: ['in-context-learning', 'multilingual', 'demonstrations']
venue: "ACL 2024"
tldr: "A multidimensional analysis of how demonstration examples impact multilingual in-context learning across diverse languages."
---

# The Impact of Demonstrations on Multilingual In-Context Learning: A Multidimensional Analysis

**Source**: [https://aclanthology.org/2024.findings-acl.438/](https://aclanthology.org/2024.findings-acl.438/)

**TLDR**: A multidimensional analysis of how demonstration examples impact multilingual in-context learning across diverse languages.

## Abstract

AbstractIn-context learning is a popular inference strategy where large language models solve a task using only a few labeled demonstrations without needing any parameter updates. Although there have been extensive studies on English in-context learning, multilingual in-context learning remains under-explored, and we lack an in-depth understanding of the role of demonstrations in this context. To address this gap, we conduct a multidimensional analysis of multilingual in-context learning, experimenting with 5 models from different model families, 9 datasets covering classification and generation tasks, and 56 typologically diverse languages. Our results reveal that the effectiveness of demonstrations varies significantly across models, tasks, and languages. We also find that strong instruction-following models including Llama 2-Chat, GPT-3.5, and GPT-4 are largely insensitive to the quality of demonstrations. Instead, a carefully crafted template often eliminates the benefits of demonstrations for some tasks and languages altogether. These findings show that the importance of demonstrations might be overestimated. Our work highlights the need for granular evaluation across multiple axes towards a better understanding of in-context learning.