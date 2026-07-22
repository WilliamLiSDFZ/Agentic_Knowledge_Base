---
title: "Question Translation Training for Better Multilingual Reasoning"
source: "https://aclanthology.org/2024.findings-acl.498/"
categories: ['language-technology-cultural-linguistic-diversity', 'multilingual-text-classification-and-sentiment-analysis']
tags: ['multilingual-reasoning', 'question-translation', 'instruction-tuning']
venue: "ACL 2024"
tldr: "Training LLMs with translated questions rather than translated answers improves multilingual reasoning performance across diverse languages."
---

# Question Translation Training for Better Multilingual Reasoning

**Source**: [https://aclanthology.org/2024.findings-acl.498/](https://aclanthology.org/2024.findings-acl.498/)

**TLDR**: Training LLMs with translated questions rather than translated answers improves multilingual reasoning performance across diverse languages.

## Abstract

AbstractLarge language models show compelling performance on reasoning tasks but they tend to perform much worse in languages other than English. This is unsurprising given that their training data largely consists of English text and instructions. A typical solution is to translate instruction data into all languages of interest, and then train on the resulting multilingual data, which is called translate-training. This approach not only incurs high cost, but also results in poorly translated data due to the non-standard formatting of mathematical chain-of-thought. In this paper, we explore the benefits of question alignment, where we train the model to translate reasoning questions into English by finetuning on X-English parallel question data. In this way we perform targeted, in-domain language alignment which makes best use of English instruction data to unlock the LLMs’ multilingual reasoning abilities. Experimental results on LLaMA2-13B show that question alignment leads to consistent improvements over the translate-training approach: an average improvement of 11.3% and 16.1% accuracy across ten languages on the MGSM and MSVAMP multilingual reasoning benchmarks.