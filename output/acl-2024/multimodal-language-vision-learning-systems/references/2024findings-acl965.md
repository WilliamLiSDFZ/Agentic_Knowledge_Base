---
title: "CF-TCIR: A Compositor-Free Framework for Hierarchical Text-Conditioned Image Retrieval"
source: "https://aclanthology.org/2024.findings-acl.965/"
categories: ['multimodal-language-vision-learning-systems', 'natural-language-processing-information-extraction']
tags: ['image-retrieval', 'text-conditioned', 'multimodal', 'compositor-free', 'hierarchical']
venue: "ACL 2024"
tldr: "CF-TCIR is a compositor-free hierarchical framework for text-conditioned image retrieval combining visual and textual semantics."
---

# CF-TCIR: A Compositor-Free Framework for Hierarchical Text-Conditioned Image Retrieval

**Source**: [https://aclanthology.org/2024.findings-acl.965/](https://aclanthology.org/2024.findings-acl.965/)

**TLDR**: CF-TCIR is a compositor-free hierarchical framework for text-conditioned image retrieval combining visual and textual semantics.

## Abstract

AbstractIn text-conditioned image retrieval (TCIR), the combination of a reference image and modification text forms a query tuple, aiming to locate the most congruent target image within a dataset. The advantages of rich image semantic information and text flexibility are combined in this manner for more accurate retrieval. While traditional techniques often employ attention-driven compositors to craft a unified image-text representation, our paper introduces a compositor-free framework, CF-TCIR, which eschews the standard compositor. Compositor-based methods are designed to learn a joint representation of images and text, but they struggle to directly capture the correlations between attributes across the image and text modalities. Instead, we reformulate the retrieval process as a cross-modal interaction between a synthesized image feature and its corresponding text descriptor. This novel methodology offers advantages in terms of computational efficiency, scalability, and superior performance. To optimize the retrieval performance, we advocate a tiered retrieval mechanism, blending both coarse-grain and fine-grain paradigms. Moreover, to enrich the contextual relationship within the query tuple, we integrate a generative cross-modal alignment technique, ensuring synchronization of sequential attributes between image and text data.