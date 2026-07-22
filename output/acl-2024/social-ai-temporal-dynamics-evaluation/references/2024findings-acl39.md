---
title: "Large Language Models can Share Images, Too!"
source: "https://aclanthology.org/2024.findings-acl.39/"
categories: ['multimodal-language-vision-learning-systems', 'social-ai-temporal-dynamics-evaluation']
tags: ['image-sharing', 'LLM-multimodal', 'zero-shot-evaluation']
venue: "ACL 2024"
tldr: "Explores and evaluates the image-sharing capability of LLMs in zero-shot settings with an enriched annotation dataset."
---

# Large Language Models can Share Images, Too!

**Source**: [https://aclanthology.org/2024.findings-acl.39/](https://aclanthology.org/2024.findings-acl.39/)

**TLDR**: Explores and evaluates the image-sharing capability of LLMs in zero-shot settings with an enriched annotation dataset.

## Abstract

AbstractThis paper explores the image-sharing capability of Large Language Models (LLMs), such as GPT-4 and LLaMA 2, in a zero-shot setting. To facilitate a comprehensive evaluation of LLMs, we introduce the photochatplus dataset, which includes enriched annotations (ie intent, triggering sentence, image description, and salient information). Furthermore, we present the gradient-free and extensible Decide, Describe, and Retrieve () framework. With extensive experiments, we unlock the image-sharing capability of equipped with LLMs in zero-shot prompting, with ChatGPT achieving the best performance.Our findings also reveal the emergent image-sharing ability in LLMs under zero-shot conditions, validating the effectiveness of . We use this framework to demonstrate its practicality and effectiveness in two real-world scenarios: (1) human-bot interaction and (2) dataset augmentation. To the best of our knowledge, this is the first study to assess the image-sharing ability of various LLMs in a zero-shot setting. We make our source code and dataset publicly available at https://github.com/passing2961/DribeR.