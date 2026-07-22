---
title: "Unsupervised Sign Language Translation and Generation"
source: "https://aclanthology.org/2024.findings-acl.835/"
pdf_url: ""
categories: ['speech-and-language-multimodal-generation-systems', 'language-technology-cultural-linguistic-diversity']
tags: ['unsupervised-translation', 'sign-language', 'multimodal']
venue: "ACL 2024"
tldr: "Introduces USLNet, an unsupervised network for sign language translation and generation trained on single-modality data without parallel sign language corpora."
---

# Unsupervised Sign Language Translation and Generation

**Source**: [https://aclanthology.org/2024.findings-acl.835/](https://aclanthology.org/2024.findings-acl.835/)

**TLDR**: Introduces USLNet, an unsupervised network for sign language translation and generation trained on single-modality data without parallel sign language corpora.

## Abstract

AbstractMotivated by the success of unsupervised neural machine translation (UNMT), we introduce an unsupervised sign language translation and generation network (USLNet), which learns from abundant single-modality (text and video) data without parallel sign language data. USLNet comprises two main components: single-modality reconstruction modules (text and video) that rebuild the input from its noisy version in the same modality and cross-modality back-translation modules (text-video-text and video-text-video) that reconstruct the input from its noisy version in the different modality using back-translation procedure. Unlike the single-modality back-translation procedure in text-based UNMT, USLNet faces the cross-modality discrepancy in feature representation, in which the length and the feature dimension mismatch between text and video sequences. We propose a sliding window method to address the issues of aligning variable-length text with video sequences. To our knowledge, USLNet is the first unsupervised sign language translation and generation model capable of generating both natural language text and sign language video in a unified manner. Experimental results on the BBC-Oxford Sign Language dataset and Open-Domain American Sign Language dataset reveal that USLNet achieves competitive results compared to supervised baseline models, indicating its effectiveness in sign language translation and generation.