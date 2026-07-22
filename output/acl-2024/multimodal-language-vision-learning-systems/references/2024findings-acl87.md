---
title: "Revisiting Multimodal Transformers for Tabular Data with Text Fields"
source: "https://aclanthology.org/2024.findings-acl.87/"
pdf_url: ""
categories: ['multimodal-language-vision-learning-systems', 'language-model-human-cognitive-linguistic-alignment']
tags: ['multimodal-transformers', 'tabular-data', 'text-fields']
venue: "ACL 2024"
tldr: "Revisits multimodal transformer architectures for tabular data containing text fields across applications like finance and medicine."
---

# Revisiting Multimodal Transformers for Tabular Data with Text Fields

**Source**: [https://aclanthology.org/2024.findings-acl.87/](https://aclanthology.org/2024.findings-acl.87/)

**TLDR**: Revisits multimodal transformer architectures for tabular data containing text fields across applications like finance and medicine.

## Abstract

AbstractTabular data with text fields can be leveraged in applications such as financial risk assessment or medical diagnosis prediction. When employing multimodal approaches to make predictions based on these modalities, it is crucial to make the most appropriate modeling choices in terms of numerical feature encoding or fusion strategy. In this paper, we focus on multimodal classification tasks based on tabular datasets with text fields. We build on multimodal Transformers to propose the Tabular-Text Transformer (TTT), a tabular/text dual-stream Transformer network. This architecture includes a distance-to-quantile embedding scheme for numerical features and an overall attention module which concurrently considers self-attention and cross-modal attention. Further, we leverage the two well-informed modality streams to estimate whether a prediction is uncertain or not. To explain uncertainty in terms of feature values, we use a sampling-based approximation of Shapley values in a bimodal context, with two options for the value function. To show the efficacy and relevance of this approach, we compare it to six baselines and measure its ability to quantify and explain uncertainty against various methods. Our code is available at https://github.com/thomas-bonnier/TabularTextTransformer.