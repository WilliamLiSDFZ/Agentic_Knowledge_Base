---
title: "An Experimental Design Framework for Label-Efficient Supervised Finetuning of Large Language Models"
source: "https://aclanthology.org/2024.findings-acl.390/"
pdf_url: ""
categories: ['llm-training-alignment-and-evaluation', 'label-noise-robust-annotation-learning']
tags: ['supervised-finetuning', 'label-efficiency', 'experimental-design']
venue: "ACL 2024"
tldr: "An experimental design framework for reducing annotation costs while maintaining quality in supervised finetuning of LLMs."
---

# An Experimental Design Framework for Label-Efficient Supervised Finetuning of Large Language Models

**Source**: [https://aclanthology.org/2024.findings-acl.390/](https://aclanthology.org/2024.findings-acl.390/)

**TLDR**: An experimental design framework for reducing annotation costs while maintaining quality in supervised finetuning of LLMs.

## Abstract

AbstractSupervised finetuning (SFT) on instruction datasets has played a crucial role in achieving the remarkable zero-shot generalization capabilities observed in modern large language models (LLMs). However, the annotation efforts required to produce high quality responses for instructions are becoming prohibitively expensive, especially as the number of tasks spanned by instruction datasets continues to increase. Active learning is effective in identifying useful subsets of samples to annotate from an unlabeled pool, but its high computational cost remains a barrier to its widespread applicability in the context of LLMs. To mitigate the annotation cost of SFT and circumvent the computational bottlenecks of active learning, we propose using experimental design. Experimental design techniques select the most informative samples to label, and typically maximize some notion of uncertainty and/or diversity. In our work, we implement a framework that evaluates several existing and novel experimental design techniques and find that these methods consistently yield significant gains in label efficiency with little computational overhead. On generative tasks, to reach the same generalization performance, our methods save 50% of the annotation cost compared to random sampling.