---
title: "Converting Transformers to Polynomial Form for Secure Inference Over Homomorphic Encryption"
source: "https://proceedings.mlr.press/v235/zimerman24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/zimerman24a/zimerman24a.pdf"
categories: ['privacy-preserving-federated-and-distributed-learning', 'transformer-architecture-efficiency-and-scaling']
tags: ['homomorphic-encryption', 'privacy-preserving', 'transformers', 'polynomial-approximation', 'secure-inference']
venue: "ICML 2024"
tldr: "This paper converts transformer architectures into polynomial form to enable efficient privacy-preserving inference over homomorphic encryption."
---

# Converting Transformers to Polynomial Form for Secure Inference Over Homomorphic Encryption

**Source**: [https://proceedings.mlr.press/v235/zimerman24a.html](https://proceedings.mlr.press/v235/zimerman24a.html)

**TLDR**: This paper converts transformer architectures into polynomial form to enable efficient privacy-preserving inference over homomorphic encryption.

## Abstract

Designing privacy-preserving DL solutions is a major challenge within the AI community. Homomorphic Encryption (HE) has emerged as one of the most promising approaches in this realm, enabling the decoupling of knowledge between a model owner and a data owner. Despite extensive research and application of this technology, primarily in CNNs, applying HE on transformer models has been challenging because of the difficulties in converting these models into a polynomial form. We break new ground by introducing the first polynomial transformer, providing the first demonstration of secure inference over HE with full transformers. This includes a transformer architecture tailored for HE, alongside a novel method for converting operators to their polynomial equivalent. This innovation enables us to perform secure inference on LMs and ViTs with several datasts and tasks. Our techniques yield results comparable to traditional models, bridging the performance gap with transformers of similar scale and underscoring the viability of HE for state-of-the-art applications. Finally, we assess the stability of our models and conduct a series of ablations to quantify the contribution of each model component. Our code is publicly available.