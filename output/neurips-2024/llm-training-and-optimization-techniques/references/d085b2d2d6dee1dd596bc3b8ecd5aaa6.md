---
title: "Mixture of Adversarial LoRAs: Boosting Robust Generalization in Meta-Tuning"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/d085b2d2d6dee1dd596bc3b8ecd5aaa6-Abstract-Conference.html"
categories: ['llm-training-and-optimization-techniques', 'machine-learning-theory-and-evaluation-methods']
tags: ['adversarial-meta-tuning', 'lora', 'few-shot-learning', 'out-of-domain-generalization', 'robust-fine-tuning']
venue: "NeurIPS 2024"
tldr: "Adversarial Meta-Tuning with a mixture of LoRAs improves robust out-of-domain generalization in few-shot learning scenarios."
---

# Mixture of Adversarial LoRAs: Boosting Robust Generalization in Meta-Tuning

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/d085b2d2d6dee1dd596bc3b8ecd5aaa6-Abstract-Conference.html](https://papers.nips.cc/paper_files/paper/2024/hash/d085b2d2d6dee1dd596bc3b8ecd5aaa6-Abstract-Conference.html)

**TLDR**: Adversarial Meta-Tuning with a mixture of LoRAs improves robust out-of-domain generalization in few-shot learning scenarios.

## Abstract

This paper introduces AMT, an \textbf{A}dversarial \textbf{M}eta-\textbf{T}uning methodology, to boost the robust generalization of pre-trained models in the out-of-domain (OOD) few-shot learning. To address the challenge of transferring knowledge from source domains to unseen target domains, we construct the robust LoRAPool by meta-tuning LoRAs with dual perturbations applied to not only the inputs but also singular values and vectors of the weight matrices at various robustness levels. On top of that, we introduce a simple yet effective test-time merging mechanism to dynamically merge discriminative LoRAs for test-time task customization. Extensive evaluations demonstrate that AMT yields significant improvements, up to 12.92\% in clean generalization and up to 49.72\% in adversarial generalization, over previous state-of-the-art methods across a diverse range of OOD few-shot image classification tasks on three benchmarks, confirming the effectiveness of our approach to boost the robust generalization of pre-trained models. Our code is available at \href{https://github.com/xyang583/AMT}{https://github.com/xyang583/AMT}.