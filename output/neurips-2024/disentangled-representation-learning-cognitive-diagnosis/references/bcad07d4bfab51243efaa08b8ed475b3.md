---
title: "In-Context Symmetries: Self-Supervised Learning through Contextual World Models"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/bcad07d4bfab51243efaa08b8ed475b3-Abstract-Conference.html"
categories: ['deep-learning-optimization-and-generalization-theory', 'disentangled-representation-learning-cognitive-diagnosis']
tags: ['self-supervised-learning', 'contextual-world-models', 'equivariance']
venue: "NeurIPS 2024"
tldr: "Proposes learning invariant/equivariant representations through contextual world models that adapt symmetries in-context for improved downstream flexibility."
---

# In-Context Symmetries: Self-Supervised Learning through Contextual World Models

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/bcad07d4bfab51243efaa08b8ed475b3-Abstract-Conference.html](https://papers.nips.cc/paper_files/paper/2024/hash/bcad07d4bfab51243efaa08b8ed475b3-Abstract-Conference.html)

**TLDR**: Proposes learning invariant/equivariant representations through contextual world models that adapt symmetries in-context for improved downstream flexibility.

## Abstract

At the core of self-supervised learning for vision is the idea of learning invariant or equivariant representations with respect to a set of data transformations. This approach, however, introduces strong inductive biases, which can render the representations fragile in downstream tasks that do not conform to these symmetries. In this work, drawing insights from world models, we propose to instead learn a general representation that can adapt to be invariant or equivariant to different transformations by paying attention to context --- a memory module that tracks task-specific states, actions and future states. Here, the action is the transformation, while the current and future states respectively represent the input's representation before and after the transformation.  Our proposed algorithm, Contextual Self Supervised Learning (ContextSSL), learns equivariance to all transformations (as opposed to invariance). In this way, the model can learn to encode all relevant features as general representations while having the versatility to tail down to task-wise symmetries when given a few examples as the context. Empirically, we demonstrate significant performance gains over existing methods on equivariance-related tasks, supported by both qualitative and quantitative evaluations.