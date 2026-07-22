---
title: "Fine-Tuning Pre-Trained Language Models with Gaze Supervision"
source: "https://aclanthology.org/2024.acl-short.21/"
pdf_url: ""
categories: ['language-model-human-cognitive-linguistic-alignment']
tags: ['gaze-supervision', 'cognitive-nlp', 'fine-tuning']
venue: "ACL 2024"
tldr: "Human gaze data is used as cognitive supervision signal during fine-tuning of pre-trained language models to improve NLP task performance."
---

# Fine-Tuning Pre-Trained Language Models with Gaze Supervision

**Source**: [https://aclanthology.org/2024.acl-short.21/](https://aclanthology.org/2024.acl-short.21/)

**TLDR**: Human gaze data is used as cognitive supervision signal during fine-tuning of pre-trained language models to improve NLP task performance.

## Abstract

AbstractHuman gaze data provide cognitive information that reflect human language comprehension and has been effectively integrated into a variety of natural language processing (NLP) tasks, demonstrating improved performance over corresponding plain text-based models. In this work, we propose to integrate a gaze module into pre-trained language models (LMs) at the fine-tuning stage to improve their capabilities to learn representations that are grounded in human language processing. This is done by extending the conventional purely text-based fine-tuning objective with an auxiliary loss to exploit cognitive signals. The gaze module is only included during training, retaining compatibility with existing pre-trained LM-based pipelines. We evaluate the proposed approach using two distinct pre-trained LMs on the GLUE benchmark and observe that the proposed model improves performance compared to both standard fine-tuning and traditional text augmentation baselines.