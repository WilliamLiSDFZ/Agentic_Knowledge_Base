---
title: "Assessing News Thumbnail Representativeness: Counterfactual text can enhance the cross-modal matching ability"
source: "https://aclanthology.org/2024.findings-acl.534/"
pdf_url: ""
categories: ['multimodal-language-vision-learning-systems', 'computational-misinformation-narrative-framing-detection']
tags: ['news-thumbnails', 'cross-modal-matching', 'counterfactual-text', 'representativeness']
venue: "ACL 2024"
tldr: "Proposes a method to assess whether news thumbnail images represent the actors in articles using counterfactual text to improve cross-modal matching."
---

# Assessing News Thumbnail Representativeness: Counterfactual text can enhance the cross-modal matching ability

**Source**: [https://aclanthology.org/2024.findings-acl.534/](https://aclanthology.org/2024.findings-acl.534/)

**TLDR**: Proposes a method to assess whether news thumbnail images represent the actors in articles using counterfactual text to improve cross-modal matching.

## Abstract

AbstractThis paper addresses the critical challenge of assessing the representativeness of news thumbnail images, which often serve as the first visual engagement for readers when an article is disseminated on social media. We focus on whether a news image represents the actors discussed in the news text. To serve the challenge, we introduce NewsTT, a manually annotated dataset of 1000 news thumbnail images and text pairs. We found that the pretrained vision and language models, such as BLIP-2, struggle with this task. Since news subjects frequently involve named entities or proper nouns, the pretrained models could have a limited capability to match news actors’ visual and textual appearances. We hypothesize that learning to contrast news text with its counterfactual, of which named entities are replaced, can enhance the cross-modal matching ability of vision and language models. We propose CFT-CLIP, a contrastive learning framework that updates vision and language bi-encoders according to the hypothesis. We found that our simple method can boost the performance for assessing news thumbnail representativeness, supporting our assumption. Code and data can be accessed at https://github.com/ssu-humane/news-images-acl24.