---
title: "Optimal Transport-based Labor-free Text Prompt Modeling for Sketch Re-identification"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/d7ae0d47fe6a8dfeb6a149be03ea89ce-Abstract-Conference.html"
categories: ['optimal-transport-and-learning-theory', 'generative-models-for-visual-style-and-appearance']
tags: ['optimal-transport', 'sketch-reidentification', 'text-prompt-modeling']
venue: "NeurIPS 2024"
tldr: "An optimal transport-based labor-free text prompt approach bridges the modality gap in sketch-based person re-identification."
---

# Optimal Transport-based Labor-free Text Prompt Modeling for Sketch Re-identification

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/d7ae0d47fe6a8dfeb6a149be03ea89ce-Abstract-Conference.html](https://papers.nips.cc/paper_files/paper/2024/hash/d7ae0d47fe6a8dfeb6a149be03ea89ce-Abstract-Conference.html)

**TLDR**: An optimal transport-based labor-free text prompt approach bridges the modality gap in sketch-based person re-identification.

## Abstract

Sketch Re-identification (Sketch Re-ID), which aims to retrieve target person from an image gallery based on a sketch query, is crucial for criminal investigation, law enforcement, and missing person searches. Existing methods aim to alleviate the modality gap by employing semantic metrics constraints or auxiliary modal guidance. However, they incur expensive labor costs and inevitably omit fine-grained modality-consistent information due to the abstraction of sketches.To address this issue, this paper proposes a novel $\textit{Optimal Transport-based Labor-free Text Prompt Modeling}$ (OLTM) network, which hierarchically extracts coarse- and fine-grained similarity representations guided by textual semantic information without any additional annotations. Specifically, multiple target attributes are flexibly obtained by a pre-trained visual question answering (VQA) model. Subsequently, a text prompt reasoning module employs learnable prompt strategy and optimal transport algorithm to extract discriminative global and local text representations, which serve as a bridge for hierarchical and multi-granularity modal alignment between sketch and image modalities.Additionally, instead of measuring the similarity of two samples by only computing their distance, a novel triplet assignment loss is further proposed, in which the whole data distribution also contributes to optimizing the inter/intra-class distances. Extensive experiments conducted on two public benchmarks consistently demonstrate the robustness and superiority of our OLTM over state-of-the-art methods.