---
title: "Mixture-of-Supernets: Improving Weight-Sharing Supernet Training with Architecture-Routed Mixture-of-Experts"
source: "https://aclanthology.org/2024.findings-acl.621/"
pdf_url: ""
categories: ['transformer-architecture-analysis-and-design', 'llm-training-alignment-and-evaluation']
tags: ['neural-architecture-search', 'mixture-of-experts', 'weight-sharing', 'supernet', 'NLP']
venue: "ACL 2024"
tldr: "Mixture-of-Supernets improves weight-sharing supernet training by routing subnetworks through mixture-of-experts architecture."
---

# Mixture-of-Supernets: Improving Weight-Sharing Supernet Training with Architecture-Routed Mixture-of-Experts

**Source**: [https://aclanthology.org/2024.findings-acl.621/](https://aclanthology.org/2024.findings-acl.621/)

**TLDR**: Mixture-of-Supernets improves weight-sharing supernet training by routing subnetworks through mixture-of-experts architecture.

## Abstract

AbstractWeight-sharing supernets are crucial for performance estimation in cutting-edge neural architecture search (NAS) frameworks. Despite their ability to generate diverse subnetworks without retraining, the quality of these subnetworks is not guaranteed due to weight sharing. In NLP tasks like machine translation and pre-trained language modeling, there is a significant performance gap between supernet and training from scratch for the same model architecture, necessitating retraining post optimal architecture identification.This study introduces a solution called mixture-of-supernets, a generalized supernet formulation leveraging mixture-of-experts (MoE) to enhance supernet model expressiveness with minimal training overhead. Unlike conventional supernets, this method employs an architecture-based routing mechanism, enabling indirect sharing of model weights among subnetworks. This customization of weights for specific architectures, learned through gradient descent, minimizes retraining time, significantly enhancing training efficiency in NLP. The proposed method attains state-of-the-art (SoTA) performance in NAS for fast machine translation models, exhibiting a superior latency-BLEU tradeoff compared to HAT, the SoTA NAS framework for machine translation. Furthermore, it excels in NAS for building memory-efficient task-agnostic BERT models, surpassing NAS-BERT and AutoDistil across various model sizes. The code can be found at: https://github.com/UBC-NLP/MoS.