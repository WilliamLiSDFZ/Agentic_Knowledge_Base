---
title: "k-SemStamp: A Clustering-Based Semantic Watermark for Detection of Machine-Generated Text"
source: "https://aclanthology.org/2024.findings-acl.98/"
categories: ['llm-security-robustness-and-detection', 'language-model-representations-and-embedding-spaces']
tags: ['watermarking', 'machine-generated-text-detection', 'semantic-clustering']
venue: "ACL 2024"
tldr: "k-SemStamp applies clustering-based semantic watermarking to improve robustness of machine-generated text detection against paraphrase attacks."
---

# k-SemStamp: A Clustering-Based Semantic Watermark for Detection of Machine-Generated Text

**Source**: [https://aclanthology.org/2024.findings-acl.98/](https://aclanthology.org/2024.findings-acl.98/)

**TLDR**: k-SemStamp applies clustering-based semantic watermarking to improve robustness of machine-generated text detection against paraphrase attacks.

## Abstract

AbstractRecent watermarked generation algorithms inject detectable signatures during language generation to facilitate post-hoc detection. While token-level watermarks are vulnerable to paraphrase attacks, SemStamp (Hou et al., 2023) applies watermark on the semantic representation of sentences and demonstrates promising robustness. SemStamp employs locality-sensitive hashing (LSH) to partition the semantic space with arbitrary hyperplanes, which results in a suboptimal tradeoff between robustness and speed. We propose k-SemStamp, a simple yet effective enhancement of SemStamp, utilizing k-means clustering as an alternative of LSH to partition the embedding space with awareness of inherent semantic structure. Experimental results indicate that k-SemStamp saliently improves its robustness and sampling efficiency while preserving the generation quality, advancing a more effective tool for machine-generated text detection.