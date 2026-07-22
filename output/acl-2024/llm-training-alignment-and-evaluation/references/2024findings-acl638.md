---
title: "Batch-ICL: Effective, Efficient, and Order-Agnostic In-Context Learning"
source: "https://aclanthology.org/2024.findings-acl.638/"
pdf_url: ""
categories: ['llm-training-alignment-and-evaluation']
tags: ['in-context-learning', 'order-robustness', 'inference-efficiency']
venue: "ACL 2024"
tldr: "Batch-ICL is an order-agnostic in-context learning algorithm that treats ICL as meta-optimization to improve robustness and efficiency."
---

# Batch-ICL: Effective, Efficient, and Order-Agnostic In-Context Learning

**Source**: [https://aclanthology.org/2024.findings-acl.638/](https://aclanthology.org/2024.findings-acl.638/)

**TLDR**: Batch-ICL is an order-agnostic in-context learning algorithm that treats ICL as meta-optimization to improve robustness and efficiency.

## Abstract

AbstractIn this paper, by treating in-context learning (ICL) as a meta-optimization process, we explain why LLMs are sensitive to the order of ICL examples. This understanding leads us to the development of Batch-ICL, an effective, efficient, and order-agnostic inference algorithm for ICL. Differing from the standard N-shot learning approach, Batch-ICL employs N separate 1-shot forward computations and aggregates the resulting meta-gradients. These aggregated meta-gradients are then applied to the forward computation of a zero-shot query to generate the final prediction. This batch processing approach renders the LLM agnostic to the order of ICL examples. Through extensive experiments and analysis, we demonstrate that Batch-ICL consistently outperforms most permutations of ICL examples. In some cases, it even exceeds the performance of the best order for standard ICL, all while reducing the computational resources required. Furthermore, we develop a novel variant of Batch-ICL featuring multiple “epochs” of meta-optimization. This variant implicitly explores permutations of ICL examples, further enhancing ICL performance.