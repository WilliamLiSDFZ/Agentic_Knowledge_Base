---
title: "Bottleneck-Minimal Indexing for Generative Document Retrieval"
source: "https://proceedings.mlr.press/v235/du24j.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/du24j/du24j.pdf"
categories: ['information-retrieval-and-recommendation-systems']
tags: ['generative-document-retrieval', 'information-bottleneck', 'indexing', 'autoregressive-models']
venue: "ICML 2024"
tldr: "An information-theoretic bottleneck-minimal indexing approach is proposed to improve generative document retrieval by optimizing document identifiers."
---

# Bottleneck-Minimal Indexing for Generative Document Retrieval

**Source**: [https://proceedings.mlr.press/v235/du24j.html](https://proceedings.mlr.press/v235/du24j.html)

**TLDR**: An information-theoretic bottleneck-minimal indexing approach is proposed to improve generative document retrieval by optimizing document identifiers.

## Abstract

We apply an information-theoretic perspective to reconsider generative document retrieval (GDR), in which a document $x \in \mathcal{X}$ is indexed by $t \in \mathcal{T}$, and a neural autoregressive model is trained to map queries $\mathcal{Q}$ to $\mathcal{T}$. GDR can be considered to involve information transmission from documents $\mathcal{X}$ to queries $\mathcal{Q}$, with the requirement to transmit more bits via the indexes $\mathcal{T}$. By applying Shannon’s rate-distortion theory, the optimality of indexing can be analyzed in terms of the mutual information, and the design of the indexes $\mathcal{T}$ can then be regarded as a bottleneck in GDR. After reformulating GDR from this perspective, we empirically quantify the bottleneck underlying GDR. Finally, using the NQ320K and MARCO datasets, we evaluate our proposed bottleneck-minimal indexing method in comparison with various previous indexing methods, and we show that it outperforms those methods.