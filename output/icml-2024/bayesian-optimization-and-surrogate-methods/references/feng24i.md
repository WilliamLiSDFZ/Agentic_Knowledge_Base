---
title: "Memory Efficient Neural Processes via Constant Memory Attention Block"
source: "https://proceedings.mlr.press/v235/feng24i.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/feng24i/feng24i.pdf"
categories: ['bayesian-optimization-and-surrogate-methods']
tags: ['neural-processes', 'attention-mechanisms', 'memory-efficiency']
venue: "ICML 2024"
tldr: "Proposes a constant memory attention block for neural processes to enable scalable meta-learning in low-resource settings."
---

# Memory Efficient Neural Processes via Constant Memory Attention Block

**Source**: [https://proceedings.mlr.press/v235/feng24i.html](https://proceedings.mlr.press/v235/feng24i.html)

**TLDR**: Proposes a constant memory attention block for neural processes to enable scalable meta-learning in low-resource settings.

## Abstract

Neural Processes (NPs) are popular meta-learning methods for efficiently modelling predictive uncertainty. Recent state-of-the-art methods, however, leverage expensive attention mechanisms, limiting their applications, particularly in low-resource settings. In this work, we propose Constant Memory Attentive Neural Processes (CMANPs), an NP variant that only requires constant memory. To do so, we first propose an efficient update operation for Cross Attention. Leveraging the update operation, we propose Constant Memory Attention Block (CMAB), a novel attention block that (i) is permutation invariant, (ii) computes its output in constant memory, and (iii) performs constant computation updates. Finally, building on CMAB, we detail Constant Memory Attentive Neural Processes. Empirically, we show CMANPs achieve state-of-the-art results on popular NP benchmarks while being significantly more memory efficient than prior methods.