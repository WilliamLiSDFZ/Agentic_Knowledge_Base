---
title: "STSPL-SSC: Semi-Supervised Few-Shot Short Text Clustering with Semantic text similarity Optimized Pseudo-Labels"
source: "https://aclanthology.org/2024.findings-acl.725/"
categories: ['text-clustering-with-limited-labels', 'llm-training-alignment-and-evaluation']
tags: ['short-text-clustering', 'semi-supervised-learning', 'pseudo-labels']
venue: "ACL 2024"
tldr: "Proposes STSPL-SSC, a semi-supervised few-shot short text clustering framework using semantic textual similarity to generate optimized pseudo-labels."
---

# STSPL-SSC: Semi-Supervised Few-Shot Short Text Clustering with Semantic text similarity Optimized Pseudo-Labels

**Source**: [https://aclanthology.org/2024.findings-acl.725/](https://aclanthology.org/2024.findings-acl.725/)

**TLDR**: Proposes STSPL-SSC, a semi-supervised few-shot short text clustering framework using semantic textual similarity to generate optimized pseudo-labels.

## Abstract

AbstractThis study introduces the Semantic Textual Similarity Pseudo-Label Semi-Supervised Clustering (STSPL-SSC) framework. The STSPL-SSC framework is designed to tackle the prevalent issue of scarce labeled data by combining a Semantic Textual Similarity Pseudo-Label Generation process with a Robust Contrastive Learning module. The process begins with employing k-means clustering on embeddings for initial pseudo-Label allocation. Then we use a Semantic Text Similarity-enhanced module to supervise the secondary clustering of pseudo-labels using labeled data to better align with the real clustering centers. Subsequently, an Adaptive Optimal Transport (AOT) approach fine-tunes the pseudo-labels. Finally, a Robust Contrastive Learning module is employed to foster the learning of classification and instance-level distinctions, aiding clusters to better separate. Experiments conducted on multiple real-world datasets demonstrate that with just one label per class, clustering performance can be significantly improved, outperforming state-of-the-art models with an increase of 1-6% in both accuracy and normalized mutual information, approaching the results of fully-labeled classification.