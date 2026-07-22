---
title: "Towards Better Utilization of Multi-Reference Training Data for Chinese Grammatical Error Correction"
source: "https://aclanthology.org/2024.findings-acl.180/"
categories: ['natural-language-processing-information-extraction', 'nlp-for-asian-languages']
tags: ['grammatical-error-correction', 'multi-reference', 'Chinese-NLP', 'training-data']
venue: "ACL 2024"
tldr: "This paper systematically studies how to better utilize multi-reference training data for Chinese grammatical error correction tasks."
---

# Towards Better Utilization of Multi-Reference Training Data for Chinese Grammatical Error Correction

**Source**: [https://aclanthology.org/2024.findings-acl.180/](https://aclanthology.org/2024.findings-acl.180/)

**TLDR**: This paper systematically studies how to better utilize multi-reference training data for Chinese grammatical error correction tasks.

## Abstract

AbstractFor the grammatical error correction (GEC) task, there usually exist multiple correction ways for an erroneous input sentence, leading to multiple references. Observing the high proportion of multi-reference instances in Chinese GEC training data, we target a systematic study on how to better utilize multi-reference training data. We propose two new approaches and a simple two-stage training strategy. We compare them against previously proposed approaches, on two Chinese training datasets, i.e., Lang-8 for second language learner texts and FCGEC-Train for native speaker texts, and three test datasets. The experiments and analyses demonstrate the effectiveness of our proposed approaches and reveal interesting insights. Our code is available at https://github.com/ymliucs/MrGEC.