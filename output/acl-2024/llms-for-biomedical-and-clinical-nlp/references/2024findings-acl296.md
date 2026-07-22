---
title: "MLeVLM: Improve Multi-level Progressive Capabilities based on Multimodal Large Language Model for Medical Visual Question Answering"
source: "https://aclanthology.org/2024.findings-acl.296/"
categories: ['llms-for-biomedical-and-clinical-nlp']
tags: ['medical-vqa', 'multimodal-llm', 'progressive-capabilities']
venue: "ACL 2024"
tldr: "MLeVLM introduces multi-level progressive capability learning for medical visual question answering using multimodal large language models."
---

# MLeVLM: Improve Multi-level Progressive Capabilities based on Multimodal Large Language Model for Medical Visual Question Answering

**Source**: [https://aclanthology.org/2024.findings-acl.296/](https://aclanthology.org/2024.findings-acl.296/)

**TLDR**: MLeVLM introduces multi-level progressive capability learning for medical visual question answering using multimodal large language models.

## Abstract

AbstractMedical visual question answering (MVQA) requires in-depth understanding of medical images and questions to provide reliable answers. We summarize multi-level progressive capabilities that models need to focus on in MVQA: recognition, details, diagnosis, knowledge, and reasoning. Existing MVQA models tend to ignore the above capabilities due to unspecific data and plain architecture. To address these issues, this paper proposes Multi-level Visual Language Model (MLeVLM) for MVQA. On the data side, we construct a high-quality multi-level instruction dataset MLe-VQA via GPT-4, which covers multi-level questions and answers as well as reasoning processes from visual clues to semantic cognition. On the architecture side, we propose a multi-level feature alignment module, including attention-based token selector and context merger, which can efficiently align features at different levels from visual to semantic. To better evaluate the model’s capabilities, we manually construct a multi-level MVQA evaluation benchmark named MLe-Bench. Extensive experiments demonstrate the effectiveness of our constructed multi-level instruction dataset and the multi-level feature alignment module. It also proves that MLeVLM outperforms existing medical multimodal large language models.