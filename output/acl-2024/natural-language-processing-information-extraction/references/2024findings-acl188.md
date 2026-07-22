---
title: "GENDEX: Generative Data Augmentation Strategy Leveraging External Data for Abstractive Dialogue Summarization"
source: "https://aclanthology.org/2024.findings-acl.188/"
pdf_url: ""
categories: ['natural-language-processing-information-extraction']
tags: ['data-augmentation', 'dialogue-summarization', 'generative-models']
venue: "ACL 2024"
tldr: "Presents a generative data augmentation strategy using external data to improve abstractive dialogue summarization under low-resource conditions."
---

# GENDEX: Generative Data Augmentation Strategy Leveraging External Data for Abstractive Dialogue Summarization

**Source**: [https://aclanthology.org/2024.findings-acl.188/](https://aclanthology.org/2024.findings-acl.188/)

**TLDR**: Presents a generative data augmentation strategy using external data to improve abstractive dialogue summarization under low-resource conditions.

## Abstract

AbstractWith the proliferation of digital communication, dialogue summarization has become increasingly important. However, it still faces a shortage of data. To address this issue, we developed **Gen**erative **D**ata Augmentation Strategy Leveraging **Ex**ternal Data for Abstractive Dialogue Summarization (**GENDEX**), which is based on the hypothetical foundation that texts containing people and their interpersonal interactions can potentially serve as summaries of corresponding dialogues. We filter short texts containing people and resolve coreferences for better contextual analysis. We then identify the semantic roles of words within the texts and filter them based on the patterns observed in the dialogue summarization datasets. Using these texts, we generate synthetic dialogues through a controlled generation method. To better leverage the augmented data, we utilize noise-tolerant training to fine-tune the summarization model. The experimental results demonstrate the effectiveness of our proposed method, showing its robust performance, generalizability, and scalability. Moreover, performance improvements by *GENDEX* were observed regardless of complexity of dialogues. The code is available at https://github.com/DMCB-GIST/GENDEX.