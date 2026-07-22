---
title: "wav2vec-S: Adapting Pre-trained Speech Models for Streaming"
source: "https://aclanthology.org/2024.findings-acl.681/"
categories: ['speech-and-language-multimodal-generation-systems', 'state-memory-replay-sequence-modeling']
tags: ['streaming-speech', 'wav2vec', 'adaptation']
venue: "ACL 2024"
tldr: "Adapts pre-trained wav2vec 2.0 speech models for streaming scenarios by addressing the mismatch between full-utterance training and online inference."
---

# wav2vec-S: Adapting Pre-trained Speech Models for Streaming

**Source**: [https://aclanthology.org/2024.findings-acl.681/](https://aclanthology.org/2024.findings-acl.681/)

**TLDR**: Adapts pre-trained wav2vec 2.0 speech models for streaming scenarios by addressing the mismatch between full-utterance training and online inference.

## Abstract

AbstractPre-trained speech models, such as wav2vec 2.0, have significantly advanced speech-related tasks, including speech recognition and translation. However, their applicability in streaming scenarios is limited because these models are trained on complete utterances, leading to a mismatch with incremental streaming inputs. This paper identifies three critical design aspects within the architecture of wav2vec 2.0 and proposes a novel model, wav2vec-S, which incorporates simple modifications to ensure consistent speech representations during both training and inference phases for streaming speech inputs. Furthermore, we demonstrate that wav2vec-S models can be efficiently adapted from pre-trained wav2vec 2.0 models through continued pre-training and effectively finetuned to meet various latency requirements in downstream applications. Experiments on speech recognition and translation tasks show that wav2vec-S outperforms strong baseline models and achieves a superior balance between quality and latency.