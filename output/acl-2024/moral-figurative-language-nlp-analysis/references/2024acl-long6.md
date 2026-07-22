---
title: "Exploring Chain-of-Thought for Multi-modal Metaphor Detection"
source: "https://aclanthology.org/2024.acl-long.6/"
pdf_url: ""
categories: ['moral-figurative-language-nlp-analysis', 'multimodal-language-vision-learning-systems']
tags: ['metaphor-detection', 'chain-of-thought', 'multimodal']
venue: "ACL 2024"
tldr: "Applies chain-of-thought reasoning to multimodal metaphor detection in advertising and internet memes combining visual and textual cues."
---

# Exploring Chain-of-Thought for Multi-modal Metaphor Detection

**Source**: [https://aclanthology.org/2024.acl-long.6/](https://aclanthology.org/2024.acl-long.6/)

**TLDR**: Applies chain-of-thought reasoning to multimodal metaphor detection in advertising and internet memes combining visual and textual cues.

## Abstract

AbstractMetaphors are commonly found in advertising and internet memes. However, the free form of internet memes often leads to a lack of high-quality textual data. Metaphor detection demands a deep interpretation of both textual and visual elements, requiring extensive common-sense knowledge, which poses a challenge to language models. To address these challenges, we propose a compact framework called C4MMD, which utilizes a Chain-of-Thought(CoT) method for Multi-modal Metaphor Detection. Specifically, our approach designs a three-step process inspired by CoT that extracts and integrates knowledge from Multi-modal Large Language Models(MLLMs) into smaller ones. We also developed a modality fusion architecture to transform knowledge from large models into metaphor features, supplemented by auxiliary tasks to improve model performance. Experimental results on the MET-MEME dataset demonstrate that our method not only effectively enhances the metaphor detection capabilities of small models but also outperforms existing models. To our knowledge, this is the first systematic study leveraging MLLMs in metaphor detection tasks. The code for our method is publicly available at https://github.com/xyz189411yt/C4MMD.