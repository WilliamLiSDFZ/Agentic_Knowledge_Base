---
title: "X-ACE: Explainable and Multi-factor Audio Captioning Evaluation"
source: "https://aclanthology.org/2024.findings-acl.729/"
pdf_url: ""
categories: ['speech-and-language-multimodal-generation-systems', 'emotion-aware-dialogue-and-empathy-systems']
tags: ['audio-captioning', 'evaluation-metrics', 'explainability', 'multi-factor']
venue: "ACL 2024"
tldr: "Presents X-ACE, an explainable multi-factor evaluation metric for automated audio captioning that provides nuanced dimension-specific quality scores."
---

# X-ACE: Explainable and Multi-factor Audio Captioning Evaluation

**Source**: [https://aclanthology.org/2024.findings-acl.729/](https://aclanthology.org/2024.findings-acl.729/)

**TLDR**: Presents X-ACE, an explainable multi-factor evaluation metric for automated audio captioning that provides nuanced dimension-specific quality scores.

## Abstract

AbstractAutomated audio captioning (AAC) aims to generate descriptions based on audio input, attracting exploration of emerging audio language models (ALMs). However, current evaluation metrics only provide a single score to assess the overall quality of captions without characterizing the nuanced difference by systematically going through an evaluation checklist. To this end, we propose the explainable and multi-factor audio captioning evaluation (X-ACE) paradigm. X-ACE identifies four main factors that constitute the majority of audio features, specifically sound event, source, attribute and relation. To assess a given caption from an ALM, it is firstly transformed into an audio graph, where each node denotes an entity in the caption and corresponds to a factor. On the one hand, graph matching is conducted from part to whole for a holistic assessment. On the other hand, the nodes contained within each factor are aggregated to measure the factor-level performance. The pros and cons of an ALM can be explicitly and clearly demonstrated through X-ACE, pointing out the direction for further improvements. Experiments show that X-ACE exhibits better correlation with human perception and can detect mismatches sensitively.