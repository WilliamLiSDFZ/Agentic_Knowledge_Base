---
title: "Learning Multimodal Contrast with Cross-modal Memory and Reinforced Contrast Recognition"
source: "https://aclanthology.org/2024.findings-acl.391/"
pdf_url: ""
categories: ['multimodal-language-vision-learning-systems']
tags: ['multimodal-contrast', 'cross-modal-memory', 'irony-humor']
venue: "ACL 2024"
tldr: "This paper proposes a multimodal contrastive learning approach with cross-modal memory to handle semantically misaligned visual-textual content like irony."
---

# Learning Multimodal Contrast with Cross-modal Memory and Reinforced Contrast Recognition

**Source**: [https://aclanthology.org/2024.findings-acl.391/](https://aclanthology.org/2024.findings-acl.391/)

**TLDR**: This paper proposes a multimodal contrastive learning approach with cross-modal memory to handle semantically misaligned visual-textual content like irony.

## Abstract

AbstractIn many practical scenarios, contents from different modalities are not semantically aligned; for instance, visual and textual information may conflict with each other, resulting in non-compositional expression effects such as irony or humor. Effective modeling and smooth integration of multimodal information are crucial for achieving good understanding of the contrast across modalities. Being focusing on image-text matching, most current studies face challenges in identifying such contrast, leading to limitations in exploring the extended semantics when images and texts do not match. In this paper, we propose an LLM-based approach for learning multimodal contrast following the encoding-decoding paradigm, enhanced by a memory module with reinforced contrast recognition, and use a series of tasks that have the nature of multimodal contrast to verify our approach. The memory module learns the integration between visual and textual features with trainable memory vectors and the reinforced contrast recognition uses self-rejection sampling to optimize the memory to further enhance learning multimodal contrast. The resulted information, accompanied with visual and text features, is finally fed into the LLM to predict corresponding labels. We experiment our approach on four English and Chinese benchmark datasets, where it outperforms strong baselines and state-of-the-art studies.