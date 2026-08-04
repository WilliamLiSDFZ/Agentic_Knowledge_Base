---
title: "Exact Soft Analytical Side-Channel Attacks using Tractable Circuits"
source: "https://proceedings.mlr.press/v235/wedenig24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/wedenig24a/wedenig24a.pdf"
categories: ['soft-analytical-side-channel-attack-methods']
tags: ['side-channel-attacks', 'tractable-circuits', 'probabilistic-inference']
venue: "ICML 2024"
tldr: "Exact soft analytical side-channel attacks are formulated using tractable probabilistic circuits to precisely exploit physical leakage in cryptographic systems."
---

# Exact Soft Analytical Side-Channel Attacks using Tractable Circuits

**Source**: [https://proceedings.mlr.press/v235/wedenig24a.html](https://proceedings.mlr.press/v235/wedenig24a.html)

**TLDR**: Exact soft analytical side-channel attacks are formulated using tractable probabilistic circuits to precisely exploit physical leakage in cryptographic systems.

## Abstract

Detecting weaknesses in cryptographic algorithms is of utmost importance for designing secure information systems. The state-of-the-art soft analytical side-channel attack (SASCA) uses physical leakage information to make probabilistic predictions about intermediate computations and combines these "guesses" with the known algorithmic logic to compute the posterior distribution over the key. This attack is commonly performed via loopy belief propagation, which, however, lacks guarantees in terms of convergence and inference quality. In this paper, we develop a fast and exact inference method for SASCA, denoted as ExSASCA, by leveraging knowledge compilation and tractable probabilistic circuits. When attacking the Advanced Encryption Standard (AES), the most widely used encryption algorithm to date, ExSASCA outperforms SASCA by more than 31% top-1 success rate absolute. By leveraging sparse belief messages, this performance is achieved with little more computational cost than SASCA, and about 3 orders of magnitude less than exact inference via exhaustive enumeration. Even with dense belief messages, ExSASCA still uses 6 times less computations than exhaustive inference.