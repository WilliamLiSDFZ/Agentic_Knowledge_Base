---
title: "Empowering Graph Invariance Learning with Deep Spurious Infomax"
source: "https://proceedings.mlr.press/v235/yao24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/yao24a/yao24a.pdf"
categories: ['graph-neural-networks-and-topology']
tags: ['graph-neural-networks', 'invariance-learning', 'out-of-distribution', 'spurious-correlations']
venue: "ICML 2024"
tldr: "A deep spurious infomax framework is introduced to enhance graph invariance learning for OOD generalization."
---

# Empowering Graph Invariance Learning with Deep Spurious Infomax

**Source**: [https://proceedings.mlr.press/v235/yao24a.html](https://proceedings.mlr.press/v235/yao24a.html)

**TLDR**: A deep spurious infomax framework is introduced to enhance graph invariance learning for OOD generalization.

## Abstract

Recently, there has been a surge of interest in developing graph neural networks that utilize the invariance principle on graphs to generalize the out-of-distribution (OOD) data. Due to the limited knowledge about OOD data, existing approaches often pose assumptions about the correlation strengths of the underlying spurious features and the target labels. However, this prior is often unavailable and will change arbitrarily in the real-world scenarios, which may lead to severe failures of the existing graph invariance learning methods. To bridge this gap, we introduce a novel graph invariance learning paradigm, which induces a robust and general inductive bias, which is built upon the observation that the infomax principle encourages learning spurious features regardless of spurious correlation strengths. We further propose the EQuAD framework that realizes this learning paradigm and employs tailored learning objectives that provably elicit invariant features by disentangling them from the spurious features learned through infomax. Notably, EQuAD shows stable and enhanced performance across different degrees of bias in synthetic datasets and challenging real-world datasets up to 31.76%.