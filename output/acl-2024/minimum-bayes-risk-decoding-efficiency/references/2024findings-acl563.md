---
title: "Domain-Aware k-Nearest-Neighbor Knowledge Distillation for Machine Translation"
source: "https://aclanthology.org/2024.findings-acl.563/"
pdf_url: ""
categories: ['minimum-bayes-risk-decoding-efficiency']
tags: ['knn-machine-translation', 'knowledge-distillation', 'domain-adaptation']
venue: "ACL 2024"
tldr: "Proposes domain-aware kNN knowledge distillation to transfer neighborhood knowledge into model training for improved machine translation efficiency."
---

# Domain-Aware k-Nearest-Neighbor Knowledge Distillation for Machine Translation

**Source**: [https://aclanthology.org/2024.findings-acl.563/](https://aclanthology.org/2024.findings-acl.563/)

**TLDR**: Proposes domain-aware kNN knowledge distillation to transfer neighborhood knowledge into model training for improved machine translation efficiency.

## Abstract

AbstractkNN-MT has utilized neighborhood knowledge for auxiliary decoding, significantly improving translation performance. Subsequently, kNN-KD transitions the use of neighborhood knowledge from the decoding phase to the training phase, to address the temporal and spatial inefficiencies inherent in kNN-MT. However, kNN-KD transfers all the kNN knowledge arbitrarily, which has the potential to restrict the learning of student models. In this paper, we propose a novel domain-aware kNN-KD method, which filters out domain-relevant neighborhood knowledge for learning in the distillation process. Notably, this entire process exclusively utilizes the neighborhood knowledge of the original model, eliminating the need for establishing any additional datastores. Experiments on four domain translation tasks demonstrate that our method achieves state-of-the-art performance, realizing an average gain of 1.55 COMET and 1.42 BLEU scores, by further enhancing the translation of rare words. Source code can be accessed at https://github.com/wangzx1219/Dk-KD.