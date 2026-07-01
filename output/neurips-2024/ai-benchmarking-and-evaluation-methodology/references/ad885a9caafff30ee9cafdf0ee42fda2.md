---
title: "Optimistic Verifiable Training by Controlling Hardware Nondeterminism"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/ad885a9caafff30ee9cafdf0ee42fda2-Abstract-Conference.html"
categories: ['ai-benchmarking-and-evaluation-methodology', 'machine-learning-theory-and-evaluation-methods']
tags: ['verifiable-training', 'hardware-nondeterminism', 'training-integrity']
venue: "NeurIPS 2024"
tldr: "Proposes an optimistic verifiable training framework that controls hardware nondeterminism to ensure correctness of outsourced model training."
---

# Optimistic Verifiable Training by Controlling Hardware Nondeterminism

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/ad885a9caafff30ee9cafdf0ee42fda2-Abstract-Conference.html](https://papers.nips.cc/paper_files/paper/2024/hash/ad885a9caafff30ee9cafdf0ee42fda2-Abstract-Conference.html)

**TLDR**: Proposes an optimistic verifiable training framework that controls hardware nondeterminism to ensure correctness of outsourced model training.

## Abstract

The increasing compute demands of AI systems has led to the emergence of services that train models on behalf of clients lacking necessary resources. However, ensuring correctness of training and guarding against potential training-time attacks, such as data poisoning and backdoors, poses challenges. Existing works on verifiable training largely fall into two classes: proof-based systems, which can be difficult to scale, and ``optimistic'' methods that consider a trusted third-party auditor who replicates the training process. A key challenge with the latter is that hardware nondeterminism between GPU types during training prevents an auditor from replicating the training process exactly, and such schemes are therefore non-robust. We propose a method that combines training in a higher precision than the target model, rounding after intermediate computation steps, and storing rounding decisions based on an adaptive thresholding procedure, to successfully control for  nondeterminism. Across three different NVIDIA GPUs (A40, Titan XP, RTX 2080 Ti), we achieve exact training replication at FP32 precision for both full-training and fine-tuning of ResNet-50 (23M) and GPT-2 (117M) models. Our  verifiable training scheme significantly decreases the storage and time costs compared to proof-based systems.