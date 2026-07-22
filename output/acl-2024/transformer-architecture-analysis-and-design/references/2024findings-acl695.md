---
title: "BranchNorm: Robustly Scaling Extremely Deep Transformers"
source: "https://aclanthology.org/2024.findings-acl.695/"
pdf_url: ""
categories: ['transformer-architecture-analysis-and-design', 'llm-training-alignment-and-evaluation']
tags: ['deep-transformers', 'training-stability', 'normalization']
venue: "ACL 2024"
tldr: "Introduces BranchNorm to stabilize training of extremely deep transformers beyond the limitations of DeepNorm."
---

# BranchNorm: Robustly Scaling Extremely Deep Transformers

**Source**: [https://aclanthology.org/2024.findings-acl.695/](https://aclanthology.org/2024.findings-acl.695/)

**TLDR**: Introduces BranchNorm to stabilize training of extremely deep transformers beyond the limitations of DeepNorm.

## Abstract

AbstractRecently, DeepNorm scales Transformers into extremely deep (i.e., 1000 layers) and reveals the promising potential of deep scaling. To stabilize the training of deep models, DeepNorm attempts to constrain the model update to a constant value. Although applying such a constraint can benefit the early stage of model training, it may lead to undertrained models during the whole training procedure. In this paper, we propose BranchNorm, which dynamically rescales the non-residual branch of Transformer in accordance with the training period. BranchNorm not only theoretically stabilizes the training with smooth gradient norms at the early stage, but also encourages better convergence in the subsequent training stage. Experimental results on multiple translation tasks demonstrate that BranchNorm achieves a better trade-off between training stability and converge performance.