---
title: "S3-DST: Structured Open-Domain Dialogue Segmentation and State Tracking in the Era of LLMs"
source: "https://aclanthology.org/2024.findings-acl.891/"
pdf_url: ""
categories: ['coreference-resolution-and-dialogue-understanding', 'llm-agents-reasoning-and-planning']
tags: ['dialogue-state-tracking', 'open-domain-dialogue', 'segmentation']
venue: "ACL 2024"
tldr: "Presents S3-DST, a structured approach to open-domain dialogue segmentation and state tracking leveraging LLMs for flexible multi-domain conversations."
---

# S3-DST: Structured Open-Domain Dialogue Segmentation and State Tracking in the Era of LLMs

**Source**: [https://aclanthology.org/2024.findings-acl.891/](https://aclanthology.org/2024.findings-acl.891/)

**TLDR**: Presents S3-DST, a structured approach to open-domain dialogue segmentation and state tracking leveraging LLMs for flexible multi-domain conversations.

## Abstract

AbstractTraditional Dialogue State Tracking (DST) has focused on tracking preferences and intents in conversations centered around specific tasks (e.g. booking services). These conventional systems assume a relatively restricted conversation flow in which each turn gradually offers new information. However, advancements in Large Language Models (LLMs) have ushered in more versatile open-domain chat systems in which extended dialogue sessions encompassing numerous tasks and topics are common—in turn requiring new conversational tracking tools in order to successfully orchestrate such systems. Addressing these challenges, we introduce a novel approach combining dialogue segmentation and state tracking within open-domain dialogues, tailored for zero-shot applications appropriate to a true open-domain dialogue system. Our proposed method S3-DST employs a unique structured prompting technique and *Pre-Analytical Recollection*, a novel grounding mechanism we designed for improving long context tracking. Tested on proprietary anonymized open-domain dialogue datasets as well as publicly available DST and segmentation datasets, S3-DST consistently outperforms the state-of-the-art, showcasing its effectiveness and adaptability state tracking in the next wave of LLM-based chat systems. We also release S3-DST annotations with GPT-4 on a curated subset of LMSYS-Chat-1M to be used as a testbed to fuel research in this direction.