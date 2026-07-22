---
title: "X-Instruction: Aligning Language Model in Low-resource Languages with Self-curated Cross-lingual Instructions"
source: "https://aclanthology.org/2024.findings-acl.30/"
pdf_url: ""
categories: ['language-technology-cultural-linguistic-diversity']
tags: ['low-resource-languages', 'cross-lingual', 'instruction-tuning']
venue: "ACL 2024"
tldr: "Introduces X-Instruction, a self-curation framework for aligning LLMs in low-resource languages via cross-lingual instructions."
---

# X-Instruction: Aligning Language Model in Low-resource Languages with Self-curated Cross-lingual Instructions

**Source**: [https://aclanthology.org/2024.findings-acl.30/](https://aclanthology.org/2024.findings-acl.30/)

**TLDR**: Introduces X-Instruction, a self-curation framework for aligning LLMs in low-resource languages via cross-lingual instructions.

## Abstract

AbstractLarge language models respond well in high-resource languages like English but struggle in low-resource languages. It may arise from the lack of high-quality instruction following data in these languages. Directly translating English samples into these languages can be a solution but unreliable, leading to responses with translation errors and lacking language-specific or cultural knowledge. To address this issue, we propose a novel method to construct cross-lingual instruction following samples with instruction in English and response in low-resource languages. Specifically, the language model first learns to generate appropriate English instructions according to the natural web texts in other languages as responses. The candidate cross-lingual instruction tuning samples are further refined and diversified. We have employed this method to build a large-scale cross-lingual instruction tuning dataset on 10 languages, namely X-Instruction. The instruction data built using our method incorporate more language-specific knowledge compared with the naive translation method. Experimental results have shown that the response quality of the model tuned on X-Instruction greatly exceeds the model distilled from a powerful teacher model, reaching or even surpassing the ones of ChatGPT. In addition, we find that models tuned on cross-lingual instruction following samples can follow the instruction in the output language without further tuning.