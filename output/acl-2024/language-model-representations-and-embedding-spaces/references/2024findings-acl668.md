---
title: "Space Decomposition for Sentence Embedding"
source: "https://aclanthology.org/2024.findings-acl.668/"
categories: ['language-model-representations-and-embedding-spaces', 'continuous-discrete-representation-tradeoffs']
tags: ['sentence-embedding', 'space-decomposition', 'semantic-similarity']
venue: "ACL 2024"
tldr: "Sentence embedding space is decomposed to better model the discrete-continuous nature of semantic textual similarity scores."
---

# Space Decomposition for Sentence Embedding

**Source**: [https://aclanthology.org/2024.findings-acl.668/](https://aclanthology.org/2024.findings-acl.668/)

**TLDR**: Sentence embedding space is decomposed to better model the discrete-continuous nature of semantic textual similarity scores.

## Abstract

AbstractDetermining sentence pair similarity is crucial for various NLP tasks. A common technique to address this is typically evaluated on a continuous semantic textual similarity scale from 0 to 5. However, based on a linguistic observation in STS annotation guidelines, we found that the score in the range [4,5] indicates an upper-range sample, while the rest are lower-range samples. This necessitates a new approach to treating the upper-range and lower-range classes separately. In this paper, we introduce a novel embedding space decomposition method called MixSP utilizing a Mixture of Specialized Projectors, designed to distinguish and rank upper-range and lower-range samples accurately. The experimental results demonstrate that MixSP decreased the overlap representation between upper-range and lower-range classes significantly while outperforming competitors on STS and zero-shot benchmarks.