---
title: "Multimodal Prompt Learning with Missing Modalities for Sentiment Analysis and Emotion Recognition"
source: "https://aclanthology.org/2024.acl-long.94/"
pdf_url: ""
categories: ['multimodal-language-vision-learning-systems']
tags: ['multimodal-learning', 'missing-modality', 'sentiment-analysis']
venue: "ACL 2024"
tldr: "A multimodal prompt learning approach is proposed to handle missing modalities in sentiment analysis and emotion recognition tasks."
---

# Multimodal Prompt Learning with Missing Modalities for Sentiment Analysis and Emotion Recognition

**Source**: [https://aclanthology.org/2024.acl-long.94/](https://aclanthology.org/2024.acl-long.94/)

**TLDR**: A multimodal prompt learning approach is proposed to handle missing modalities in sentiment analysis and emotion recognition tasks.

## Abstract

AbstractThe development of multimodal models has significantly advanced multimodal sentiment analysis and emotion recognition. However, in real-world applications, the presence of various missing modality cases often leads to a degradation in the model’s performance. In this work, we propose a novel multimodal Transformer framework using prompt learning to address the issue of missing modalities. Our method introduces three types of prompts: generative prompts, missing-signal prompts, and missing-type prompts. These prompts enable the generation of missing modality features and facilitate the learning of intra- and inter-modality information. Through prompt learning, we achieve a substantial reduction in the number of trainable parameters. Our proposed method outperforms other methods significantly across all evaluation metrics. Extensive experiments and ablation studies are conducted to demonstrate the effectiveness and robustness of our method, showcasing its ability to effectively handle missing modalities. Codes are available at https://github.com/zrguo/MPLMM.