---
title: "PartialFormer: Modeling Part Instead of Whole for Machine Translation"
source: "https://aclanthology.org/2024.findings-acl.434/"
categories: ['transformer-architecture-analysis-and-design', 'collaborative-llm-deployment-and-inference-optimization']
tags: ['transformer', 'machine-translation', 'feed-forward-network', 'efficient-architecture', 'lightweight']
venue: "ACL 2024"
tldr: "Proposes PartialFormer, a lightweight transformer variant that reduces computational overhead by modeling partial hidden dimensions in feed-forward networks."
---

# PartialFormer: Modeling Part Instead of Whole for Machine Translation

**Source**: [https://aclanthology.org/2024.findings-acl.434/](https://aclanthology.org/2024.findings-acl.434/)

**TLDR**: Proposes PartialFormer, a lightweight transformer variant that reduces computational overhead by modeling partial hidden dimensions in feed-forward networks.

## Abstract

AbstractThe design choices in Transformer feed-forward neural networks have resulted in significant computational and parameter overhead. In this work, we emphasize the importance of hidden dimensions in designing lightweight FFNs, a factor often overlooked in previous architectures. Guided by this principle, we introduce PartialFormer, a parameter-efficient Transformer architecture utilizing multiple smaller FFNs to reduce parameters and computation while maintaining essential hidden dimensions. These smaller FFNs are integrated into a multi-head attention mechanism for effective collaboration. We also propose a tailored head scaling strategy to enhance PartialFormer’s capabilities. Furthermore, we present a residual-like attention calculation to improve depth scaling within PartialFormer. Extensive experiments on 9 translation tasks and 1 abstractive summarization task validate the effectiveness of our PartialFormer approach on machine translation and summarization tasks. Our code would be available at: https://github.com/zhengkid/PartialFormer.