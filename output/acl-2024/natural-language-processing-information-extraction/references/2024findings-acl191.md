---
title: "Refine, Align, and Aggregate: Multi-view Linguistic Features Enhancement for Aspect Sentiment Triplet Extraction"
source: "https://aclanthology.org/2024.findings-acl.191/"
categories: ['natural-language-processing-information-extraction']
tags: ['aspect-sentiment-triplet-extraction', 'multi-view', 'linguistic-features']
venue: "ACL 2024"
tldr: "Proposes a multi-view linguistic feature enhancement framework for more accurate aspect sentiment triplet extraction."
---

# Refine, Align, and Aggregate: Multi-view Linguistic Features Enhancement for Aspect Sentiment Triplet Extraction

**Source**: [https://aclanthology.org/2024.findings-acl.191/](https://aclanthology.org/2024.findings-acl.191/)

**TLDR**: Proposes a multi-view linguistic feature enhancement framework for more accurate aspect sentiment triplet extraction.

## Abstract

AbstractAspect Sentiment Triplet Extraction (ASTE) aims to extract the triplets of aspect terms, their associated sentiment and opinion terms. Previous works based on different modeling paradigms have achieved promising results. However, these methods struggle to comprehensively explore the various specific relations between sentiment elements in multi-view linguistic features, which is the prior indication effect for facilitating sentiment triplets extraction, requiring to align and aggregate them to capture the complementary higher-order interactions. In this paper, we propose Multi-view Linguistic Features Enhancement (MvLFE) to explore the aforementioned prior indication effect in the “Refine, Align, and Aggregate” learning process. Specifically, we first introduce the relational graph attention network to encode the word-pair relations represented by each linguistic feature and refine them to pay more attention to the aspect-opinion pairs. Next, we employ the multi-view contrastive learning to align them at a fine-grained level in the contextual semantic space to maintain semantic consistency. Finally, we utilize the multi-semantic cross attention to capture and aggregate the complementary higher-order interactions between diverse linguistic features to enhance the aspect-opinion relations. Experimental results on several benchmark datasets show the effectiveness and robustness of our model, which achieves state-of-the-art performance.