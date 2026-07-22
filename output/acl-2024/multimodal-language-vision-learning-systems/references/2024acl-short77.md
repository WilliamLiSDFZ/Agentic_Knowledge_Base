---
title: "Don’t Buy it! Reassessing the Ad Understanding Abilities of Contrastive Multimodal Models"
source: "https://aclanthology.org/2024.acl-short.77/"
categories: ['multimodal-language-vision-learning-systems', 'moral-figurative-language-nlp-analysis']
tags: ['advertisement-understanding', 'contrastive-vision-language', 'multimodal-evaluation']
venue: "ACL 2024"
tldr: "A reassessment revealing that contrastive vision-language models perform poorly on ad-understanding tasks despite reported high accuracy."
---

# Don’t Buy it! Reassessing the Ad Understanding Abilities of Contrastive Multimodal Models

**Source**: [https://aclanthology.org/2024.acl-short.77/](https://aclanthology.org/2024.acl-short.77/)

**TLDR**: A reassessment revealing that contrastive vision-language models perform poorly on ad-understanding tasks despite reported high accuracy.

## Abstract

AbstractImage-based advertisements are complex multimodal stimuli that often contain unusual visual elements and figurative language. Previous research on automatic ad understanding has reported impressive zero-shot accuracy of contrastive vision-and-language models (VLMs) on an ad-explanation retrieval task. Here, we examine the original task setup and show that contrastive VLMs can solve it by exploiting grounding heuristics. To control for this confound, we introduce TRADE, a new evaluation test set with adversarial grounded explanations. While these explanations look implausible to humans, we show that they “fool” four different contrastive VLMs. Our findings highlight the need for an improved operationalisation of automatic ad understanding that truly evaluates VLMs’ multimodal reasoning abilities. We make our code and TRADE available at https://github.com/dmg-illc/trade.