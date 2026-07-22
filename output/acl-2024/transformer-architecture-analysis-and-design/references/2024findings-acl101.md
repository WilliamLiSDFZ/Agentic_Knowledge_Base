---
title: "CeeBERT: Cross-Domain Inference in Early Exit BERT"
source: "https://aclanthology.org/2024.findings-acl.101/"
categories: ['transformer-architecture-analysis-and-design', 'llm-training-alignment-and-evaluation']
tags: ['early-exit', 'bert', 'cross-domain-inference']
venue: "ACL 2024"
tldr: "Introduces CeeBERT, a cross-domain early exit method for BERT that reduces inference latency while maintaining performance."
---

# CeeBERT: Cross-Domain Inference in Early Exit BERT

**Source**: [https://aclanthology.org/2024.findings-acl.101/](https://aclanthology.org/2024.findings-acl.101/)

**TLDR**: Introduces CeeBERT, a cross-domain early exit method for BERT that reduces inference latency while maintaining performance.

## Abstract

AbstractPre-trained Language Models (PLMs), like BERT, with self-supervision objectives exhibit remarkable performance and generalization across various tasks. However, they suffer in inference latency due to their large size. To address this issue, side branches are attached at intermediate layers, enabling early inference of samples without requiring them to pass through all layers. However, the challenge is to decide which layer to infer and exit each sample so that the accuracy and latency are balanced. Moreover, the distribution of the samples to be inferred may differ from that used for training necessitating cross-domain adaptation. We propose an online learning algorithm named Cross-Domain Inference in Early Exit BERT (CeeBERT) that dynamically determines early exits of samples based on the level of confidence at each exit point. CeeBERT learns optimal thresholds from domain-specific confidence observed at intermediate layers on the fly, eliminating the need for labeled data. Experimental results on five distinct datasets with BERT and ALBERT models demonstrate CeeBERT’s ability to improve latency by reducing unnecessary computations with minimal drop in performance. By adapting to the threshold values, CeeBERT can speed up the BERT/ALBERT models by 2× - 3.1× with minimal drop in accuracy. The anonymized source code is available at https://github.com/Div290/CeeBERT.