---
title: "Learning-Efficient Yet Generalizable Collaborative Filtering for Item Recommendation"
source: "https://proceedings.mlr.press/v235/pu24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/pu24a/pu24a.pdf"
categories: ['information-retrieval-and-recommendation-systems', 'optimization-algorithms-convergence-theory']
tags: ['collaborative-filtering', 'recommendation', 'weighted-loss']
venue: "ICML 2024"
tldr: "Proposes a learning-efficient yet generalizable collaborative filtering approach connecting weighted squared loss to ranking objectives."
---

# Learning-Efficient Yet Generalizable Collaborative Filtering for Item Recommendation

**Source**: [https://proceedings.mlr.press/v235/pu24a.html](https://proceedings.mlr.press/v235/pu24a.html)

**TLDR**: Proposes a learning-efficient yet generalizable collaborative filtering approach connecting weighted squared loss to ranking objectives.

## Abstract

The weighted squared loss is a common component in several Collaborative Filtering (CF) algorithms for item recommendation, including the representative implicit Alternating Least Squares (iALS). Despite its widespread use, this loss function lacks a clear connection to ranking objectives such as Discounted Cumulative Gain (DCG), posing a fundamental challenge in explaining the exceptional ranking performance observed in these algorithms. In this work, we make a breakthrough by establishing a connection between squared loss and ranking metrics through a Taylor expansion of the DCG-consistent surrogate loss—softmax loss. We also discover a new surrogate squared loss function, namely Ranking-Generalizable Squared (RG$^2$) loss, and conduct thorough theoretical analyses on the DCG-consistency of the proposed loss function. Later, we present an example of utilizing the RG$^2$ loss with Matrix Factorization (MF), coupled with a generalization upper bound and an ALS optimization algorithm that leverages closed-form solutions over all items. Experimental results over three public datasets demonstrate the effectiveness of the RG$^2$ loss, exhibiting ranking performance on par with, or even surpassing, the softmax loss while achieving faster convergence.