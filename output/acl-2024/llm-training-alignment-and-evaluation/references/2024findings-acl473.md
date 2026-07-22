---
title: "Empowering cross-lingual abilities of instruction-tuned large language models by translation-following demonstrations"
source: "https://aclanthology.org/2024.findings-acl.473/"
pdf_url: ""
categories: ['language-technology-cultural-linguistic-diversity', 'llm-training-alignment-and-evaluation']
tags: ['cross-lingual', 'instruction-tuning', 'translation-demonstrations']
venue: "ACL 2024"
tldr: "Enhances cross-lingual abilities of instruction-tuned LLMs by incorporating translation-following demonstration examples."
---

# Empowering cross-lingual abilities of instruction-tuned large language models by translation-following demonstrations

**Source**: [https://aclanthology.org/2024.findings-acl.473/](https://aclanthology.org/2024.findings-acl.473/)

**TLDR**: Enhances cross-lingual abilities of instruction-tuned LLMs by incorporating translation-following demonstration examples.

## Abstract

AbstractThe language ability of Large Language Models (LLMs) is often unbalanced towards English because of the imbalance in the distribution of the pre-training data. This disparity is demanded in further fine-tuning and affecting the cross-lingual abilities of LLMs. In this paper, we propose to empower Instruction-tuned LLMs (It-LLMs) in languages other than English by building semantic alignment between them. Hence, we propose CrossAlpaca, an It-LLM with cross-lingual Instruction-following and Translation-following demonstrations to improve semantic alignment between languages. We validate our approach on the multilingual Question Answering (QA) benchmarks XQUAD and MLQA and adapted versions of MMLU and BBH.Our models, tested over six different languages, outperform the It-LLMs tuned on monolingual data. The final results show that instruction tuning on non-English data is not enough and that semantic alignment can be further improved by Translation-following demonstrations.