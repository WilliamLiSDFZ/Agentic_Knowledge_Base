---
title: "Length Generalization of Causal Transformers without Position Encoding"
source: "https://aclanthology.org/2024.findings-acl.834/"
categories: ['transformer-architecture-analysis-and-design', 'neural-language-models-formal-language-theory']
tags: ['length-generalization', 'transformers', 'position-encoding', 'NoPE']
venue: "ACL 2024"
tldr: "Studies length generalization in causal transformers without position encodings, offering theoretical and empirical insights into how NoPE models handle longer sequences."
---

# Length Generalization of Causal Transformers without Position Encoding

**Source**: [https://aclanthology.org/2024.findings-acl.834/](https://aclanthology.org/2024.findings-acl.834/)

**TLDR**: Studies length generalization in causal transformers without position encodings, offering theoretical and empirical insights into how NoPE models handle longer sequences.

## Abstract

AbstractGeneralizing to longer sentences is important for recent Transformer-based language models. Besides algorithms manipulating explicit position features, the success of Transformers without position encodings (NoPE) provides a new way to overcome the challenge. In this paper, we study the length generalization property of NoPE. We find that although NoPE can extend to longer sequences than the commonly used explicit position encodings, it still has a limited context length. We identify a connection between the failure of NoPE’s generalization and the distraction of attention distributions. We propose a parameter-efficient tuning for searching attention heads’ best temperature hyper-parameters, which substantially expands NoPE’s context size. Experiments on long sequence language modeling, the synthetic passkey retrieval task and real-world long context tasks show that NoPE can achieve competitive performances with state-of-the-art length generalization algorithms. The source code is publicly accessible