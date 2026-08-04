---
title: "Provably Neural Active Learning Succeeds via Prioritizing Perplexing Samples"
source: "https://proceedings.mlr.press/v235/bu24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/bu24a/bu24a.pdf"
categories: ['data-selection-and-active-learning-methods', 'neural-network-learning-dynamics-theory']
tags: ['active-learning', 'neural-networks', 'sample-selection', 'theory']
venue: "ICML 2024"
tldr: "Provides theoretical analysis explaining why neural active learning succeeds by prioritizing perplexing/uncertain samples."
---

# Provably Neural Active Learning Succeeds via Prioritizing Perplexing Samples

**Source**: [https://proceedings.mlr.press/v235/bu24a.html](https://proceedings.mlr.press/v235/bu24a.html)

**TLDR**: Provides theoretical analysis explaining why neural active learning succeeds by prioritizing perplexing/uncertain samples.

## Abstract

Neural Network-based active learning (NAL) is a cost-effective data selection technique that utilizes neural networks to select and train on a small subset of samples. While existing work successfully develops various effective or theory-justified NAL algorithms, the understanding of the two commonly used query criteria of NAL: uncertainty-based and diversity-based, remains in its infancy. In this work, we try to move one step forward by offering a unified explanation for the success of both query criteria-based NAL from a feature learning view. Specifically, we consider a feature-noise data model comprising easy-to-learn or hard-to-learn features disrupted by noise, and conduct analysis over 2-layer NN-based NALs in the pool-based scenario. We provably show that both uncertainty-based and diversity-based NAL are inherently amenable to one and the same principle, i.e., striving to prioritize samples that contain yet-to-be-learned features. We further prove that this shared principle is the key to their success-achieve small test error within a small labeled set. Contrastingly, the strategy-free passive learning exhibits a large test error due to the inadequate learning of yet-to-be-learned features, necessitating resort to a significantly larger label complexity for a sufficient test error reduction. Experimental results validate our findings.