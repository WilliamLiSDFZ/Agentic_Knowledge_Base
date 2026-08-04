---
title: "Privacy-Preserving Embedding via Look-up Table Evaluation with Fully Homomorphic Encryption"
source: "https://proceedings.mlr.press/v235/kim24ab.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/kim24ab/kim24ab.pdf"
categories: ['privacy-preserving-federated-and-distributed-learning', 'information-retrieval-and-recommendation-systems']
tags: ['homomorphic-encryption', 'privacy-preserving-ML', 'embedding-lookup']
venue: "ICML 2024"
tldr: "Proposes a look-up table evaluation method using fully homomorphic encryption for privacy-preserving embedding computations."
---

# Privacy-Preserving Embedding via Look-up Table Evaluation with Fully Homomorphic Encryption

**Source**: [https://proceedings.mlr.press/v235/kim24ab.html](https://proceedings.mlr.press/v235/kim24ab.html)

**TLDR**: Proposes a look-up table evaluation method using fully homomorphic encryption for privacy-preserving embedding computations.

## Abstract

In privacy-preserving machine learning (PPML), homomorphic encryption (HE) has emerged as a significant primitive, allowing the use of machine learning (ML) models while protecting the confidentiality of input data. Although extensive research has been conducted on implementing PPML with HE by developing the efficient construction of private counterparts to ML models, the efficient HE implementation of embedding layers for token inputs such as words remains inadequately addressed. Thus, our study proposes an efficient algorithm for privacy-preserving embedding via look-up table evaluation with HE(HELUT) by developing an encrypted indicator function (EIF) that assures high precision with the use of the approximate HE scheme(CKKS). Based on the proposed EIF, we propose the CodedHELUT algorithm to facilitate an encrypted embedding layer for the first time. CodedHELUT leverages coded inputs to improve overall efficiency and optimize memory usage. Our comprehensive empirical analysis encompasses both synthetic tables and real-world largescale word embedding models. CodedHELUT algorithm achieves amortized evaluation time of 0.018-0.242s for GloVe6B50d, 0.104-01.298s for GloVe42300d, 0.262-3.283s for GPT-2 and BERT embedding layers while maintaining high precision (16 bits)