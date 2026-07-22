---
title: "A Non-autoregressive Generation Framework for End-to-End Simultaneous Speech-to-Any Translation"
source: "https://aclanthology.org/2024.acl-long.85/"
pdf_url: ""
categories: ['speech-and-language-multimodal-generation-systems', 'multimodal-language-vision-learning-systems']
tags: ['simultaneous-translation', 'non-autoregressive', 'speech-to-speech']
venue: "ACL 2024"
tldr: "Proposes a non-autoregressive end-to-end framework for simultaneous speech-to-any translation, eliminating cascaded pipeline errors."
---

# A Non-autoregressive Generation Framework for End-to-End Simultaneous Speech-to-Any Translation

**Source**: [https://aclanthology.org/2024.acl-long.85/](https://aclanthology.org/2024.acl-long.85/)

**TLDR**: Proposes a non-autoregressive end-to-end framework for simultaneous speech-to-any translation, eliminating cascaded pipeline errors.

## Abstract

AbstractSimultaneous translation models play a crucial role in facilitating communication. However, existing research primarily focuses on text-to-text or speech-to-text models, necessitating additional cascade components to achieve speech-to-speech translation. These pipeline methods suffer from error propagation and accumulate delays in each cascade component, resulting in reduced synchronization between the speaker and listener. To overcome these challenges, we propose a novel non-autoregressive generation framework for simultaneous speech translation (NAST-S2x), which integrates speech-to-text and speech-to-speech tasks into a unified end-to-end framework.We develop a non-autoregressive decoder capable of concurrently generating multiple text or acoustic unit tokens upon receiving fixed-length speech chunks. The decoder can generate blank or repeated tokens and employ CTC decoding to dynamically adjust its latency. Experimental results show that NAST-S2x outperforms state-of-the-art models in both speech-to-text and speech-to-speech tasks. It achieves high-quality simultaneous interpretation within a delay of less than 3 seconds and provides a 28× decoding speedup in offline generation.