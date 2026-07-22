---
title: "Boosting Textural NER with Synthetic Image and Instructive Alignment"
source: "https://aclanthology.org/2024.findings-acl.74/"
pdf_url: ""
categories: ['natural-language-processing-information-extraction']
tags: ['named-entity-recognition', 'synthetic-images', 'multimodal-alignment']
venue: "ACL 2024"
tldr: "Enhances textual NER by generating synthetic images and aligning them instructively to resolve entity disambiguation challenges."
---

# Boosting Textural NER with Synthetic Image and Instructive Alignment

**Source**: [https://aclanthology.org/2024.findings-acl.74/](https://aclanthology.org/2024.findings-acl.74/)

**TLDR**: Enhances textual NER by generating synthetic images and aligning them instructively to resolve entity disambiguation challenges.

## Abstract

AbstractNamed entity recognition (NER) is a pivotal task reliant on textual data, often impeding the disambiguation of entities due to the absence of context. To tackle this challenge, conventional methods often incorporate images crawled from the internet as auxiliary information. However, the images often lack sufficient entities or would introduce noise. Even with high-quality images, it is still challenging to efficiently use images as auxiliaries (i.e., fine-grained alignment with texts). We introduce a novel method named InstructNER to address these issues. Leveraging the rich real-world knowledge and image synthesis capabilities of a large pre-trained stable diffusion (SD) model, InstructNER transforms the text-only NER into a multimodal NER (MNER) task. A selection process automatically identifies the best synthetic image by comparing fine-grained similarities with internet-crawled images through a visual bag-of-words strategy. Note, during the image synthesis, a cross-attention matrix between synthetic images and raw text emerges, which inspires a soft attention guidance alignment (AGA) mechanism. AGA optimizes the MNER task and concurrently facilitates instructive alignment in MNER. Empirical experiments on prominent MNER datasets show that our method surpasses all text-only baselines, improving F1-score by 1.4% to 2.3%. Remarkably, even when compared to fully multimodal baselines, our approach maintains competitive. Furthermore, we open-source a comprehensive synthetic image dataset and the code to supplement existing raw dataset. The code and datasets are available in https://github.com/Heyest/InstructNER.