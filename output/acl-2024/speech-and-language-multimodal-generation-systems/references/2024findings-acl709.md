---
title: "On the Evaluation of Speech Foundation Models for Spoken Language Understanding"
source: "https://aclanthology.org/2024.findings-acl.709/"
categories: ['speech-and-language-multimodal-generation-systems', 'llm-training-alignment-and-evaluation']
tags: ['spoken-language-understanding', 'speech-foundation-models', 'benchmark-evaluation']
venue: "ACL 2024"
tldr: "Evaluates speech foundation models on the SLUE benchmark suite covering classification and sequence generation tasks for spoken language understanding."
---

# On the Evaluation of Speech Foundation Models for Spoken Language Understanding

**Source**: [https://aclanthology.org/2024.findings-acl.709/](https://aclanthology.org/2024.findings-acl.709/)

**TLDR**: Evaluates speech foundation models on the SLUE benchmark suite covering classification and sequence generation tasks for spoken language understanding.

## Abstract

AbstractThe Spoken Language Understanding Evaluation (SLUE) suite of benchmark tasks was recently introduced to address the need for openresources and benchmarking of complex spoken language understanding (SLU) tasks, including both classification and sequence generation tasks, on natural speech. The benchmark has demonstrated preliminary success in using pre-trained speech foundation models (SFM) for these SLU tasks. However, the community still lacks a fine-grained understanding of the comparative utility of different SFMs. Inspired by this, we ask: which SFMs offer the most benefits for these complex SLU tasks, and what is the most effective approach for incorporating these SFMs? To answer this, we perform an extensive evaluation of multiple supervised and self-supervised SFMs using several evaluation protocols: (i) frozen SFMs with a lightweight prediction head, (ii) frozen SFMs with a complex prediction head, and (iii) fine-tuned SFMs with a lightweight prediction head. Although the supervised SFMs are pre-trained on much more speech recognition data (with labels), they do not always outperform self-supervised SFMs; the latter tend to perform at least as well as, and sometimes better than, supervised SFMs, especially on the sequence generation tasks in SLUE. While there is no universally optimal way of incorporating SFMs, the complex prediction head gives the best performance for most tasks, although it increases the inference time. We also introduce an open-source toolkit and performance leaderboard, SLUE-PERB, for these tasks and modeling strategies.