---
title: "ToxVidLM: A Multimodal Framework for Toxicity Detection in Code-Mixed Videos"
source: "https://aclanthology.org/2024.findings-acl.663/"
pdf_url: ""
categories: ['hate-speech-and-toxic-content-detection', 'multimodal-language-vision-learning-systems']
tags: ['toxicity-detection', 'multimodal', 'code-mixed-language', 'video-understanding', 'low-resource']
venue: "ACL 2024"
tldr: "A multimodal framework for detecting toxic content in code-mixed videos combining visual and linguistic signals."
---

# ToxVidLM: A Multimodal Framework for Toxicity Detection in Code-Mixed Videos

**Source**: [https://aclanthology.org/2024.findings-acl.663/](https://aclanthology.org/2024.findings-acl.663/)

**TLDR**: A multimodal framework for detecting toxic content in code-mixed videos combining visual and linguistic signals.

## Abstract

AbstractIn an era of rapidly evolving internet technology, the surge in multimodal content, including videos, has expanded the horizons of online communication. However, the detection of toxic content in this diverse landscape, particularly in low-resource code-mixed languages, remains a critical challenge. While substantial research has addressed toxic content detection in textual data, the realm of video content, especially in non-English languages, has been relatively underexplored. This paper addresses this research gap by introducing a benchmark dataset, the first of its kind, consisting of 931 videos with 4021 code-mixed Hindi-English utterances collected from YouTube. Each utterance within this dataset has been meticulously annotated for toxicity, severity, and sentiment labels. We have developed an advanced Multimodal Multitask framework built for Toxicity detection in Video Content by leveraging Language Models (LMs), crafted for the primary objective along with the additional tasks of conducting sentiment and severity analysis. ToxVidLM incorporates three key modules – the Encoder module, Cross-Modal Synchronization module, and Multitask module – crafting a generic multimodal LM customized for intricate video classification tasks. Our experiments reveal that incorporating multiple modalities from the videos substantially enhances the performance of toxic content detection by achieving an Accuracy and Weighted F1 score of 94.29% and 94.35%, respectively.