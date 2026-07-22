---
title: "Towards Artwork Explanation in Large-scale Vision Language Models"
source: "https://aclanthology.org/2024.acl-short.65/"
pdf_url: ""
categories: ['multimodal-language-vision-learning-systems', 'nlp-benchmark-design-and-interpretability']
tags: ['vision-language-models', 'artwork-explanation', 'visual-understanding', 'multimodal', 'evaluation']
venue: "ACL 2024"
tldr: "Evaluates the extent to which large vision-language models understand the complex knowledge required to explain artwork."
---

# Towards Artwork Explanation in Large-scale Vision Language Models

**Source**: [https://aclanthology.org/2024.acl-short.65/](https://aclanthology.org/2024.acl-short.65/)

**TLDR**: Evaluates the extent to which large vision-language models understand the complex knowledge required to explain artwork.

## Abstract

AbstractLarge-scale Vision-Language Models (LVLMs) output text from images and instructions, demonstrating advanced capabilities in text generation and comprehension. However, it has not been clarified to what extent LVLMs understand the knowledge necessary for explaining images, the complex relationships between various pieces of knowledge, and how they integrate these understandings into their explanations. To address this issue, we propose a new task: the artwork explanation generation task, along with its evaluation dataset and metric for quantitatively assessing the understanding and utilization of knowledge about artworks. This task is apt for image description based on the premise that LVLMs are expected to have pre-existing knowledge of artworks, which are often subjects of wide recognition and documented information.It consists of two parts: generating explanations from both images and titles of artworks, and generating explanations using only images, thus evaluating the LVLMs’ language-based and vision-based knowledge.Alongside, we release a training dataset for LVLMs to learn explanations that incorporate knowledge about artworks.Our findings indicate that LVLMs not only struggle with integrating language and visual information but also exhibit a more pronounced limitation in acquiring knowledge from images alone. The datasets ExpArt=Explain Artworks are available at https://huggingface.co/datasets/naist-nlp/ExpArt