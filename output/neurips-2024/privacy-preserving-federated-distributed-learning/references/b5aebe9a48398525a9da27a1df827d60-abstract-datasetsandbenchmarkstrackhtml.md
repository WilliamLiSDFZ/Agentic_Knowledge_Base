---
title: "HARMONIC: Harnessing LLMs for Tabular Data Synthesis and Privacy Protection"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/b5aebe9a48398525a9da27a1df827d60-Abstract-Datasets_and_Benchmarks_Track.html"
categories: ['llm-safety-robustness-and-privacy-defenses', 'privacy-preserving-federated-distributed-learning']
tags: ['LLM', 'tabular-data-synthesis', 'privacy-protection']
venue: "NeurIPS 2024"
tldr: "Leverages LLMs to synthesize realistic tabular data while preserving privacy for sensitive structured datasets."
---

# HARMONIC: Harnessing LLMs for Tabular Data Synthesis and Privacy Protection

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/b5aebe9a48398525a9da27a1df827d60-Abstract-Datasets_and_Benchmarks_Track.html](https://papers.nips.cc/paper_files/paper/2024/hash/b5aebe9a48398525a9da27a1df827d60-Abstract-Datasets_and_Benchmarks_Track.html)

**TLDR**: Leverages LLMs to synthesize realistic tabular data while preserving privacy for sensitive structured datasets.

## Abstract

Data serves as the fundamental basis for advancing deep learning. The tabular data presented in a structured format is highly valuable for modeling and training.However, even in the era of LLM, obtaining tabular data from sensitive domains remains a challenge due to privacy or copyright concerns. Therefore, exploring the methods for effectively using models like LLMs to generate synthetic tabular data, which is privacy-preserving but similar to original one, is urgent.In this paper, we introduce a new framework HARMONIC for tabular data generation and evaluation by LLMs. In the data generation part of our framework, we employ fine-tuning to generate tabular data and enhance privacy rather than continued pre-training which is often used by previous small-scale LLM-based methods. In particular, we construct an instruction fine-tuning dataset based on the idea of the k-nearest neighbors algorithm to inspire LLMs to discover inter-row relationships. By such fine-tuning, LLMs are trained to remember the format and connections of the data rather than the data itself, which reduces the risk of privacy leakage. The experiments find that our tabular data generation achieves equivalent performance as existing methods but with better privacy by the metric of MLE, DCR, etc.In the evaluation part of our framework, we develop a specific privacy risk metric DLT for LLM synthetic data generation, which quantifies the extent to which the generator itself leaks data. We also developed LLE, a performance evaluation metric for downstream LLM tasks, which is more practical and credible than previous metrics.The experiments show that our data generation method outperform the previous methods in the metrics DLT and LLE.