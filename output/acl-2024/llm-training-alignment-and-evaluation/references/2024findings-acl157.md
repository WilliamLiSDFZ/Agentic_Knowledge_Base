---
title: "Self-Specialization: Uncovering Latent Expertise within Large Language Models"
source: "https://aclanthology.org/2024.findings-acl.157/"
categories: ['llm-training-alignment-and-evaluation']
tags: ['self-alignment', 'specialization', 'instruction-tuning']
venue: "ACL 2024"
tldr: "Proposes self-specialization to uncover and activate latent domain expertise within LLMs using self-generated data."
---

# Self-Specialization: Uncovering Latent Expertise within Large Language Models

**Source**: [https://aclanthology.org/2024.findings-acl.157/](https://aclanthology.org/2024.findings-acl.157/)

**TLDR**: Proposes self-specialization to uncover and activate latent domain expertise within LLMs using self-generated data.

## Abstract

AbstractRecent works have demonstrated the effectiveness of self-alignment in which a large language model is aligned to follow general instructions using instructional data generated from the model itself starting from a handful of human-written seeds. Instead of general alignment, in this work, we focus on self-alignment for expert domain specialization (e.g., biomedicine, finance). As a preliminary, we quantitively show the marginal effect that generic instruction-following training has on downstream expert domains’ performance. To remedy this, we propose self-specialization - allowing for effective model specialization while achieving cross-task generalization by leveraging only a few labeled seeds. Self-specialization offers a data- and parameter-efficient way of “carving out” an expert model out of a generalist pre-trained LLM. Exploring a variety of popular open large models as a base for specialization, our experimental results in both biomedical and financial domains show that our self-specialized models outperform their base models by a large margin, and even larger models that are generally instruction-tuned or that have been adapted to the target domain by other means.