---
title: "Efficient k-Nearest-Neighbor Machine Translation with Dynamic Retrieval"
source: "https://aclanthology.org/2024.findings-acl.475/"
categories: ['collaborative-llm-deployment-and-inference-optimization', 'natural-language-processing-information-extraction']
tags: ['kNN-machine-translation', 'dynamic-retrieval', 'domain-adaptation']
venue: "ACL 2024"
tldr: "Proposes efficient dynamic retrieval strategies for kNN-MT to reduce datastore lookup costs while maintaining domain adaptation performance."
---

# Efficient k-Nearest-Neighbor Machine Translation with Dynamic Retrieval

**Source**: [https://aclanthology.org/2024.findings-acl.475/](https://aclanthology.org/2024.findings-acl.475/)

**TLDR**: Proposes efficient dynamic retrieval strategies for kNN-MT to reduce datastore lookup costs while maintaining domain adaptation performance.

## Abstract

AbstractTo achieve non-parametric NMT domain adaptation, k-Nearest-Neighbor Machine Translation (kNN-MT) constructs an external datastore to store domain-specific translation knowledge, which derives a kNN distribution to interpolate the prediction distribution of the NMT model via a linear interpolation coefficient 𝜆. Despite its success, kNN retrieval at each timestep leads to substantial time overhead. To address this issue, dominant studies resort to kNN-MT with adaptive retrieval (kNN-MT-AR), which dynamically estimates 𝜆 and skips kNN retrieval if 𝜆 is less than a fixed threshold. Unfortunately, kNN-MT-AR does not yield satisfactory results. In this paper, we first conduct a preliminary study to reveal two key limitations of kNN-MT-AR: 1) the optimization gap leads to inaccurate estimation of 𝜆 for determining kNN retrieval skipping, and 2) using a fixed threshold fails to accommodate the dynamic demands for kNN retrieval at different timesteps. To mitigate these limitations, we then propose kNN-MT with dynamic retrieval (kNN-MT-DR) that significantly extends vanilla kNN-MT in two aspects. Firstly, we equip kNN-MT with a MLP-based classifier for determining whether to skip kNN retrieval at each timestep. Particularly, we explore several carefully-designed scalar features to fully exert the potential of the classifier. Secondly, we propose a timestep-aware threshold adjustment method to dynamically generate the threshold, which further improves the efficiency of our model. Experimental results on the widely-used datasets demonstrate the effectiveness and generality of our model.