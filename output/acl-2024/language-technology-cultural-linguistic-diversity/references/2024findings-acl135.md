---
title: "Length-aware Byte Pair Encoding for Mitigating Over-segmentation in Korean Machine Translation"
source: "https://aclanthology.org/2024.findings-acl.135/"
categories: ['nlp-for-asian-languages', 'language-technology-cultural-linguistic-diversity']
tags: ['bpe', 'korean', 'machine-translation']
venue: "ACL 2024"
tldr: "Length-aware BPE is proposed to mitigate over-segmentation of morphologically rich Korean in machine translation."
---

# Length-aware Byte Pair Encoding for Mitigating Over-segmentation in Korean Machine Translation

**Source**: [https://aclanthology.org/2024.findings-acl.135/](https://aclanthology.org/2024.findings-acl.135/)

**TLDR**: Length-aware BPE is proposed to mitigate over-segmentation of morphologically rich Korean in machine translation.

## Abstract

AbstractByte Pair Encoding is an effective approach in machine translation across several languages. However, our analysis indicates that BPE is prone to over-segmentation in the morphologically rich language, Korean, which can erode word semantics and lead to semantic confusion during training. This semantic confusion, stemming from over-segmentation, ultimately contributes to a degradation of overall translation quality. To address this issue, we introduce Length-aware Subword Vocabulary Construction (LeVoC), a novel approach strategically incorporating longer words into the vocabulary. By utilizing an external monolingual Korean corpus, LeVoC extracts and integrates long words, effectively preserving morphological information and reducing semantic confusion. Our experiments demonstrate that LeVoC not only significantly outperforms BPE, but also can be applied to and surpass current state-of-the-art morpheme-aware subword tokenization methods. We provide evidence that the difficulty in translating sentences with long words in Korean is associated with morphological compositionality, and LeVoC’s ability to reduce semantic confusion during training leads to improved translation quality.