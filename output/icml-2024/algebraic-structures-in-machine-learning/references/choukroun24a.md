---
title: "Learning Linear Block Error Correction Codes"
source: "https://proceedings.mlr.press/v235/choukroun24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/choukroun24a/choukroun24a.pdf"
categories: ['neural-symbolic-combinatorial-optimization-learning', 'algebraic-structures-in-machine-learning']
tags: ['error-correction-codes', 'neural-decoding', 'linear-block-codes']
venue: "ICML 2024"
tldr: "A neural approach for jointly learning and decoding linear block error correction codes, particularly effective for short block lengths."
---

# Learning Linear Block Error Correction Codes

**Source**: [https://proceedings.mlr.press/v235/choukroun24a.html](https://proceedings.mlr.press/v235/choukroun24a.html)

**TLDR**: A neural approach for jointly learning and decoding linear block error correction codes, particularly effective for short block lengths.

## Abstract

Error correction codes are a crucial part of the physical communication layer, ensuring the reliable transfer of data over noisy channels. The design of optimal linear block codes capable of being efficiently decoded is of major concern, especially for short block lengths. While neural decoders have recently demonstrated their advantage over classical decoding techniques, the neural design of the codes remains a challenge. In this work, we propose for the first time a unified encoder-decoder training of binary linear block codes. To this end, we adapt the coding setting to support efficient and differentiable training of the code for end-to-end optimization over the order two Galois field. We also propose a novel Transformer model in which the self-attention masking is performed in a differentiable fashion for the efficient backpropagation of the code gradient. Our results show that (i) the proposed decoder outperforms existing neural decoding on conventional codes, (ii) the suggested framework generates codes that outperform the analogous conventional codes, and (iii) the codes we developed not only excel with our decoder but also show enhanced performance with traditional decoding techniques.