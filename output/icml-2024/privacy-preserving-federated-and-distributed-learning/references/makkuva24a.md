---
title: "LASER: Linear Compression in Wireless Distributed Optimization"
source: "https://proceedings.mlr.press/v235/makkuva24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/makkuva24a/makkuva24a.pdf"
categories: ['privacy-preserving-federated-and-distributed-learning', 'fast-sketching-methods-for-large-scale-optimization']
tags: ['distributed-optimization', 'wireless-communication', 'linear-compression']
venue: "ICML 2024"
tldr: "LASER achieves linear compression for distributed SGD over noisy wireless channels with provable convergence guarantees."
---

# LASER: Linear Compression in Wireless Distributed Optimization

**Source**: [https://proceedings.mlr.press/v235/makkuva24a.html](https://proceedings.mlr.press/v235/makkuva24a.html)

**TLDR**: LASER achieves linear compression for distributed SGD over noisy wireless channels with provable convergence guarantees.

## Abstract

Data-parallel SGD is the de facto algorithm for distributed optimization, especially for large scale machine learning. Despite its merits, communication bottleneck is one of its persistent issues. Most compression schemes to alleviate this either assume noiseless communication links, or fail to achieve good performance on practical tasks. In this paper, we close this gap and introduce LASER: LineAr CompreSsion in WirEless DistRibuted Optimization. LASER capitalizes on the inherent low-rank structure of gradients and transmits them efficiently over the noisy channels. Whilst enjoying theoretical guarantees similar to those of the classical SGD, LASER shows consistent gains over baselines on a variety of practical benchmarks. In particular, it outperforms the state-of-the-art compression schemes on challenging computer vision and GPT language modeling tasks. On the latter, we obtain 50-64% improvement in perplexity over our baselines for noisy channels.