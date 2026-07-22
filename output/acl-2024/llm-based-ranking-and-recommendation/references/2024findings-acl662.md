---
title: "Distillation Enhanced Generative Retrieval"
source: "https://aclanthology.org/2024.findings-acl.662/"
pdf_url: ""
categories: ['llm-based-ranking-and-recommendation', 'language-model-representations-and-embedding-spaces']
tags: ['generative-retrieval', 'knowledge-distillation', 'passage-retrieval']
venue: "ACL 2024"
tldr: "This work enhances generative retrieval by applying knowledge distillation to improve identifier generation and retrieval accuracy."
---

# Distillation Enhanced Generative Retrieval

**Source**: [https://aclanthology.org/2024.findings-acl.662/](https://aclanthology.org/2024.findings-acl.662/)

**TLDR**: This work enhances generative retrieval by applying knowledge distillation to improve identifier generation and retrieval accuracy.

## Abstract

AbstractGenerative retrieval is a promising new paradigm in text retrieval that generates identifier strings of relevant passages as the retrieval target. This paradigm leverages powerful generative language models, distinct from traditional sparse or dense retrieval methods. In this work, we identify a viable direction to further enhance generative retrieval via distillation and propose a feasible framework, named DGR. DGR utilizes sophisticated ranking models, such as the cross-encoder, in a teacher role to supply a passage rank list, which captures the varying relevance degrees of passages instead of binary hard labels; subsequently, DGR employs a specially designed distilled RankNet loss to optimize the generative retrieval model, considering the passage rank order provided by the teacher model as labels. This framework only requires an additional distillation step to enhance current generative retrieval systems and does not add any burden to the inference stage. We conduct experiments on four public datasets, and the results indicate that DGR achieves state-of-the-art performance among the generative retrieval methods. Additionally, DGR demonstrates exceptional robustness and generalizability with various teacher models and distillation losses.