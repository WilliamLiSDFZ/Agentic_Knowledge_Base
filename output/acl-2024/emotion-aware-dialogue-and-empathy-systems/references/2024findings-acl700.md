---
title: "Visualizing Dialogues: Enhancing Image Selection through Dialogue Understanding with Large Language Models"
source: "https://aclanthology.org/2024.findings-acl.700/"
categories: ['multimodal-language-vision-learning-systems', 'emotion-aware-dialogue-and-empathy-systems']
tags: ['multimodal-dialogue', 'image-selection', 'dialogue-understanding']
venue: "ACL 2024"
tldr: "This paper enhances image selection in multimodal dialogue systems by leveraging LLMs for deeper dialogue understanding."
---

# Visualizing Dialogues: Enhancing Image Selection through Dialogue Understanding with Large Language Models

**Source**: [https://aclanthology.org/2024.findings-acl.700/](https://aclanthology.org/2024.findings-acl.700/)

**TLDR**: This paper enhances image selection in multimodal dialogue systems by leveraging LLMs for deeper dialogue understanding.

## Abstract

AbstractFor dialogue systems, the utilization of multimodal dialogue responses, as opposed to relying solely on text-only responses, offers the capability to describe different concepts through various modalities. This enhances the effectiveness of communication and elevates the overall conversational experience. However, current methods for dialogue-to-image retrieval are constrained by the capabilities of the pre-trained vision language models (VLMs). They struggle to accurately extract key information from conversations and are unable to handle long-turn conversations. In this paper, we leverage the reasoning capabilities of large language models (LLMs) to predict the potential features that may be present in the images to be shared, based on the dialogue context. This approach allows us to obtain succinct and precise descriptors, thereby improving the performance of text-image retrieval. Experimental results shows that our method outperforms previous approaches significantly in terms of Recall@k.