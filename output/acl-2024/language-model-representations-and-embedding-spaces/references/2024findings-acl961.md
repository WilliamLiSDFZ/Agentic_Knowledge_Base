---
title: "ContextBLIP: Doubly Contextual Alignment for Contrastive Image Retrieval from Linguistically Complex Descriptions"
source: "https://aclanthology.org/2024.findings-acl.961/"
categories: ['multimodal-language-vision-learning-systems', 'language-model-representations-and-embedding-spaces']
tags: ['image-retrieval', 'contrastive-learning', 'vision-language-alignment']
venue: "ACL 2024"
tldr: "ContextBLIP introduces doubly contextual alignment for contrastive image retrieval from linguistically complex and minimally contrastive descriptions."
---

# ContextBLIP: Doubly Contextual Alignment for Contrastive Image Retrieval from Linguistically Complex Descriptions

**Source**: [https://aclanthology.org/2024.findings-acl.961/](https://aclanthology.org/2024.findings-acl.961/)

**TLDR**: ContextBLIP introduces doubly contextual alignment for contrastive image retrieval from linguistically complex and minimally contrastive descriptions.

## Abstract

AbstractImage retrieval from contextual descriptions (IRCD) aims to identify an image within a set of minimally contrastive candidates based on linguistically complex text. Despite the success of VLMs, they still significantly lag behind human performance in IRCD. The main challenges lie in aligning key contextual cues in two modalities, where these subtle cues are concealed in tiny areas of multiple contrastive images and within the complex linguistics of textual descriptions. This motivates us to propose ContextBLIP, a simple yet effective method that relies on a doubly contextual alignment scheme for challenging IRCD. Specifically, 1) our model comprises a multi-scale adapter, a matching loss, and a text-guided masking loss. The adapter learns to capture fine-grained visual cues. The two losses enable iterative supervision for the adapter, gradually highlighting the focal patches of a single image to the key textual cues. We term such a way as intra-contextual alignment. 2) Then, ContextBLIP further employs an inter-context encoder to learn dependencies among candidates, facilitating alignment between the text to multiple images. We term this step as inter-contextual alignment. Consequently, the nuanced cues concealed in each modality can be effectively aligned. Experiments on two benchmarks show the superiority of our method. We observe that ContextBLIP can yield comparable results with GPT-4V, despite involving about 7,500 times fewer parameters.