---
title: "Differentially Private Set Representations"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/94ffbc2939e18adac36eedf8d38d1ef3-Abstract-Conference.html"
categories: ['privacy-preserving-federated-distributed-learning', 'statistical-inference-and-text-generation-methods\n\nhmm,-let-me-reconsider---looking-more-carefully-at-the-cluster:\n\n**score-matching-and-sampling-methods**']
tags: ['differential-privacy', 'set-representation', 'space-efficiency']
venue: "NeurIPS 2024"
tldr: "Constructs differentially private mechanisms for representing sets with near-optimal space usage and bounded error probability."
---

# Differentially Private Set Representations

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/94ffbc2939e18adac36eedf8d38d1ef3-Abstract-Conference.html](https://papers.nips.cc/paper_files/paper/2024/hash/94ffbc2939e18adac36eedf8d38d1ef3-Abstract-Conference.html)

**TLDR**: Constructs differentially private mechanisms for representing sets with near-optimal space usage and bounded error probability.

## Abstract

We study the problem of differentially private (DP) mechanisms for representingsets of size $k$ from a large universe.Our first construction creates$(\epsilon,\delta)$-DP representations with error probability of $1/(e^\epsilon + 1)$ using space at most $1.05 k \epsilon \cdot \log(e)$ bits wherethe time to construct a representation is $O(k \log(1/\delta))$ while decoding time is $O(\log(1/\delta))$.We also present a second algorithm for pure $\epsilon$-DP representations with the same error using space at most $k \epsilon \cdot \log(e)$ bits, but requiring large decoding times.Our algorithms match the lower bounds on privacy-utility trade-offs (including constants but ignoring $\delta$ factors) and we also present a new space lower boundmatching our constructions up to small constant factors.To obtain our results, we design a new approach embedding sets into random linear systemsdeviating from most prior approaches that inject noise into non-private solutions.