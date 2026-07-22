---
title: "Chinese Spoken Named Entity Recognition in Real-world Scenarios: Dataset and Approaches"
source: "https://aclanthology.org/2024.findings-acl.111/"
categories: ['nlp-for-asian-languages', 'natural-language-processing-information-extraction']
tags: ['spoken-NER', 'Chinese', 'real-world-dataset']
venue: "ACL 2024"
tldr: "A new real-world Chinese spoken NER dataset and approaches are introduced to improve entity extraction from natural speech for voice assistants."
---

# Chinese Spoken Named Entity Recognition in Real-world Scenarios: Dataset and Approaches

**Source**: [https://aclanthology.org/2024.findings-acl.111/](https://aclanthology.org/2024.findings-acl.111/)

**TLDR**: A new real-world Chinese spoken NER dataset and approaches are introduced to improve entity extraction from natural speech for voice assistants.

## Abstract

AbstractSpoken Named Entity Recognition (NER) aims to extract entities from speech. The extracted entities can help voice assistants better understand user’s questions and instructions. However, current Chinese Spoken NER datasets are laboratory-controlled data that are collected by reading existing texts in quiet environments, rather than natural spoken data, and the texts used for reading are also limited in topics. These limitations obstruct the development of Spoken NER in more natural and common real-world scenarios. To address this gap, we introduce a real-world Chinese Spoken NER dataset (RWCS-NER), encompassing open-domain daily conversations and task-oriented intelligent cockpit instructions. We compare several mainstream pipeline approaches on RWCS-NER. The results indicate that the current methods, affected by Automatic Speech Recognition (ASR) errors, do not perform satisfactorily in real settings. Aiming to enhance Spoken NER in real-world scenarios, we propose two approaches: self-training-asr and mapping then distilling (MDistilling). Experiments show that both approaches can achieve significant improvements, particularly MDistilling. Even compared with GPT4.0, MDistilling still reaches better results. We believe that our work will advance the field of Spoken NER in real-world settings.