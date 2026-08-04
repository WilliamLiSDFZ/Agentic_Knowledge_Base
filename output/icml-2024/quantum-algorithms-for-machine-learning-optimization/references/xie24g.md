---
title: "Differentially Private Synthetic Data via Foundation Model APIs 2: Text"
source: "https://proceedings.mlr.press/v235/xie24g.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/xie24g/xie24g.pdf"
categories: ['privacy-preserving-federated-and-distributed-learning', 'quantum-algorithms-for-machine-learning-optimization']
tags: ['differential-privacy', 'synthetic-text', 'foundation-models']
venue: "ICML 2024"
tldr: "Generates differentially private synthetic text data by leveraging foundation model APIs without requiring access to model internals."
---

# Differentially Private Synthetic Data via Foundation Model APIs 2: Text

**Source**: [https://proceedings.mlr.press/v235/xie24g.html](https://proceedings.mlr.press/v235/xie24g.html)

**TLDR**: Generates differentially private synthetic text data by leveraging foundation model APIs without requiring access to model internals.

## Abstract

Text data has become extremely valuable due to the emergence of machine learning algorithms that learn from it. A lot of high-quality text data generated in the real world is private and therefore cannot be shared or used freely due to privacy concerns. Generating synthetic replicas of private text data with a formal privacy guarantee, i.e., differential privacy (DP), offers a promising and scalable solution. However, existing methods necessitate DP finetuning of large language models (LLMs) on private data to generate DP synthetic data. This approach is not viable for proprietary LLMs (e.g., GPT-3.5) and also demands considerable computational resources for open-source LLMs. Lin et al. (2024) recently introduced the Private Evolution (PE) algorithm to generate DP synthetic images with only API access to diffusion models. In this work, we propose an augmented PE algorithm, named Aug-PE, that applies to the complex setting of text. We use API access to an LLM and generate DP synthetic text without any model training. We conduct comprehensive experiments on three benchmark datasets. Our results demonstrate that Aug-PE produces DP synthetic text that yields competitive utility with the SOTA DP finetuning baselines. This underscores the feasibility of relying solely on API access of LLMs to produce high-quality DP synthetic texts, thereby facilitating more accessible routes to privacy-preserving LLM applications.