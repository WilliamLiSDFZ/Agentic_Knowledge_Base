---
title: "Cross-Modal Projection in Multimodal LLMs Doesn’t Really Project Visual Attributes to Textual Space"
source: "https://aclanthology.org/2024.acl-short.60/"
pdf_url: ""
categories: ['multimodal-language-vision-learning-systems', 'language-model-representations-and-embedding-spaces']
tags: ['multimodal-LLMs', 'visual-attribute-projection', 'cross-modal-alignment']
venue: "ACL 2024"
tldr: "Demonstrates that cross-modal projection in multimodal LLMs does not effectively transfer visual attributes into textual space."
---

# Cross-Modal Projection in Multimodal LLMs Doesn’t Really Project Visual Attributes to Textual Space

**Source**: [https://aclanthology.org/2024.acl-short.60/](https://aclanthology.org/2024.acl-short.60/)

**TLDR**: Demonstrates that cross-modal projection in multimodal LLMs does not effectively transfer visual attributes into textual space.

## Abstract

AbstractMultimodal large language models (MLLMs) like LLaVA and GPT-4(V) enable general-purpose conversations about images with the language modality. As off-the-shelf MLLMs may have limited capabilities on images from domains like dermatology and agriculture, they must be fine-tuned to unlock domain-specific applications. The prevalent architecture of current open-source MLLMs comprises two major modules: an image-language (cross-modal) projection network and a large language model. It is desirable to understand the roles of these two modules in modeling domain-specific visual attributes to inform the design of future models and streamline the interpretability efforts on the current models. To this end, via experiments on 4 datasets and under 2 fine-tuning settings, we find that as the MLLM is fine-tuned, it indeed gains domain-specific visual capabilities, but the updates do not lead to the projection extracting relevant domain-specific visual attributes. Our results indicate that the domain-specific visual attributes are modeled by the LLM, even when only the projection is fine-tuned. Through this study, we offer a potential reinterpretation of the role of cross-modal projections in MLLM architectures.