---
title: "Sign Language Translation with Sentence Embedding Supervision"
source: "https://aclanthology.org/2024.acl-short.40/"
categories: ['multimodal-language-vision-learning-systems', 'speech-and-language-multimodal-generation-systems']
tags: ['sign-language', 'translation', 'sentence-embeddings']
venue: "ACL 2024"
tldr: "Proposes using sentence embedding supervision to improve sign language translation without relying on scarce gloss annotations."
---

# Sign Language Translation with Sentence Embedding Supervision

**Source**: [https://aclanthology.org/2024.acl-short.40/](https://aclanthology.org/2024.acl-short.40/)

**TLDR**: Proposes using sentence embedding supervision to improve sign language translation without relying on scarce gloss annotations.

## Abstract

AbstractState-of-the-art sign language translation (SLT) systems facilitate the learning process through gloss annotations, either in an end2end manner or by involving an intermediate step. Unfortunately, gloss labelled sign language data is usually not available at scale and, when available, gloss annotations widely differ from dataset to dataset. We present a novel approach using sentence embeddings of the target sentences at training time that take the role of glosses. The new kind of supervision does not need any manual annotation but it is learned on raw textual data. As our approach easily facilitates multilinguality, we evaluate it on datasets covering German (PHOENIX-2014T) and American (How2Sign) sign languages and experiment with mono- and multilingual sentence embeddings and translation systems. Our approach significantly outperforms other gloss-free approaches, setting the new state-of-the-art for data sets where glosses are not available and when no additional SLT datasets are used for pretraining, diminishing the gap between gloss-free and gloss-dependent systems.