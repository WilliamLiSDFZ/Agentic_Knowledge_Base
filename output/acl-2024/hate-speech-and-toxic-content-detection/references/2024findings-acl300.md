---
title: "MemeMQA: Multimodal Question Answering for Memes via Rationale-Based Inferencing"
source: "https://aclanthology.org/2024.findings-acl.300/"
categories: ['hate-speech-and-toxic-content-detection']
tags: ['meme-analysis', 'multimodal-qa', 'harmful-content']
venue: "ACL 2024"
tldr: "MemeMQA introduces a multimodal question answering framework for memes using rationale-based inferencing to understand their communicative intent and potential harm."
---

# MemeMQA: Multimodal Question Answering for Memes via Rationale-Based Inferencing

**Source**: [https://aclanthology.org/2024.findings-acl.300/](https://aclanthology.org/2024.findings-acl.300/)

**TLDR**: MemeMQA introduces a multimodal question answering framework for memes using rationale-based inferencing to understand their communicative intent and potential harm.

## Abstract

AbstractMemes have evolved as a prevalent medium for diverse communication, ranging from humour to propaganda. With the rising popularity of image-focused content, there is a growing need to explore its potential harm from different aspects. Previous studies have analyzed memes in closed settings - detecting harm, applying semantic labels, and offering natural language explanations. To extend this research, we introduce MemeMQA, a multimodal question-answering framework aiming to solicit accurate responses to structured questions while providing coherent explanations. We curate MemeMQACorpus, a new dataset featuring 1,880 questions related to 1,122 memes with corresponding answer-explanation pairs. We further propose ARSENAL, a novel two-stage multimodal framework that leverages the reasoning capabilities of LLMs to address MemeMQA. We benchmark MemeMQA using competitive baselines and demonstrate its superiority - ~18% enhanced answer prediction accuracy and distinct text generation lead across various metrics measuring lexical and semantic alignment over the best baseline. We analyze ARSENAL’s robustness through diversification of question-set, confounder-based evaluation regarding MemeMQA’s generalizability, and modality-specific assessment, enhancing our understanding of meme interpretation in the multimodal communication landscape.