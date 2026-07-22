---
title: "Overcoming Catastrophic Forgetting by Exemplar Selection in Task-oriented Dialogue System"
source: "https://aclanthology.org/2024.findings-acl.5/"
pdf_url: ""
categories: ['continual-learning-for-nlp-tasks']
tags: ['continual-learning', 'task-oriented-dialogue', 'catastrophic-forgetting']
venue: "ACL 2024"
tldr: "Addresses catastrophic forgetting in task-oriented dialogue systems via exemplar selection for continual learning."
---

# Overcoming Catastrophic Forgetting by Exemplar Selection in Task-oriented Dialogue System

**Source**: [https://aclanthology.org/2024.findings-acl.5/](https://aclanthology.org/2024.findings-acl.5/)

**TLDR**: Addresses catastrophic forgetting in task-oriented dialogue systems via exemplar selection for continual learning.

## Abstract

AbstractIntelligent task-oriented dialogue systems (ToDs) are expected to continuously acquire new knowledge, also known as Continual Learning (CL), which is crucial to fit ever-changing user needs. However, catastrophic forgetting dramatically degrades the model performance in face of a long streamed curriculum. In this paper, we aim to overcome the forgetting problem in ToDs and propose a method (HESIT) with hyper-gradient-based exemplar strategy, which samples influential exemplars for periodic retraining. Instead of unilaterally observing data or models, HESIT adopts a profound exemplar selection strategy that considers the general performance of the trained model when selecting exemplars for each task domain. Specifically, HESIT analyzes the training data influence by tracing their hyper-gradient in the optimization process. Furthermore, HESIT avoids estimating Hessian to make it compatible for ToDs with a large pre-trained model. Experimental results show that HESIT effectively alleviates catastrophic forgetting by exemplar selection, and achieves state-of-the-art performance on the largest CL benchmark of ToDs in terms of all metrics.