---
title: "MELOV: Multimodal Entity Linking with Optimized Visual Features in Latent Space"
source: "https://aclanthology.org/2024.findings-acl.46/"
pdf_url: ""
categories: ['multimodal-language-vision-learning-systems', 'natural-language-processing-information-extraction']
tags: ['multimodal-entity-linking', 'visual-features', 'latent-space']
venue: "ACL 2024"
tldr: "Proposes MELOV, a multimodal entity linking method optimizing visual features in latent space for improved cross-modal mention-entity alignment."
---

# MELOV: Multimodal Entity Linking with Optimized Visual Features in Latent Space

**Source**: [https://aclanthology.org/2024.findings-acl.46/](https://aclanthology.org/2024.findings-acl.46/)

**TLDR**: Proposes MELOV, a multimodal entity linking method optimizing visual features in latent space for improved cross-modal mention-entity alignment.

## Abstract

AbstractMultimodal entity linking (MEL), which aligns ambiguous mentions within multimodal contexts to referent entities from multimodal knowledge bases, is essential for many natural language processing applications. Previous MEL methods mainly focus on exploring complex multimodal interaction mechanisms to better capture coherence evidence between mentions and entities by mining complementary information. However, in real-world social media scenarios, vision modality often exhibits low quality, low value, or low relevance to the mention. Integrating such information directly will backfire, leading to a weakened consistency between mentions and their corresponding entities. In this paper, we propose a novel latent space vision feature optimization framework MELOV, which combines inter-modality and intra-modality optimizations to address these challenges. For the inter-modality optimization, we exploit the variational autoencoder to mine shared information and generate text-based visual features. For the intra-modality optimization, we consider the relationships between mentions and build graph convolutional network to aggregate the visual features of semantic similar neighbors. Extensive experiments on three benchmark datasets demonstrate the superiority of our proposed framework.