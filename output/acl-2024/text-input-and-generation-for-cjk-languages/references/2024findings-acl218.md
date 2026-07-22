---
title: "Generative Input: Towards Next-Generation Input Methods Paradigm"
source: "https://aclanthology.org/2024.findings-acl.218/"
pdf_url: ""
categories: ['text-input-and-generation-for-cjk-languages']
tags: ['input-method', 'chinese-text-input', 'generative-models']
venue: "ACL 2024"
tldr: "This paper proposes a next-generation input method paradigm leveraging generative models for Chinese and CJK language text input."
---

# Generative Input: Towards Next-Generation Input Methods Paradigm

**Source**: [https://aclanthology.org/2024.findings-acl.218/](https://aclanthology.org/2024.findings-acl.218/)

**TLDR**: This paper proposes a next-generation input method paradigm leveraging generative models for Chinese and CJK language text input.

## Abstract

AbstractSince the release of ChatGPT, generative models have achieved tremendous success and become the de facto approach for various NLP tasks. However, its application in the field of input methods remains under-explored. Many neural network approaches have been applied to the construction of Chinese input method engines (IMEs). Previous research often assumed that the input pinyin was correct and focused on Pinyin-to-character (P2C) task, which significantly falls short of meeting users’ demands. Moreover, previous research could not leverage user feedback to optimize the model and provide personalized results. In this study, we propose a novel Generative Input paradigm named GeneInput. It uses prompts to handle all input scenarios and other intelligent auxiliary input functions, optimizing the model with user feedback. The results demonstrate that we have achieved state-of-the-art performance for the first time in the Full-mode Key-sequence to Characters task. GeneInput also includes RLHF-IME, a novel RLHF application framework for input method, that eliminates the need for manual ranking annotations and the performance surpasses GPT-4. Relevant resources have been open-sourced.