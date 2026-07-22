---
title: "Efficient Domain Adaptation for Non-Autoregressive Machine Translation"
source: "https://aclanthology.org/2024.findings-acl.810/"
pdf_url: ""
categories: ['language-technology-cultural-linguistic-diversity', 'transformer-architecture-analysis-and-design']
tags: ['domain-adaptation', 'non-autoregressive-MT', 'neural-machine-translation', 'efficiency']
venue: "ACL 2024"
tldr: "Presents an efficient domain adaptation approach for non-autoregressive machine translation leveraging nearest-neighbor methods without full retraining."
---

# Efficient Domain Adaptation for Non-Autoregressive Machine Translation

**Source**: [https://aclanthology.org/2024.findings-acl.810/](https://aclanthology.org/2024.findings-acl.810/)

**TLDR**: Presents an efficient domain adaptation approach for non-autoregressive machine translation leveraging nearest-neighbor methods without full retraining.

## Abstract

AbstractDomain adaptation remains a challenge in the realm of Neural Machine Translation (NMT), even in the era of large language models (LLMs). Existing non-parametric approaches like nearest neighbor machine translation have made small Autoregressive Translation (AT) models achieve efficient domain generalization and adaptation without updating parameters, but leaving the Non-Autoregressive Translation (NAT) counterparts under-explored. To fill this blank, we introduce Bi-kNN, an innovative and efficient domain adaptation approach for NAT models that tailors a k-nearest-neighbor algorithm for NAT. Specifically, we introduce an effective datastore construction and correlated updating strategies to conform the parallel nature of NAT. Additionally, we train a meta-network that seamlessly integrates the NN distribution with the NMT distribution robustly during the iterative decoding process of NAT. Our experimental results across four benchmark datasets demonstrate that our Bi-kNN not only achieves significant improvements over the Base-NAT model (7.8 BLEU on average) but also exhibits enhanced efficiency.