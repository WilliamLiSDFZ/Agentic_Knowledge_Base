---
title: "Exploiting Target Language Data for Neural Machine Translation Beyond Back Translation"
source: "https://aclanthology.org/2024.findings-acl.727/"
categories: ['language-technology-cultural-linguistic-diversity', 'continual-learning-for-nlp-tasks']
tags: ['neural-machine-translation', 'translation-memories', 'low-resource']
venue: "ACL 2024"
tldr: "Proposes a method to exploit target language data beyond back-translation for improving NMT in low-resource and domain-shift scenarios."
---

# Exploiting Target Language Data for Neural Machine Translation Beyond Back Translation

**Source**: [https://aclanthology.org/2024.findings-acl.727/](https://aclanthology.org/2024.findings-acl.727/)

**TLDR**: Proposes a method to exploit target language data beyond back-translation for improving NMT in low-resource and domain-shift scenarios.

## Abstract

AbstractNeural Machine Translation (NMT) encounters challenges when translating in new domains and low-resource languages. To address these issues, researchers have proposed methods to integrate additional knowledge into NMT, such as translation memories (TMs). However, finding TMs that closely match the input sentence remains challenging, particularly in specific domains. On the other hand, monolingual data is widely accessible in most languages, and back-translation is seen as a promising approach for utilizing target language data. Nevertheless, it still necessitates additional training. In this paper, we introduce Pseudo-kNN-MT, a variant of k-nearest neighbor machine translation (kNN-MT) that utilizes target language data by constructing a pseudo datastore. Furthermore, we investigate the utility of large language models (LLMs) for the kNN component. Experimental results demonstrate that our approach exhibits strong domain adaptation capability in both high-resource and low-resource machine translation. Notably, LLMs are found to be beneficial for robust NMT systems.