---
title: "SSDM: Scalable Speech Dysfluency Modeling"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/b8adf038ba1da7a58afa2f88f0f0fb8e-Abstract-Conference.html"
categories: ['audio-visual-speech-processing-and-benchmarks', 'ai-benchmarking-and-evaluation-methodology']
tags: ['speech-dysfluency', 'spoken-language', 'scalable-modeling']
venue: "NeurIPS 2024"
tldr: "A scalable speech dysfluency modeling framework addressing scalability, data scarcity, and benchmark gaps for speech therapy and language learning."
---

# SSDM: Scalable Speech Dysfluency Modeling

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/b8adf038ba1da7a58afa2f88f0f0fb8e-Abstract-Conference.html](https://papers.nips.cc/paper_files/paper/2024/hash/b8adf038ba1da7a58afa2f88f0f0fb8e-Abstract-Conference.html)

**TLDR**: A scalable speech dysfluency modeling framework addressing scalability, data scarcity, and benchmark gaps for speech therapy and language learning.

## Abstract

Speech dysfluency modeling is the core module for spoken language learning, and speech therapy. However, there are three challenges. First, current state-of-the-art solutions~~\cite{lian2023unconstrained-udm, lian-anumanchipalli-2024-towards-hudm} suffer from poor scalability. Second, there is a lack of a large-scale dysfluency corpus. Third, there is not an effective learning framework. In this paper, we propose \textit{SSDM: Scalable Speech Dysfluency Modeling}, which (1) adopts articulatory gestures as scalable forced alignment; (2) introduces connectionist subsequence aligner (CSA) to achieve dysfluency alignment; (3) introduces a large-scale simulated dysfluency corpus called Libri-Dys; and (4) develops an end-to-end system by leveraging the power of large language models (LLMs). We expect SSDM to serve as a standard in the area of dysfluency modeling. Demo is available at \url{https://berkeley-speech-group.github.io/SSDM/}.