---
title: "Grid4D: 4D Decomposed Hash Encoding for High-Fidelity Dynamic Gaussian Splatting"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/df8b8c12afcaf65639aa686ececbf00c-Abstract-Conference.html"
categories: ['neural-geometric-shape-representation-learning', 'visual-language-multimodal-generation-reasoning']
tags: ['gaussian-splatting', 'dynamic-scenes', '4d-hash-encoding']
venue: "NeurIPS 2024"
tldr: "Grid4D introduces a 4D decomposed hash encoding scheme for high-fidelity dynamic scene rendering with Gaussian splatting."
---

# Grid4D: 4D Decomposed Hash Encoding for High-Fidelity Dynamic Gaussian Splatting

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/df8b8c12afcaf65639aa686ececbf00c-Abstract-Conference.html](https://papers.nips.cc/paper_files/paper/2024/hash/df8b8c12afcaf65639aa686ececbf00c-Abstract-Conference.html)

**TLDR**: Grid4D introduces a 4D decomposed hash encoding scheme for high-fidelity dynamic scene rendering with Gaussian splatting.

## Abstract

Recently, Gaussian splatting has received more and more attention in the field of static scene rendering. Due to the low computational overhead and inherent flexibility of explicit representations, plane-based explicit methods are popular ways to predict deformations for Gaussian-based dynamic scene rendering models. However, plane-based methods rely on the inappropriate low-rank assumption and excessively decompose the space-time 4D encoding, resulting in overmuch feature overlap and unsatisfactory rendering quality. To tackle these problems, we propose Grid4D, a dynamic scene rendering model based on Gaussian splatting and employing a novel explicit encoding method for the 4D input through the hash encoding. Different from plane-based explicit representations, we decompose the 4D encoding into one spatial and three temporal 3D hash encodings without the low-rank assumption. Additionally, we design a novel attention module that generates the attention scores in a directional range to aggregate the spatial and temporal features. The directional attention enables Grid4D to more accurately fit the diverse deformations across distinct scene components based on the spatial encoded features. Moreover, to mitigate the inherent lack of smoothness in explicit representation methods, we introduce a smooth regularization term that keeps our model from the chaos of deformation prediction. Our experiments demonstrate that Grid4D significantly outperforms the state-of-the-art models in visual quality and rendering speed.