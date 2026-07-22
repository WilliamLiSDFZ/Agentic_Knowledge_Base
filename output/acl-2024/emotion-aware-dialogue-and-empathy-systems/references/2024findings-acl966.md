---
title: "DMIN: A Discourse-specific Multi-granularity Integration Network for Conversational Aspect-based Sentiment Quadruple Analysis"
source: "https://aclanthology.org/2024.findings-acl.966/"
pdf_url: ""
categories: ['emotion-aware-dialogue-and-empathy-systems', 'coreference-resolution-and-dialogue-understanding']
tags: ['aspect-based-sentiment', 'dialogue', 'discourse-structure']
venue: "ACL 2024"
tldr: "A discourse-aware multi-granularity network for extracting sentiment quadruples from conversational data."
---

# DMIN: A Discourse-specific Multi-granularity Integration Network for Conversational Aspect-based Sentiment Quadruple Analysis

**Source**: [https://aclanthology.org/2024.findings-acl.966/](https://aclanthology.org/2024.findings-acl.966/)

**TLDR**: A discourse-aware multi-granularity network for extracting sentiment quadruples from conversational data.

## Abstract

AbstractConversational Aspect-based Sentiment Quadruple Analysis (DiaASQ) aims to extract fine-grained sentiment quadruples from dialogues. Previous research has primarily concentrated on enhancing token-level interactions, still lacking in sufficient modeling of the discourse structure information in dialogue. Firstly, it does not incorporate interactions among different utterances in the encoding stage, resulting in a limited token-level context understanding for subsequent modules. Secondly, it ignores the critical fact that discourse information is naturally organized at the utterance level and learning it solely at the token level is incomplete. In this work, we strengthen the token-level encoder by utilizing a discourse structure called “thread” and graph convolutional networks to enhance the token interaction among different utterances. Moreover, we propose an utterance-level encoder to learn the structured speaker and reply information, providing a macro understanding of dialogue discourse. Furthermore, we introduce a novel Multi-granularities Integrator to integrate token-level and utterance-level representations, resulting in a comprehensive and cohesive dialogue contextual understanding. Experiments on two datasets demonstrate that our model achieves state-of-the-art performance. Our codes are publicly available at https://github.com/SIGSDSscau/DMIN.