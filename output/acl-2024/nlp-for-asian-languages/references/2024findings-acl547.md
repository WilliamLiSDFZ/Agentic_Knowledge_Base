---
title: "LCS: A Language Converter Strategy for Zero-Shot Neural Machine Translation"
source: "https://aclanthology.org/2024.findings-acl.547/"
categories: ['language-technology-cultural-linguistic-diversity', 'nlp-for-asian-languages']
tags: ['zero-shot-translation', 'language-tag', 'multilingual-NMT']
venue: "ACL 2024"
tldr: "A language converter strategy improves zero-shot neural machine translation by better indicating target language directions."
---

# LCS: A Language Converter Strategy for Zero-Shot Neural Machine Translation

**Source**: [https://aclanthology.org/2024.findings-acl.547/](https://aclanthology.org/2024.findings-acl.547/)

**TLDR**: A language converter strategy improves zero-shot neural machine translation by better indicating target language directions.

## Abstract

AbstractMultilingual neural machine translation models generally distinguish translation directions by the language tag (LT) in front of the source or target sentences. However, current LT strategies cannot indicate the desired target language as expected on zero-shot translation, i.e., the off-target issue. Our analysis reveals that the indication of the target language is sensitive to the placement of the target LT. For example, when placing the target LT on the decoder side, the indication would rapidly degrade along with decoding steps, while placing the target LT on the encoder side would lead to copying or paraphrasing the source input. To address the above issues, we propose a simple yet effective strategy named Language Converter Strategy (LCS). By introducing the target language embedding into the top encoder layers, LCS mitigates confusion in the encoder and ensures stable language indication for the decoder. Experimental results on MultiUN, TED, and OPUS-100 datasets demonstrate that LCS could significantly mitigate the off-target issue, with language accuracy up to 95.28%, 96.21%, and 85.35% meanwhile outperforming the vanilla LT strategy by 3.07, 3,3, and 7.93 BLEU scores on zero-shot translation, respectively.